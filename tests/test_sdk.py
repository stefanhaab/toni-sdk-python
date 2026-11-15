"""Tests gegen einen kleinen Nachbau der API. Start: python3 -m unittest discover -s tests -v"""
import json
import os
import sys
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import re

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from toni_sdk import (  # noqa: E402
    ConfirmationRequiredError, PermissionError, RateLimitError, Toni, ToniConnectionError, ToniError, Tool, catalog,
)

anfragen = []
antworten = []


def chat_antwort(**message):
    return {"id": "chatcmpl-1", "object": "chat.completion", "created": 1, "model": "toni-mittel",
            "choices": [{"index": 0, "message": {"role": "assistant", **message}, "finish_reason": "stop"}],
            "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}}


def aufruf(id_, name, args):
    return {"id": id_, "type": "function", "function": {"name": name, "arguments": json.dumps(args)}}


class Nachbau(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _json(self, status, o, kopf=None):
        daten = json.dumps(o).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(daten)))
        for k, v in (kopf or {}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(daten)

    def _bedienen(self):
        roh = self.rfile.read(int(self.headers.get("Content-Length") or 0))
        typ = self.headers.get("Content-Type") or ""
        body = json.loads(roh or b"null") if "json" in typ else roh.decode("latin1")
        anfragen.append({"method": self.command, "url": self.path, "headers": {k.lower(): v for k, v in self.headers.items()}, "body": body})
        if antworten:
            a = antworten.pop(0)
            return self._json(a.get("status", 200), a["body"], a.get("headers"))
        if self.path == "/v1/preise":
            return self._json(200, {"object": "list", "data": [{"id": "toni-leicht", "name": "Leicht", "preis": {}}]})
        if self.path == "/v1/chat/completions" and body.get("stream"):
            self.send_response(200)
            self.send_header("Content-Type", "text/event-stream")
            self.end_headers()
            for s in ("Hal", "lo"):
                self.wfile.write(("data: " + json.dumps({"id": "c", "object": "chat.completion.chunk", "choices": [{"index": 0, "delta": {"content": s}, "finish_reason": None}]}) + "\n\n").encode())
            self.wfile.write(b"data: [DONE]\n\n")
            return None
        if self.path == "/v1/chat/completions":
            return self._json(200, chat_antwort(content="Hallo."))
        if self.path == "/v1/audio/transcriptions":
            return self._json(200, {"text": "gesprochen"})
        if self.path == "/v1/videos/vid_1/content":
            self.send_response(200)
            self.send_header("Content-Type", "video/mp4")
            self.send_header("Content-Length", "3")
            self.end_headers()
            self.wfile.write(bytes([1, 2, 3]))
            return None
        m = re.match(r"^/v1/platform/([a-z_]+)/([a-z0-9_]+)$", self.path)
        if m:
            if m.group(2).startswith("delete") and (body or {}).get("bestaetigt") is not True:
                return self._json(409, {"error": {"message": "Bestätigung fehlt.", "type": "invalid_request_error", "param": None, "code": "bestaetigung_fehlt"}})
            return self._json(200, {"object": "platform.result", "bereich": m.group(1), "werkzeug": m.group(2), "stufe": "lesen",
                                    "data": {"success": True, "data": {"items": [{"id": 4711, "firstname": "Mira"}]}}})
        return self._json(404, {"error": {"message": "Gibt es nicht.", "type": "invalid_request_error", "param": None, "code": "not_found"}})

    do_GET = do_POST = _bedienen


class SdkTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Nachbau)
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()
        cls.basis = f"http://127.0.0.1:{cls.server.server_address[1]}/v1"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()

    def neu(self, **o):
        anfragen.clear()
        antworten.clear()
        return Toni("km_live_test", base_url=self.basis, **o)

    def test_katalog_jede_funktion_ist_eine_methode(self):
        toni = self.neu()
        anzahl = 0
        for a in catalog():
            bereich = getattr(toni, a["name"])
            for f in a["functions"]:
                self.assertTrue(callable(getattr(bereich, f["name"])), f'{a["name"]}.{f["name"]}')
                self.assertLessEqual(len(f'{a["name"]}__{f["name"]}'), 64)
                anzahl += 1
        self.assertGreaterEqual(len(catalog()), 30)
        self.assertGreaterEqual(anzahl, 260)

    def test_plattform_funktion_pfad_schluessel_rueckgabe(self):
        toni = self.neu()
        r = toni.crm.get_leads(status="new", limit=5)
        self.assertEqual(r["data"]["items"][0]["firstname"], "Mira")
        a = anfragen[0]
        self.assertEqual((a["method"], a["url"]), ("POST", "/v1/platform/crm/get_leads"))
        self.assertEqual(a["headers"]["authorization"], "Bearer km_live_test")
        self.assertEqual(a["body"], {"status": "new", "limit": 5})
        self.assertEqual(toni.crm.get_leads({"status": "new"}, limit=2), r)
        self.assertEqual(anfragen[1]["body"], {"status": "new", "limit": 2})
        self.assertEqual(toni.platform.raw("crm", "get_leads")["object"], "platform.result")
        with self.assertRaises(ToniError):
            toni.platform.call("crm/../x", "get_leads")

    def test_loeschen_nur_mit_bestaetigung(self):
        toni = self.neu()
        with self.assertRaises(ConfirmationRequiredError) as c:
            toni.crm.delete_lead(lead_id=4711)
        self.assertEqual(c.exception.code, "bestaetigung_fehlt")
        self.assertTrue(toni.crm.delete_lead(lead_id=4711, confirmed=True)["success"])
        self.assertEqual(anfragen[-1]["body"], {"lead_id": 4711, "bestaetigt": True})

    def test_fehler_klassen_und_wiederholung(self):
        toni = self.neu()
        antworten.append({"status": 403, "body": {"error": {"message": "Recht fehlt.", "type": "permission_error", "param": None, "code": "recht_fehlt"}}})
        with self.assertRaises(PermissionError) as c:
            toni.models.list()
        self.assertEqual((c.exception.status, c.exception.code, str(c.exception)), (403, "recht_fehlt", "Recht fehlt."))
        grenze = {"status": 429, "body": {"error": {"message": "Zu viele.", "code": "rate_limit"}}, "headers": {"Retry-After": "0"}}
        antworten.extend([dict(grenze), {"body": {"object": "list", "data": []}}])
        self.assertEqual(toni.models.list()["object"], "list")
        self.assertEqual(len(anfragen), 3)
        antworten.append(dict(grenze))
        with self.assertRaises(RateLimitError):
            toni.crm.create_lead(data={"email": "a@b.de"})
        self.assertEqual(len(anfragen), 4)  # schreibende Aufrufe werden nicht wiederholt

    def test_ohne_schluessel(self):
        alt = {k: os.environ.pop(k, None) for k in ("TONI_API_KEY", "KM_KEY")}
        try:
            anfragen.clear()
            toni = Toni(base_url=self.basis)
            with self.assertRaises(ToniError) as c:
                toni.ask("Hallo")
            self.assertIn("TONI_API_KEY", str(c.exception))
            self.assertEqual(toni.prices()["data"][0]["id"], "toni-leicht")
            self.assertNotIn("authorization", anfragen[0]["headers"])
        finally:
            for k, v in alt.items():
                if v is not None:
                    os.environ[k] = v

    def test_nicht_erreichbar(self):
        toni = Toni("km_live_test", base_url="http://127.0.0.1:9/v1", max_retries=0, timeout=2)
        with self.assertRaises(ToniConnectionError):
            toni.ask("Hallo")

    def test_chat_strom_transkription_video(self):
        toni = self.neu()
        self.assertEqual(toni.ask("Sag Hallo", system="Kurz."), "Hallo.")
        self.assertEqual([m["role"] for m in anfragen[0]["body"]["messages"]], ["system", "user"])
        self.assertEqual("".join(toni.stream("Sag Hallo")), "Hallo")
        stuecke = list(toni.chat.completions.create(model="toni-leicht", messages=[{"role": "user", "content": "x"}], stream=True))
        self.assertEqual(len(stuecke), 2)
        self.assertEqual(toni.audio.transcriptions.create(file=("a.mp3", b"\x00\x01"), language="de")["text"], "gesprochen")
        a = anfragen[-1]
        self.assertIn("multipart/form-data", a["headers"]["content-type"])
        self.assertIn('name="file"; filename="a.mp3"', a["body"])
        self.assertIn("toni-transkription", a["body"])
        self.assertEqual(toni.videos.content("vid_1"), bytes([1, 2, 3]))

    def test_agent_mit_bereichen(self):
        toni = self.neu()
        agent = toni.agent(areas=["crm"])
        self.assertIn("crm__get_leads", agent.tool_names)
        self.assertNotIn("crm__create_lead", agent.tool_names)
        antworten.extend([
            {"body": chat_antwort(content=None, tool_calls=[aufruf("c1", "crm__get_leads", {"status": "new"})])},
            {"body": {"object": "platform.result", "bereich": "crm", "werkzeug": "get_leads", "stufe": "lesen", "data": {"success": True, "data": {"items": [{"firstname": "Mira"}]}}}},
            {"body": chat_antwort(content="Mira hat sich gemeldet.")},
        ])
        schritte = []
        agent = toni.agent(areas=["crm"], on_step=schritte.append, instructions="Sei knapp.")
        r = agent.run("Wer hat sich gemeldet?")
        self.assertEqual((r.text, r.finish, len(r.steps)), ("Mira hat sich gemeldet.", "stop", 1))
        self.assertEqual((r.steps[0].tool, r.steps[0].failed, len(schritte)), ("crm/get_leads", False, 1))
        self.assertEqual(r.usage["total_tokens"], 30)
        self.assertIn("Sei knapp.", anfragen[0]["body"]["messages"][0]["content"])
        self.assertEqual(anfragen[1]["url"], "/v1/platform/crm/get_leads")
        letzte = anfragen[2]["body"]["messages"]
        self.assertEqual((letzte[-1]["role"], letzte[-1]["tool_call_id"]), ("tool", "c1"))
        self.assertIn("Mira", letzte[-1]["content"])

    def test_agent_schreiben_und_loeschen_nur_mit_erlaubnis(self):
        toni = self.neu()
        # Nur lesen: der Aufruf einer Schreib-Funktion erreicht die Plattform nicht.
        antworten.extend([
            {"body": chat_antwort(content=None, tool_calls=[aufruf("c1", "toni_funktion_aufrufen", {"bereich": "crm", "funktion": "create_lead", "parameter": {"data": {}}})])},
            {"body": chat_antwort(content="Das darf ich nicht.")},
        ])
        r = toni.agent().run("Leg einen Lead an.")
        self.assertTrue(r.steps[0].failed)
        self.assertEqual(len([a for a in anfragen if "/platform/" in a["url"]]), 0)

        # Löschen erlaubt, aber niemand bestätigt.
        toni = self.neu()
        antworten.extend([
            {"body": chat_antwort(content=None, tool_calls=[aufruf("c1", "crm__delete_lead", {"lead_id": 1, "bestaetigt": True})])},
            {"body": chat_antwort(content="Nicht gelöscht.")},
        ])
        r = toni.agent(areas=["crm"], allow=["lesen", "loeschen"]).run("Lösch Lead 1.")
        self.assertTrue(r.steps[0].failed)
        self.assertEqual(len([a for a in anfragen if "/platform/" in a["url"]]), 0)

        # Mensch lehnt ab, dann stimmt er zu. Das Modell kann `bestaetigt` nicht selbst setzen.
        for antwort, erwartet in ((False, 0), (True, 1)):
            toni = self.neu()
            gefragt = []
            antworten.extend([
                {"body": chat_antwort(content=None, tool_calls=[aufruf("c1", "crm__delete_lead", {"lead_id": 1, "bestaetigt": True})])},
                *([{"body": {"object": "platform.result", "data": {"success": True}}}] if antwort else []),
                {"body": chat_antwort(content="Fertig.")},
            ])
            agent = toni.agent(areas=["crm"], allow=["lesen", "loeschen"], on_confirm=lambda c, a=antwort: gefragt.append(c) or a)
            self.assertNotIn("bestaetigt", json.dumps(next(d for d in agent.toolbox.definitions if d["function"]["name"] == "crm__delete_lead")))
            r = agent.run("Lösch Lead 1.")
            plattform = [a for a in anfragen if "/platform/" in a["url"]]
            self.assertEqual(len(plattform), erwartet)
            self.assertEqual((gefragt[0].name, gefragt[0].args), ("delete_lead", {"lead_id": 1}))
            self.assertEqual(r.steps[0].failed, not antwort)
            if antwort:
                self.assertEqual(plattform[0]["body"], {"lead_id": 1, "bestaetigt": True})

    def test_agent_ohne_bereiche_sucht_eigene_werkzeuge_rundengrenze(self):
        toni = self.neu()
        uhr = Tool(name="uhrzeit", description="Sagt die Uhrzeit.", execute=lambda a: {"zeit": "12:00"})
        agent = toni.agent(tools=[uhr], max_steps=2)
        self.assertEqual(agent.tool_names, ["uhrzeit", "toni_funktion_suchen", "toni_funktion_aufrufen"])
        antworten.extend([
            {"body": chat_antwort(content=None, tool_calls=[aufruf("c1", "toni_funktion_suchen", {"suche": "leads"}), aufruf("c2", "uhrzeit", {})])},
            {"body": chat_antwort(content=None, tool_calls=[aufruf("c3", "toni_funktion_aufrufen", {"bereich": "crm", "funktion": "gibt_es_nicht"})])},
            {"body": chat_antwort(content="Ende.")},
        ])
        r = agent.run("Such was.")
        self.assertEqual((r.finish, [s.tool for s in r.steps]), ("max_steps", ["uhrzeit"]))
        zweite = anfragen[1]["body"]["messages"]
        self.assertIn("get_leads", zweite[-2]["content"])
        self.assertIn("12:00", zweite[-1]["content"])
        self.assertNotIn("tools", anfragen[2]["body"])  # letzte Runde ohne Werkzeuge
        antworten.append({"body": chat_antwort(content="Weiter.")})
        r2 = agent.run("Und jetzt?", messages=r.messages)
        self.assertEqual(r2.text, "Weiter.")
        self.assertEqual(len(r2.messages), len(r.messages) + 2)
        with self.assertRaises(ToniError):
            toni.agent(areas=["gibt_es_nicht"])

    def test_terminal_login_logout_verbinden(self):
        import contextlib
        import io
        import stat
        import tempfile
        from toni_sdk import cli

        def toni(*args):
            aus, err = io.StringIO(), io.StringIO()
            code = 0
            argv = sys.argv
            sys.argv = ["toni", *args]
            try:
                with contextlib.redirect_stdout(aus), contextlib.redirect_stderr(err):
                    cli.main()
            except SystemExit as e:
                code = e.code
            finally:
                sys.argv = argv
            return code, aus.getvalue(), err.getvalue()

        alt = {k: os.environ.pop(k, None) for k in ("TONI_API_KEY", "KM_KEY", "XDG_CONFIG_HOME", "TONI_BASE_URL")}
        with tempfile.TemporaryDirectory() as ordner:
            os.environ["XDG_CONFIG_HOME"] = ordner
            os.environ["TONI_BASE_URL"] = self.basis
            datei = os.path.join(ordner, "toni", "config.json")
            try:
                anfragen.clear()
                antworten[:] = [{"status": 401, "body": {"error": {"message": "Falsch.", "type": "authentication_error", "param": None, "code": "invalid_api_key"}}}]
                code, _, err = toni("login", "km_live_falsch")
                self.assertEqual(code, 1)
                self.assertIn("nicht angenommen", err)
                self.assertFalse(os.path.exists(datei))

                antworten[:] = [{"body": {"object": "list", "data": []}}]
                self.assertEqual(toni("login", "km_live_gespeichert")[0], 0)
                with open(datei, encoding="utf-8") as f:
                    self.assertEqual(json.load(f)["api_key"], "km_live_gespeichert")
                self.assertEqual(stat.S_IMODE(os.stat(datei).st_mode), 0o600)

                anfragen.clear()
                self.assertEqual(toni("--bereiche", "crm", "Hallo")[1].strip(), "Hallo.")
                self.assertEqual(anfragen[0]["headers"]["authorization"], "Bearer km_live_gespeichert")

                self.assertIn("gelöscht", toni("logout")[1])
                self.assertFalse(os.path.exists(datei))
                self.assertIn("toni login", toni("Hallo")[2])

                hermes = toni("verbinden", "hermes")[1]
                self.assertIn("https://app.landingpage.tools/mcp", hermes)
                self.assertIn("mcp_servers", hermes)
                self.assertIn("streamable-http", toni("verbinden", "openclaw")[1])
            finally:
                for k in ("XDG_CONFIG_HOME", "TONI_BASE_URL"):
                    os.environ.pop(k, None)
                for k, v in alt.items():
                    if v is not None:
                        os.environ[k] = v


if __name__ == "__main__":
    unittest.main()
