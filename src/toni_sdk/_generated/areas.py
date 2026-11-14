# ERZEUGT von scripts/generate.py aus der OpenAPI-Datei (KI-Markt API 1.0.0-beta). Nicht von Hand ändern.
"""Jede Funktion der Plattform als Methode: ``toni.<bereich>.<funktion>(…)``."""
from __future__ import annotations

from typing import Any, Dict, Mapping, Optional, Type


class _Area:
    def __init__(self, platform: Any) -> None:
        self._platform = platform


class BooksArea(_Area):
    """Bücher — Der Bereich books verwaltet die Bücher deines Unternehmens und ihre Kapitel."""

    def get_books(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Bücher auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/books/get_books``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``limit`` (int): Höchstzahl der Bücher in der Antwort (ganze Zahl). Standard ist 10. Eine Obergrenze erzwingt der Code nicht; wähle für große Bestände sinnvolle Seitengrößen, etwa 20 bis 50.
        - ``offset`` (int): Anzahl der Bücher, die am Anfang übersprungen werden (ganze Zahl, Standard 0). Zusammen mit `limit` ergibt das die Seiteneinteilung, z. B. `offset` 10 und `limit` 10 für die zweite Seite.
        - ``status`` (str): Optionaler Filter auf den Status eines Buchs. Erlaubt laut Schema: `draft`, `published`, `in_progress`. Der Vergleich ist exakt; ohne Angabe (oder bei leerem Wert) werden alle Status geliefert.
        """
        return self._platform.call("books", "get_books", {**(params or {}), **kwargs})

    def get_book(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Buch abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/books/get_book``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``book_id`` (int, Pflicht): ID des Buchs als ganze Zahl (Pflicht). Die ID ist die Objekt-ID aus `get_books`, `search_books` oder `create_book`. Bücher anderer Unternehmen werden wie nicht vorhanden behandelt.
        """
        return self._platform.call("books", "get_book", {**(params or {}), **kwargs})

    def search_books(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Bücher suchen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/books/search_books``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``query`` (str, Pflicht): Suchbegriff als Text (Pflicht). Gesucht wird als Teilstring in Titel, Untertitel und Beschreibung. Leere Werte werden abgelehnt.
        - ``limit`` (int): Höchstzahl der Treffer (ganze Zahl, Standard 10). Eine Obergrenze erzwingt der Code nicht.
        - ``offset`` (int): Anzahl der Treffer, die übersprungen werden (ganze Zahl, Standard 0), für das seitenweise Blättern durch die Trefferliste.
        """
        return self._platform.call("books", "search_books", {**(params or {}), **kwargs})

    def create_book(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Buch anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/books/create_book``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``title`` (str, Pflicht): Titel des Buchs (Pflicht, nicht leer). Er wird als Titel gespeichert und dient als Grundlage des Objektschlüssels.
        - ``subtitle`` (str): Optionaler Untertitel als Text. Wird nur gesetzt, wenn er im Körper vorkommt.
        - ``author`` (str): Optionaler Name des Autors oder der Autorin als Text. Er erscheint in allen Buchansichten.
        - ``description`` (str): Optionale Beschreibung oder Klappentext als Text. Die Beschreibung wird auch von `search_books` durchsucht.
        - ``status`` (str): Optionaler Status. Laut Schema `draft`, `published` oder `in_progress`. Ohne Angabe bleibt der Status leer; setze am besten `draft`, wenn du mit einem Entwurf beginnst.
        """
        return self._platform.call("books", "create_book", {**(params or {}), **kwargs})

    def update_book(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Buchdaten ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/books/update_book``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``book_id`` (int, Pflicht): ID des zu ändernden Buchs als ganze Zahl (Pflicht). Das Buch muss zu deinem Unternehmen gehören, sonst kommt „Buch nicht gefunden oder kein Zugriff“.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern (Pflicht). Dokumentierte Felder: `title`, `subtitle`, `author`, `description`, `status` (`draft`, `published`, `in_progress`), `isbn`, `price` (Zahl), `currency` (z. B. `EUR`), `lang`…
        """
        return self._platform.call("books", "update_book", {**(params or {}), **kwargs})

    def delete_book(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Buch löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/books/delete_book``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``book_id`` (int, Pflicht): ID des zu löschenden Buchs als ganze Zahl (Pflicht). Das Buch muss zu deinem Unternehmen gehören; andernfalls kommt „Buch nicht gefunden oder kein Zugriff“.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("books", "delete_book", {**(params or {}), **kwargs}, confirmed=confirmed)

    def copy_book(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Buch kopieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/books/copy_book``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``book_id`` (int, Pflicht): ID des Quellbuchs als ganze Zahl (Pflicht). Das Buch muss zu deinem Unternehmen gehören.
        - ``title`` (str): Optionaler Titel der Kopie. Ohne Angabe wird der Originaltitel mit dem Zusatz „ (Kopie)“ verwendet.
        - ``include_chapters`` (bool): Wahrheitswert, ob die Kapitel mitkopiert werden. Standard ist `true`; mit `false` wird nur das Buch ohne Kapitel angelegt.
        """
        return self._platform.call("books", "copy_book", {**(params or {}), **kwargs})

    def get_book_chapters(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kapitel eines Buchs abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/books/get_book_chapters``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``book_id`` (int, Pflicht): ID des Buchs als ganze Zahl (Pflicht). Das Buch muss zu deinem Unternehmen gehören, sonst kommt „Buch nicht gefunden oder kein Zugriff“.
        """
        return self._platform.call("books", "get_book_chapters", {**(params or {}), **kwargs})

    def create_chapter(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kapitel anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/books/create_chapter``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``book_id`` (int, Pflicht): ID des Buchs als ganze Zahl (Pflicht), zu dem das Kapitel gehört. Das Buch muss zu deinem Unternehmen gehören.
        - ``title`` (str, Pflicht): Titel des Kapitels als Text (Pflicht, nicht leer). Er dient auch als Grundlage für den internen Objektschlüssel.
        - ``content`` (str): Optionaler Inhalt des Kapitels als Text oder HTML. Ohne Angabe bleibt das Kapitel leer; der Inhalt lässt sich später mit `update_chapter` ergänzen.
        - ``order`` (int): Optionale Position des Kapitels (ganze Zahl). Ohne Angabe wird das Kapitel hinten angefügt. Bereits vorhandene Positionen werden nicht automatisch umsortiert.
        - ``status`` (str): Optionaler Status des Kapitels als frei wählbarer Text, z. B. `draft`. Ohne Angabe bleibt der Status leer.
        """
        return self._platform.call("books", "create_chapter", {**(params or {}), **kwargs})

    def update_chapter(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kapitel ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/books/update_chapter``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``chapter_id`` (int, Pflicht): ID des Kapitels als ganze Zahl (Pflicht). Das Kapitel muss zu einem Buch deines Unternehmens gehören.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern (Pflicht). Erlaubt sind `title`, `subtitle`, `summary`, `introduction`, `content` (Text oder HTML), `order` (ganze Zahl) und `status` (Text). Nur enthaltene Felder werden geändert.
        """
        return self._platform.call("books", "update_chapter", {**(params or {}), **kwargs})

    def delete_chapter(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Kapitel löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/books/delete_chapter``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``chapter_id`` (int, Pflicht): ID des zu löschenden Kapitels als ganze Zahl (Pflicht). Die ID stammt aus `get_book_chapters` oder `create_chapter`; das Kapitel muss zu einem Buch deines Unternehmens gehören.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("books", "delete_chapter", {**(params or {}), **kwargs}, confirmed=confirmed)

    def reorder_chapters(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kapitelreihenfolge ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/books/reorder_chapters``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``book_id`` (int, Pflicht): ID des Buchs als ganze Zahl (Pflicht). Nur Kapitel dieses Buchs werden umsortiert; Kapitel anderer Bücher in der Liste werden ignoriert.
        - ``ordering`` (list, Pflicht): Liste von Objekten (Pflicht), jeweils mit `chapter_id` (ID des Kapitels) und `order` (neue Position als ganze Zahl). Beispiel: `[{"chapter_id": 9101, "order": 2}, {"chapter_id": 9102, "order": 1}]`.
        """
        return self._platform.call("books", "reorder_chapters", {**(params or {}), **kwargs})

    def get_book_statistics(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Buchstatistiken abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/books/get_book_statistics``
        """
        return self._platform.call("books", "get_book_statistics", {**(params or {}), **kwargs})

    def export_book_as_pdf(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Buchexport starten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/books/export_book_as_pdf``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``book_id`` (int, Pflicht): ID des zu exportierenden Buchs als ganze Zahl (Pflicht). Das Buch muss zu deinem Unternehmen gehören, sonst kommt „Buch nicht gefunden oder kein Zugriff“.
        """
        return self._platform.call("books", "export_book_as_pdf", {**(params or {}), **kwargs})

    def get_isbn_status(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """ISBN-Status prüfen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/books/get_isbn_status``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``book_id`` (int, Pflicht): ID des Buchs als ganze Zahl (Pflicht). Das Buch muss zu deinem Unternehmen gehören, sonst kommt „Buch nicht gefunden oder kein Zugriff“.
        """
        return self._platform.call("books", "get_isbn_status", {**(params or {}), **kwargs})


class AudiobooksArea(_Area):
    """Hörbücher — Der Bereich audiobooks verwaltet die Hörbücher deines Unternehmens und ihre Kapitel."""

    def get_audiobooks(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Hörbücher auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/audiobooks/get_audiobooks``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``limit`` (int): Höchstzahl der Hörbücher in der Antwort (ganze Zahl, Standard 10). Eine Obergrenze erzwingt der Code nicht.
        - ``offset`` (int): Anzahl der Einträge, die am Anfang übersprungen werden (ganze Zahl, Standard 0), für das seitenweise Blättern zusammen mit `limit`.
        - ``status`` (str): Optionaler Filter auf den Status als Text, z. B. `draft`, `in_production`, `ready`, `processing` oder `error`. Der Vergleich ist exakt; ohne Angabe werden alle Status geliefert.
        """
        return self._platform.call("audiobooks", "get_audiobooks", {**(params or {}), **kwargs})

    def get_audiobook(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Hörbuch abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/audiobooks/get_audiobook``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``audiobook_id`` (int, Pflicht): ID des Hörbuchs als ganze Zahl (Pflicht). Hörbücher anderer Unternehmen werden wie nicht vorhanden behandelt.
        """
        return self._platform.call("audiobooks", "get_audiobook", {**(params or {}), **kwargs})

    def search_audiobooks(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Hörbücher suchen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/audiobooks/search_audiobooks``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``query`` (str, Pflicht): Suchbegriff als Text (Pflicht). Gesucht wird als Teilstring in Titel und Beschreibung. Leere Werte werden abgelehnt.
        - ``limit`` (int): Höchstzahl der Treffer (ganze Zahl, Standard 10). Eine Obergrenze erzwingt der Code nicht.
        - ``offset`` (int): Anzahl der Treffer, die übersprungen werden (ganze Zahl, Standard 0), um durch längere Trefferlisten zu blättern.
        """
        return self._platform.call("audiobooks", "search_audiobooks", {**(params or {}), **kwargs})

    def create_audiobook(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Hörbuch anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/audiobooks/create_audiobook``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``title`` (str, Pflicht): Titel des Hörbuchs als Text (Pflicht, nicht leer). Er dient auch als Grundlage für den internen Objektschlüssel.
        - ``subtitle`` (str): Optionaler Untertitel als Text. Leere Werte werden ignoriert.
        - ``description`` (str): Optionale Beschreibung als Text. Sie wird von `search_audiobooks` mit durchsucht. Leere Werte werden ignoriert.
        - ``status`` (str): Optionaler Status. Laut Schema `draft`, `in_production` oder `ready`. Ohne Angabe wird `draft` gesetzt.
        """
        return self._platform.call("audiobooks", "create_audiobook", {**(params or {}), **kwargs})

    def update_audiobook(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Hörbuchdaten ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/audiobooks/update_audiobook``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``audiobook_id`` (int, Pflicht): ID des zu ändernden Hörbuchs als ganze Zahl (Pflicht). Es muss zu deinem Unternehmen gehören, sonst kommt „Hörbuch nicht gefunden oder kein Zugriff“.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern (Pflicht). Wirksam sind `title`, `subtitle`, `description`, `status` (z. B. `draft`, `in_production`, `ready`), `publishDate` (ISO 8601, z. B. `2026-09-01`), `price` (Zahl), `currency…
        """
        return self._platform.call("audiobooks", "update_audiobook", {**(params or {}), **kwargs})

    def delete_audiobook(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Hörbuch löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/audiobooks/delete_audiobook``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``audiobook_id`` (int, Pflicht): ID des zu löschenden Hörbuchs als ganze Zahl (Pflicht). Das Hörbuch muss zu deinem Unternehmen gehören; andernfalls kommt „Hörbuch nicht gefunden oder kein Zugriff“.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("audiobooks", "delete_audiobook", {**(params or {}), **kwargs}, confirmed=confirmed)

    def get_audiobook_chapters(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kapitel eines Hörbuchs abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/audiobooks/get_audiobook_chapters``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``audiobook_id`` (int, Pflicht): ID des Hörbuchs als ganze Zahl (Pflicht). Es muss zu deinem Unternehmen gehören, sonst kommt „Hörbuch nicht gefunden oder kein Zugriff“.
        """
        return self._platform.call("audiobooks", "get_audiobook_chapters", {**(params or {}), **kwargs})

    def create_audiobook_chapter(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Hörbuch-Kapitel anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/audiobooks/create_audiobook_chapter``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``audiobook_id`` (int, Pflicht): ID des Hörbuchs als ganze Zahl (Pflicht), zu dem das Kapitel gehört. Es muss zu deinem Unternehmen gehören.
        - ``title`` (str, Pflicht): Titel des Kapitels als Text (Pflicht, nicht leer). Er dient auch als Grundlage für den internen Objektschlüssel.
        - ``content`` (str): Optionaler Kapiteltext als Text. Er ist die Grundlage für die spätere Sprachausgabe. Leere Werte werden ignoriert.
        - ``order`` (int): Optionale Position des Kapitels (ganze Zahl, größer als 0). Ohne Angabe oder bei 0 wird das Kapitel hinten angefügt.
        - ``status`` (str): Optionaler Status als Text; üblich sind `draft`, `ready` und `error`. Ohne Angabe wird `draft` gesetzt.
        """
        return self._platform.call("audiobooks", "create_audiobook_chapter", {**(params or {}), **kwargs})

    def update_audiobook_chapter(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Hörbuch-Kapitel ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/audiobooks/update_audiobook_chapter``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``chapter_id`` (int, Pflicht): ID des Kapitels als ganze Zahl (Pflicht). Das zugehörige Hörbuch muss zu deinem Unternehmen gehören.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern (Pflicht). Wirksam sind `title`, `content` (Text), `order` (ganze Zahl), `status` (Text, z. B. `draft`, `ready`, `error`) und `summary` (Text). Nur enthaltene Felder werden geändert.
        """
        return self._platform.call("audiobooks", "update_audiobook_chapter", {**(params or {}), **kwargs})

    def delete_audiobook_chapter(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Hörbuch-Kapitel löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/audiobooks/delete_audiobook_chapter``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``chapter_id`` (int, Pflicht): ID des zu löschenden Kapitels als ganze Zahl (Pflicht). Die ID stammt aus `get_audiobook_chapters` oder `create_audiobook_chapter`.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("audiobooks", "delete_audiobook_chapter", {**(params or {}), **kwargs}, confirmed=confirmed)

    def create_chapter_audio(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kapiteltext für Sprachausgabe aufbereiten

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/audiobooks/create_chapter_audio``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``chapter_id`` (int, Pflicht): ID des Kapitels als ganze Zahl (Pflicht). Das zugehörige Hörbuch muss zu deinem Unternehmen gehören.
        - ``limbic_type`` (str): Optionaler Persönlichkeitstyp, auf den der Text abgestimmt wird. Bekannt sind `traditionalist`, `performer`, `harmoniser`, `stimulant`, `hedonist`, `adventurer` und `disciplined`. Ohne Angabe gilt der am Hörbuch hinterl…
        - ``linguistic_id`` (int): Optionale ID eines linguistischen Profils. Im aktuellen Stand wird der Wert entgegengenommen, hat auf das Ergebnis aber keine Wirkung, weil beim Aufbereiten kein Profil angewendet wird.
        """
        return self._platform.call("audiobooks", "create_chapter_audio", {**(params or {}), **kwargs})


class PodcastsArea(_Area):
    """Podcasts — Der Bereich podcasts verwaltet die Podcasts deines Unternehmens und ihre Episoden."""

    def get_podcasts(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Podcasts auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/podcasts/get_podcasts``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``limit`` (int): Maximale Anzahl der Podcasts in dieser Antwort als ganze Zahl. Standard ist 10. Eine Obergrenze wird nicht erzwungen; wähle für Seiteneinteilung eine feste Größe und erhöhe `offset` entsprechend.
        - ``offset`` (int): Anzahl der Podcasts, die am Anfang der Sortierung (neueste zuerst) übersprungen werden. Standard ist 0. Für die zweite Seite mit `limit` 10 setzt du 10.
        - ``status`` (str): Optionaler Filter auf den Status des Podcasts, z. B. `active`, `draft` oder `archived`. Es wird exakt verglichen; nicht vorhandene Werte liefern eine leere Liste. Ohne Angabe werden alle Status geliefert.
        """
        return self._platform.call("podcasts", "get_podcasts", {**(params or {}), **kwargs})

    def get_podcast(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Podcast-Details abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/podcasts/get_podcast``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``podcast_id`` (int, Pflicht): Numerische ID des Podcasts, wie sie `get_podcasts`, `search_podcasts` oder `create_podcast` als `id` zurückgeben. Pflichtangabe; der Podcast muss zu deiner Firma gehören.
        """
        return self._platform.call("podcasts", "get_podcast", {**(params or {}), **kwargs})

    def search_podcasts(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Podcasts suchen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/podcasts/search_podcasts``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``query`` (str, Pflicht): Suchbegriff, der als Teilstring in Titel oder Beschreibung des Podcasts vorkommen muss. Pflichtangabe; leere Texte werden abgelehnt.
        - ``limit`` (int): Maximale Anzahl der Treffer als ganze Zahl. Standard ist 10. Ohne Obergrenze; für große Treffermengen in Seiten abrufen.
        - ``offset`` (int): Anzahl der Treffer, die am Anfang der alphabetischen Sortierung übersprungen werden. Standard ist 0.
        """
        return self._platform.call("podcasts", "search_podcasts", {**(params or {}), **kwargs})

    def create_podcast(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Podcast anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/podcasts/create_podcast``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``title`` (str, Pflicht): Titel des Podcasts als Text. Pflichtangabe; er wird auch zur Bildung der internen Objektbezeichnung verwendet.
        - ``subtitle`` (str): Optionaler Untertitel (Kurzbeschreibung) des Podcasts. Ohne Angabe bleibt das Feld leer.
        - ``description`` (str): Optionale ausführliche Beschreibung der Sendung, wie sie z. B. im Feed erscheint. Ohne Angabe bleibt das Feld leer.
        - ``status`` (str): Optionaler Status des Podcasts. Dokumentiert sind `active`, `draft` und `archived`; Standard ist `active`. Der Wert wird nicht gegen eine Liste geprüft.
        """
        return self._platform.call("podcasts", "create_podcast", {**(params or {}), **kwargs})

    def update_podcast(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Podcast aktualisieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/podcasts/update_podcast``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``podcast_id`` (int, Pflicht): Numerische ID des zu ändernden Podcasts. Pflichtangabe; der Podcast muss zu deiner Firma gehören.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern. Erlaubte Schlüssel: `title`, `subtitle`, `description`, `status`, `podcastlanguage`, `frequency`, `website`, `primary_category`, `secondary_category`. Werte sind Zeichenketten, z. B.…
        """
        return self._platform.call("podcasts", "update_podcast", {**(params or {}), **kwargs})

    def delete_podcast(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Podcast löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/podcasts/delete_podcast``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``podcast_id`` (int, Pflicht): Numerische ID des zu löschenden Podcasts. Pflichtangabe; der Podcast muss zu deiner Firma gehören, sonst kommt „Podcast nicht gefunden oder kein Zugriff“.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("podcasts", "delete_podcast", {**(params or {}), **kwargs}, confirmed=confirmed)

    def copy_podcast(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Podcast kopieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/podcasts/copy_podcast``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``podcast_id`` (int, Pflicht): Numerische ID des Podcasts, der kopiert werden soll. Pflichtangabe; er muss zu deiner Firma gehören.
        - ``title`` (str): Optionaler Titel der Kopie. Ohne Angabe wird „<Originaltitel> (Kopie)“ verwendet.
        - ``include_episodes`` (bool): Wahrheitswert. Bei `true` werden auch die Episodentexte des Originals kopiert, bei `false` (Standard) entsteht ein Podcast ohne Episoden.
        """
        return self._platform.call("podcasts", "copy_podcast", {**(params or {}), **kwargs})

    def get_episodes(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Episoden eines Podcasts

        Recht am Schlüssel: ``lesen`` · ``POST /platform/podcasts/get_episodes``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``podcast_id`` (int, Pflicht): Numerische ID des Podcasts, dessen Episoden geliefert werden. Pflichtangabe; der Podcast muss zu deiner Firma gehören.
        """
        return self._platform.call("podcasts", "get_episodes", {**(params or {}), **kwargs})

    def get_episode(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Episode-Details abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/podcasts/get_episode``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``episode_id`` (int, Pflicht): Numerische ID der Episode, wie sie `get_episodes`, `search_episodes` oder `create_episode` als `id` liefern. Pflichtangabe.
        """
        return self._platform.call("podcasts", "get_episode", {**(params or {}), **kwargs})

    def search_episodes(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Episoden suchen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/podcasts/search_episodes``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``query`` (str, Pflicht): Suchbegriff, der als Teilstring in Titel oder Beschreibung der Episode vorkommen muss. Pflichtangabe; leere Texte werden abgelehnt.
        - ``limit`` (int): Maximale Anzahl der Treffer als ganze Zahl. Standard ist 10; es gibt keine feste Obergrenze.
        - ``offset`` (int): Anzahl der Treffer, die am Anfang der Sortierung (neueste zuerst) übersprungen werden. Standard ist 0.
        """
        return self._platform.call("podcasts", "search_episodes", {**(params or {}), **kwargs})

    def create_episode(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Episode anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/podcasts/create_episode``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``podcast_id`` (int, Pflicht): Numerische ID des Podcasts, zu dem die Episode gehört. Pflichtangabe; der Podcast muss zu deiner Firma gehören.
        - ``title`` (str, Pflicht): Titel der Episode. Pflichtangabe; er wird auch zur Bildung der internen Objektbezeichnung verwendet.
        - ``number`` (int): Optionale Folgennummer als ganze Zahl. Ohne Angabe wird die Zahl der vorhandenen Episoden des Podcasts plus 1 verwendet.
        - ``description`` (str): Optionale Beschreibung der Episode. Ohne Angabe bleibt das Feld leer.
        """
        return self._platform.call("podcasts", "create_episode", {**(params or {}), **kwargs})

    def update_episode(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Episode aktualisieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/podcasts/update_episode``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``episode_id`` (int, Pflicht): Numerische ID der zu ändernden Episode. Pflichtangabe; die Episode muss zu einem Podcast deiner Firma gehören.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern. Erlaubte Schlüssel: `title`, `description`, `summary`, `shownotes` (Texte), `number` (ganze Zahl), `status` (Fortschrittsstatus als Text) und `publishing_date` (Datum/Zeit, z. B. `20…
        """
        return self._platform.call("podcasts", "update_episode", {**(params or {}), **kwargs})

    def delete_episode(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Episode löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/podcasts/delete_episode``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``episode_id`` (int, Pflicht): Numerische ID der zu löschenden Episode. Pflichtangabe; unbekannte IDs ergeben die Fehlermeldung „Episode nicht gefunden“.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("podcasts", "delete_episode", {**(params or {}), **kwargs}, confirmed=confirmed)

    def get_episode_stats(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Episoden-Kennzahlen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/podcasts/get_episode_stats``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``podcast_id`` (int, Pflicht): Numerische ID des Podcasts, für den die Kennzahlen berechnet werden. Pflichtangabe; der Podcast muss zu deiner Firma gehören.
        """
        return self._platform.call("podcasts", "get_episode_stats", {**(params or {}), **kwargs})

    def get_rss_feed(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """RSS-Feed-Link abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/podcasts/get_rss_feed``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``podcast_id`` (int, Pflicht): Numerische ID des Podcasts, dessen Feed-Link ermittelt wird. Pflichtangabe; der Podcast muss zu deiner Firma gehören.
        """
        return self._platform.call("podcasts", "get_rss_feed", {**(params or {}), **kwargs})

    def schedule_episode(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Episode einplanen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/podcasts/schedule_episode``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``episode_id`` (int, Pflicht): Numerische ID der Episode, die eingeplant werden soll. Pflichtangabe; sie muss zu einem Podcast deiner Firma gehören.
        - ``publish_at`` (str, Pflicht): Gewünschter Veröffentlichungszeitpunkt als Text, bevorzugt ISO-8601 mit Zeitzone, z. B. `2026-11-20T06:00:00+01:00`. Pflichtangabe. Ohne Zeitzone wird die Server-Zeitzone angenommen.
        """
        return self._platform.call("podcasts", "schedule_episode", {**(params or {}), **kwargs})


class PodcastGuestsArea(_Area):
    """Podcast-Gäste — Der Bereich podcast_guests gibt dir einen lesenden Überblick über die Gästeorganisation deiner Podcasts: Welche Gäste (Interviewpartner) sind eingeladen, wo stehen sie im Ablauf, wann und wo ist ihr Aufnahmetermin, und an welchen Aufnahmetagen sind noch Slots frei?"""

    def get_podcast_gaeste(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Podcast-Gäste auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/podcast_guests/get_podcast_gaeste``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``podcast_id`` (int): Numerische ID des Podcasts. Ohne Angabe liefert die Funktion stattdessen die Liste aller Podcasts der Firma mit Gästezahl. Ein unbekannter oder fremder Podcast ergibt den Fehler „Podcast nicht gefunden.“
        - ``status`` (str): Optionaler Filter auf eine Phase: `eingeladen`, `vorbereitung`, `aufnahme`, `nachbereitung` oder `abgesagt`. Wirkt nur zusammen mit `podcast_id`; ohne Filter werden alle Phasen geliefert.
        """
        return self._platform.call("podcast_guests", "get_podcast_gaeste", {**(params or {}), **kwargs})

    def get_podcast_aufnahmetage(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kommende Aufnahmetage

        Recht am Schlüssel: ``lesen`` · ``POST /platform/podcast_guests/get_podcast_aufnahmetage``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``podcast_id`` (int, Pflicht): Numerische ID des Podcasts, dessen Aufnahmetage geliefert werden. Pflichtangabe; der Podcast muss zu deiner Firma gehören, sonst kommt „Podcast nicht gefunden.“
        """
        return self._platform.call("podcast_guests", "get_podcast_aufnahmetage", {**(params or {}), **kwargs})

    def find_podcast_gast_kandidaten(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Gast-Kandidaten suchen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/podcast_guests/find_podcast_gast_kandidaten``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``query`` (str, Pflicht): Suchtext (mindestens 2 Zeichen): Teil eines Namens, einer Firma oder einer E-Mail-Adresse. Pflichtangabe. Kürzere Eingaben liefern eine leere Trefferliste. Das Zeichen `%` und `_` werden wörtlich gesucht.
        """
        return self._platform.call("podcast_guests", "find_podcast_gast_kandidaten", {**(params or {}), **kwargs})


class StoriesArea(_Area):
    """Magazin und Storyfilter — Der Bereich Magazin und Storyfilter verwaltet zwei Arten von Objekten deines Unternehmens: Stories (Magazin-Beiträge mit Titel, Untertitel, Text, Status, Zielkanal und Hashtags) und Storyfilter (Vorgaben für das Erzählen: Zielperson, Wunsch, Probleme, Mentor, Wertversprechen und Nutzen nach dem Heldenreise-Schema A–G)."""

    def get_stories(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Stories auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/stories/get_stories``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Optionaler Filter auf den Status der Story, z. B. `draft` oder `published`. Der Wert wird exakt verglichen; ohne Angabe kommen Stories mit jedem Status.
        - ``limit`` (int): Maximale Anzahl Stories je Antwort. Standard ist 20, kleinere Werte als 1 werden auf 1 angehoben. Ganzzahl.
        - ``offset`` (int): Anzahl der Stories, die am Anfang übersprungen werden, für das Blättern (Standard 0). Zusammen mit `limit` und `total` aus der Antwort kannst du alle Seiten abrufen.
        """
        return self._platform.call("stories", "get_stories", {**(params or {}), **kwargs})

    def get_story(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Story abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/stories/get_story``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``story_id`` (int, Pflicht): ID der Story als Ganzzahl. Pflichtangabe; die ID stammt aus `get_stories` oder `create_story`. Die Story muss zu deinem Unternehmen gehören.
        """
        return self._platform.call("stories", "get_story", {**(params or {}), **kwargs})

    def create_story(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Story anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/stories/create_story``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``data`` (dict, Pflicht): Objekt mit den Feldern der Story. Erlaubt sind: `title` (Titel), `subtitle` (Untertitel), `content` (Text, HTML möglich), `status` (Status der Story; im Datenmodell vorgesehen sind `draft`, `review`, `approved`, `publis…
        """
        return self._platform.call("stories", "create_story", {**(params or {}), **kwargs})

    def update_story(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Story ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/stories/update_story``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``story_id`` (int, Pflicht): ID der zu ändernden Story als Ganzzahl. Pflichtangabe; die Story muss zu deinem Unternehmen gehören.
        - ``data`` (dict, Pflicht): Objekt mit den Feldern der Story. Erlaubt sind: `title` (Titel), `subtitle` (Untertitel), `content` (Text, HTML möglich), `status` (Status der Story; im Datenmodell vorgesehen sind `draft`, `review`, `approved`, `publis…
        """
        return self._platform.call("stories", "update_story", {**(params or {}), **kwargs})

    def delete_story(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Story löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/stories/delete_story``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``story_id`` (int, Pflicht): ID der zu löschenden Story als Ganzzahl. Pflichtangabe; die Story muss zu deinem Unternehmen gehören und wird unwiderruflich entfernt.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("stories", "delete_story", {**(params or {}), **kwargs}, confirmed=confirmed)

    def get_storyfilters(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Storyfilter auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/stories/get_storyfilters``
        """
        return self._platform.call("stories", "get_storyfilters", {**(params or {}), **kwargs})

    def create_storyfilter(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Storyfilter anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/stories/create_storyfilter``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``data`` (dict, Pflicht): Objekt mit den Feldern des Storyfilters. Erlaubt sind: `title`, `description`, `core_message` (Kernbotschaft), `a_character` (Charakter, Heldenreise A), `b_wish` (Wunsch, B), `d_external_problem` (äußeres Problem, D), `…
        """
        return self._platform.call("stories", "create_storyfilter", {**(params or {}), **kwargs})

    def update_storyfilter(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Storyfilter ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/stories/update_storyfilter``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``storyfilter_id`` (int, Pflicht): ID des zu ändernden Storyfilters als Ganzzahl. Pflichtangabe; den Filter findest du mit `get_storyfilters`. Er muss zu deinem Unternehmen gehören.
        - ``data`` (dict, Pflicht): Objekt mit den Feldern des Storyfilters. Erlaubt sind: `title`, `description`, `core_message` (Kernbotschaft), `a_character` (Charakter, Heldenreise A), `b_wish` (Wunsch, B), `d_external_problem` (äußeres Problem, D), `…
        """
        return self._platform.call("stories", "update_storyfilter", {**(params or {}), **kwargs})


class LandingpagesArea(_Area):
    """Landingpages — Der Bereich Landingpages umfasst drei Objektarten deines Unternehmens: Templates (Vorlagen mit Name, Slug, Variante, Farben und Meta-Angaben), Portale (veröffentlichbare Landingpage-Portale mit Titel, Slug, Domain, Sprache und Status, optional mit einem Template und einem Keyword verknüpft) und Keywords (Suchbegriffe mit Suchvolumen, CPC, Intention und Gruppe)."""

    def get_templates(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Templates auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/landingpages/get_templates``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Optionaler Filter auf den Status des Templates, z. B. `draft` oder `active`. Wird exakt verglichen.
        - ``search`` (str): Optionaler Suchtext; gefunden werden Templates, deren Name oder Slug diesen Text enthalten (Teilstring, Groß-/Kleinschreibung egal).
        - ``variant`` (str): Variante, auf die gefiltert wird. Standard ist `landingpage`; Templates ohne Variante werden immer mitgeliefert. Andere Werte sind z. B. `interview` oder `landingcard`.
        - ``include_catalog`` (bool): Wahrheitswert. Bei `true` (Standard) werden zuerst die globalen Katalog-Templates aufgeführt, bei `false` nur die Templates deines Unternehmens.
        - ``limit`` (int): Maximale Anzahl Einträge je Antwort. Standard 20, Werte unter 1 werden auf 1 angehoben. Ganzzahl.
        - ``offset`` (int): Anzahl der Einträge, die am Anfang der zusammengeführten Liste übersprungen werden (Standard 0).
        """
        return self._platform.call("landingpages", "get_templates", {**(params or {}), **kwargs})

    def get_template(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Template abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/landingpages/get_template``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int, Pflicht): ID des Templates als Ganzzahl. Pflichtangabe; das Template muss zu deinem Unternehmen gehören.
        """
        return self._platform.call("landingpages", "get_template", {**(params or {}), **kwargs})

    def create_template(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Template anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/landingpages/create_template``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``name`` (str, Pflicht): Interner Name des Templates. Pflichtangabe, Text; HTML-Zeichen werden maskiert.
        - ``slug`` (str): Optionaler Slug für URLs. Ohne Angabe wird er aus dem Namen abgeleitet. Der Slug wird vereinfacht: Kleinbuchstaben, alle Zeichen außer `a–z`, `0–9` und `-` werden zu `-` (auch Umlaute), Bindestriche am Rand entfallen. B…
        - ``status`` (str): Status des neuen Templates als Text, z. B. `draft` oder `active`. Standard ist `draft`.
        - ``variant`` (str): Template-Variante als Text. Standard ist `landingpage`.
        - ``colors`` (dict): Objekt mit den Farben des Templates. Erlaubte Schlüssel: `body_color` (Textfarbe), `body_background` (Seitenhintergrund), `primary` (Primärfarbe) und `secondary` (Sekundärfarbe), jeweils als Text, üblicherweise Hex-Wert…
        - ``meta`` (dict): Objekt mit den Meta-Angaben für Suchmaschinen: `title` (Seitentitel) und `description` (Beschreibung). Beide sind Texte; nicht angegebene Schlüssel bleiben unverändert.
        """
        return self._platform.call("landingpages", "create_template", {**(params or {}), **kwargs})

    def update_template(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Template ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/landingpages/update_template``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int, Pflicht): ID des zu ändernden Templates als Ganzzahl. Pflichtangabe; das Template muss zu deinem Unternehmen gehören.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern. Erlaubt: `name`, `slug`, `status`, `variant` (jeweils Text), `colors` (Objekt mit `body_color`, `body_background`, `primary`, `secondary`) und `meta` (Objekt mit `title`, `descriptio…
        """
        return self._platform.call("landingpages", "update_template", {**(params or {}), **kwargs})

    def delete_template(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Template löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/landingpages/delete_template``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int, Pflicht): ID des zu löschenden Templates als Ganzzahl. Pflichtangabe; das Template muss zu deinem Unternehmen gehören und wird unwiderruflich entfernt.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("landingpages", "delete_template", {**(params or {}), **kwargs}, confirmed=confirmed)

    def copy_template(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Template kopieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/landingpages/copy_template``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int, Pflicht): ID des Quell-Templates als Ganzzahl. Pflichtangabe; das Template muss zu deinem Unternehmen gehören.
        - ``name`` (str): Optionaler Name der Kopie. Ohne Angabe wird „<Name> (Kopie)“ verwendet.
        - ``slug`` (str): Optionaler Slug der Kopie. Ohne Angabe wird der Slug des Originals mit `-copy` verwendet. Der Slug wird vereinfacht: Kleinbuchstaben, alle Zeichen außer `a–z`, `0–9` und `-` werden zu `-` (auch Umlaute), Bindestriche am…
        """
        return self._platform.call("landingpages", "copy_template", {**(params or {}), **kwargs})

    def get_portals(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Portale auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/landingpages/get_portals``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Optionaler Filter auf den Status des Portals. Im Datenmodell vorgesehen sind `draft` und `public`; der Wert wird exakt verglichen.
        - ``limit`` (int): Maximale Anzahl Portale je Antwort. Standard 20, Werte unter 1 werden auf 1 angehoben.
        - ``offset`` (int): Anzahl der Portale, die am Anfang übersprungen werden (Standard 0), für das Blättern zusammen mit `total`.
        """
        return self._platform.call("landingpages", "get_portals", {**(params or {}), **kwargs})

    def get_portal(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Portal abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/landingpages/get_portal``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``portal_id`` (int, Pflicht): ID des Portals als Ganzzahl. Pflichtangabe; das Portal muss zu deinem Unternehmen gehören.
        """
        return self._platform.call("landingpages", "get_portal", {**(params or {}), **kwargs})

    def create_portal(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Portal anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/landingpages/create_portal``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``title`` (str, Pflicht): Titel des Portals. Pflichtangabe, Text.
        - ``slug`` (str): Optionaler Slug für die URL des Portals. Ohne Angabe wird er aus dem Titel abgeleitet. Der Slug wird vereinfacht: Kleinbuchstaben, alle Zeichen außer `a–z`, `0–9` und `-` werden zu `-` (auch Umlaute), Bindestriche am Ra…
        - ``status`` (str): Status des Portals als Text. Standard `draft`; im Datenmodell vorgesehen sind `draft` und `public`.
        - ``domain`` (str): Optionale Domain oder Subdomain, unter der das Portal erreichbar sein soll, z. B. `ratgeber.example.com`. Standard ist leer.
        - ``lang`` (str): Sprachcode des Portals, z. B. `de` oder `en`. Standard ist `de`.
        - ``template_id`` (int): ID eines vorhandenen Templates deines Unternehmens, das dem Portal zugewiesen wird. Hat Vorrang vor `create_template`.
        - ``keyword_id`` (int): ID eines vorhandenen Keywords deines Unternehmens (siehe `get_keywords`), mit dem das Portal verknüpft wird.
        - ``meta`` (dict): Objekt mit den Meta-Angaben für Suchmaschinen: `title` (Seitentitel) und `description` (Beschreibung). Beide sind Texte; nicht angegebene Schlüssel bleiben unverändert.
        - ``create_template`` (bool): Wahrheitswert. Bei `true` und ohne `template_id` wird zusätzlich ein neues Template mit dem Namen „<Titel> Template“ (Variante `landingpage`) angelegt und dem Portal zugewiesen.
        """
        return self._platform.call("landingpages", "create_portal", {**(params or {}), **kwargs})

    def update_portal(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Portal ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/landingpages/update_portal``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``portal_id`` (int, Pflicht): ID des zu ändernden Portals als Ganzzahl. Pflichtangabe; das Portal muss zu deinem Unternehmen gehören.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern. Erlaubt: `title`, `slug`, `status`, `domain`, `lang` (Texte), `keyword_id` und `template_id` (Ganzzahlen, `0` löst die Verknüpfung) sowie `meta` (Objekt mit `title`, `description`).…
        """
        return self._platform.call("landingpages", "update_portal", {**(params or {}), **kwargs})

    def delete_portal(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Portal löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/landingpages/delete_portal``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``portal_id`` (int, Pflicht): ID des zu löschenden Portals als Ganzzahl. Pflichtangabe; das Portal muss zu deinem Unternehmen gehören und wird unwiderruflich entfernt.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("landingpages", "delete_portal", {**(params or {}), **kwargs}, confirmed=confirmed)

    def get_keywords(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Keywords auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/landingpages/get_keywords``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``group_id`` (int): Optionaler Filter auf die ID einer Keyword-Gruppe (Ganzzahl). Es werden nur Keywords dieser Gruppe geliefert.
        - ``limit`` (int): Maximale Anzahl Keywords je Antwort. Standard 25, Werte unter 1 werden auf 1 angehoben.
        - ``offset`` (int): Anzahl der Keywords, die am Anfang übersprungen werden (Standard 0), zum Blättern zusammen mit `total`.
        """
        return self._platform.call("landingpages", "get_keywords", {**(params or {}), **kwargs})

    def search_keywords(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Keywords suchen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/landingpages/search_keywords``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``query`` (str, Pflicht): Suchtext. Pflichtangabe. Treffer sind Keywords, deren Begriff oder Vorschlagstext diesen Text enthalten; derselbe Text dient als Ausgangspunkt für die Vorschläge.
        - ``limit`` (int): Maximale Gesamtzahl Einträge (gespeicherte Treffer plus Vorschläge). Standard 15, Werte unter 1 werden auf 1 angehoben.
        - ``include_suggestions`` (bool): Wahrheitswert. Bei `true` (Standard) wird die Liste mit Vorschlägen der Autovervollständigung aufgefüllt, solange weniger als `limit` Einträge vorhanden sind; bei `false` kommen nur gespeicherte Keywords.
        """
        return self._platform.call("landingpages", "search_keywords", {**(params or {}), **kwargs})

    def create_keyword(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Keyword anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/landingpages/create_keyword``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``keyword`` (str, Pflicht): Der Suchbegriff als Text. Pflichtangabe; HTML-Zeichen werden maskiert.
        - ``suggest`` (str): Optionaler Vorschlagstext, z. B. die ausführlichere Suchanfrage. Standard ist leer.
        - ``search_volume`` (int): Monatliches Suchvolumen als Ganzzahl. Optional; ohne Angabe bleibt das Feld leer.
        - ``cpc`` (float): Durchschnittlicher Klickpreis als Zahl (die Währung wird nicht gespeichert; bei Abfragen wird USD angenommen). Optional.
        - ``main_intent`` (str): Hauptintention des Suchbegriffs als Text, z. B. `informational`, `commercial` oder `transactional`. Standard ist `informational`.
        - ``group_id`` (int): ID einer Keyword-Gruppe, der das Keyword zugeordnet wird (Ganzzahl). Optional.
        - ``lang`` (str): Sprachcode des Keywords, z. B. `de`. Standard ist `de`.
        - ``competition_level`` (str): Konkurrenzgrad als Text, z. B. `LOW`, `MEDIUM` oder `HIGH`. Optional; der Wert wird nicht geprüft.
        """
        return self._platform.call("landingpages", "create_keyword", {**(params or {}), **kwargs})

    def update_keyword(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Keyword ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/landingpages/update_keyword``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``keyword_id`` (int, Pflicht): ID des zu ändernden Keywords als Ganzzahl. Pflichtangabe; das Keyword muss zu deinem Unternehmen gehören.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern. Erlaubt: `keyword`, `suggest`, `lang`, `main_intent`, `competition_level` (Texte), `search_volume` (Ganzzahl), `cpc` (Zahl) und `group_id` (Ganzzahl, `0` löst die Gruppe). Nur angege…
        """
        return self._platform.call("landingpages", "update_keyword", {**(params or {}), **kwargs})

    def delete_keyword(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Keyword löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/landingpages/delete_keyword``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``keyword_id`` (int, Pflicht): ID des zu löschenden Keywords als Ganzzahl. Pflichtangabe; das Keyword muss zu deinem Unternehmen gehören und wird unwiderruflich entfernt.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("landingpages", "delete_keyword", {**(params or {}), **kwargs}, confirmed=confirmed)

    def get_keyword_search_volume(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Suchvolumen ermitteln

        Recht am Schlüssel: ``lesen`` · ``POST /platform/landingpages/get_keyword_search_volume``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``keyword`` (str): Der Suchbegriff als Text. Wird verwendet, wenn `keyword_id` fehlt oder am gespeicherten Keyword kein Suchvolumen hinterlegt ist. Eines der beiden Felder ist erforderlich.
        - ``keyword_id`` (int): Alternativ zu `keyword`: ID eines gespeicherten Keywords deines Unternehmens. Ist dort ein Suchvolumen eingetragen, wird es ohne externe Abfrage zurückgegeben.
        - ``location`` (str): Region der Abfrage. `germany` (Standard) fragt Deutschland ab, `dubai` oder `uae` die Vereinigten Arabischen Emirate; jeder andere Wert führt beide Abfragen zusammen.
        """
        return self._platform.call("landingpages", "get_keyword_search_volume", {**(params or {}), **kwargs})

    def get_keyword_cpc(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Klickpreis (CPC) ermitteln

        Recht am Schlüssel: ``lesen`` · ``POST /platform/landingpages/get_keyword_cpc``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``keyword`` (str): Der Suchbegriff als Text. Wird verwendet, wenn `keyword_id` fehlt oder am gespeicherten Keyword kein CPC hinterlegt ist. Eines der beiden Felder ist erforderlich.
        - ``keyword_id`` (int): Alternativ zu `keyword`: ID eines gespeicherten Keywords deines Unternehmens. Ist dort ein CPC eingetragen, wird er ohne externe Abfrage zurückgegeben.
        - ``location`` (str): Region der Abfrage. `germany` (Standard) fragt Deutschland ab, `dubai` oder `uae` die Vereinigten Arabischen Emirate; jeder andere Wert führt beide Abfragen zusammen.
        """
        return self._platform.call("landingpages", "get_keyword_cpc", {**(params or {}), **kwargs})


class LandingcardsArea(_Area):
    """Landingcards — Der Bereich Landingcards verwaltet digitale Visitenkarten (Bio-Landingpages) für Mitglieder deines Unternehmens."""

    def get_landingcards(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Landingcards auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/landingcards/get_landingcards``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Optionaler Filter auf den Zustand der Karte: `active` zeigt nur eingeschaltete Karten, jeder andere Wert (z. B. `draft`) nur ausgeschaltete. Der Zustand wird am Mitglied geführt (Einschaltung der Landingcard). Mit Filte…
        - ``limit`` (int): Maximale Anzahl Karten je Antwort. Standard 25, Werte unter 1 werden auf 1 angehoben.
        - ``offset`` (int): Anzahl der Karten, die am Anfang übersprungen werden (Standard 0), für das Blättern zusammen mit `total`.
        """
        return self._platform.call("landingcards", "get_landingcards", {**(params or {}), **kwargs})

    def get_landingcard(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Landingcard abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/landingcards/get_landingcard``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int): ID des Landingcard-Templates als Ganzzahl. Optional; ohne Angabe wird die Landingcard des Mitglieds verwendet, dem dein Schlüssel zugeordnet ist. Das Template muss zu deinem Unternehmen gehören.
        """
        return self._platform.call("landingcards", "get_landingcard", {**(params or {}), **kwargs})

    def create_landingcard(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Landingcard anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/landingcards/create_landingcard``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``profile`` (dict): Objekt mit Profildaten, die am Mitglied gespeichert werden. Erlaubte Schlüssel (alle Texte): `title` (Berufsbezeichnung), `phone`, `mobile`, `bio`, `linkedin`, `twitter`, `facebook`, `instagram`, `xing`, `tiktok`, `webs…
        - ``template`` (dict): Objekt mit Gestaltungs- und Textfeldern des Landingcard-Templates. Erlaubte Schlüssel: `bio_value_proposition`, `bio_tagline`, `bio_availability_status`, `bio_contact_priority` (im Datenmodell `WhatsApp`, `E-Mail` oder…
        """
        return self._platform.call("landingcards", "create_landingcard", {**(params or {}), **kwargs})

    def update_landingcard(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Landingcard ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/landingcards/update_landingcard``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int): ID des Landingcard-Templates als Ganzzahl. Optional; ohne Angabe wird die Landingcard des Mitglieds verwendet, dem dein Schlüssel zugeordnet ist. Das Template muss zu deinem Unternehmen gehören.
        - ``profile`` (dict): Objekt mit Profildaten, die am Mitglied gespeichert werden. Erlaubte Schlüssel (alle Texte): `title` (Berufsbezeichnung), `phone`, `mobile`, `bio`, `linkedin`, `twitter`, `facebook`, `instagram`, `xing`, `tiktok`, `webs…
        - ``template`` (dict): Objekt mit Gestaltungs- und Textfeldern des Landingcard-Templates. Erlaubte Schlüssel: `bio_value_proposition`, `bio_tagline`, `bio_availability_status`, `bio_contact_priority` (im Datenmodell `WhatsApp`, `E-Mail` oder…
        """
        return self._platform.call("landingcards", "update_landingcard", {**(params or {}), **kwargs})

    def delete_landingcard(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Landingcard deaktivieren oder löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/landingcards/delete_landingcard``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int): ID des Landingcard-Templates als Ganzzahl. Optional; ohne Angabe wird die Landingcard des Mitglieds verwendet, dem dein Schlüssel zugeordnet ist. Das Template muss zu deinem Unternehmen gehören.
        - ``remove_template`` (bool): Wahrheitswert. Bei `true` wird das Landingcard-Template endgültig gelöscht; bei `false` oder ohne Angabe (Standard) bleibt es erhalten und soll archiviert werden.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("landingcards", "delete_landingcard", {**(params or {}), **kwargs}, confirmed=confirmed)

    def activate_landingcard(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Landingcard aktivieren

        Recht am Schlüssel: ``veroeffentlichen`` · ``POST /platform/landingcards/activate_landingcard``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int): ID des Landingcard-Templates als Ganzzahl. Optional; ohne Angabe wird das Template des Mitglieds verwendet, dem dein Schlüssel zugeordnet ist. Das Template muss zu deinem Unternehmen gehören.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("landingcards", "activate_landingcard", {**(params or {}), **kwargs}, confirmed=confirmed)

    def deactivate_landingcard(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Landingcard deaktivieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/landingcards/deactivate_landingcard``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int): ID des Landingcard-Templates als Ganzzahl. Optional; ohne Angabe wird das Template des Mitglieds verwendet, dem dein Schlüssel zugeordnet ist. Das Template muss zu deinem Unternehmen gehören.
        """
        return self._platform.call("landingcards", "deactivate_landingcard", {**(params or {}), **kwargs})

    def get_landingcard_analytics(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Landingcard-Kennzahlen abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/landingcards/get_landingcard_analytics``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int): ID des Landingcard-Templates als Ganzzahl. Optional; ohne Angabe wird die Landingcard des Mitglieds verwendet, dem dein Schlüssel zugeordnet ist. Das Template muss zu deinem Unternehmen gehören.
        """
        return self._platform.call("landingcards", "get_landingcard_analytics", {**(params or {}), **kwargs})

    def bulk_create_landingcards(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Landingcards für mehrere Mitglieder aktivieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/landingcards/bulk_create_landingcards``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``member_ids`` (list, Pflicht): Liste der Mitglieds-IDs (Ganzzahlen) aus deinem Unternehmen, für die die Landingcard eingeschaltet wird. Pflichtangabe, darf nicht leer sein. Es gibt keine Obergrenze; große Listen dauern entsprechend länger, da je Mitg…
        """
        return self._platform.call("landingcards", "bulk_create_landingcards", {**(params or {}), **kwargs})

    def regenerate_landingcard_qrcode(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """QR-Code neu erzeugen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/landingcards/regenerate_landingcard_qrcode``
        """
        return self._platform.call("landingcards", "regenerate_landingcard_qrcode", {**(params or {}), **kwargs})


class QrcodesArea(_Area):
    """QR-Codes — Mit diesem Bereich verwaltest du die QR-Codes deines Unternehmens."""

    def get_qrcodes(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """QR-Codes auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/qrcodes/get_qrcodes``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Optionaler Filter auf den Aktivstatus. Erlaubt sind `active` (nur aktive Codes) und `inactive` (nur deaktivierte); Groß-/Kleinschreibung spielt keine Rolle. Jeder andere Wert wird still ignoriert und liefert alle Codes.
        - ``limit`` (int): Maximale Anzahl Einträge pro Antwort als ganze Zahl. Standard ist 25, der kleinste Wert ist 1. Es gibt keine feste Obergrenze; sehr große Werte machen die Antwort aber entsprechend groß.
        - ``offset`` (int): Anzahl der Einträge, die am Anfang der sortierten Liste übersprungen werden, für das seitenweise Blättern. Standard ist 0, negative Werte werden zu 0.
        """
        return self._platform.call("qrcodes", "get_qrcodes", {**(params or {}), **kwargs})

    def get_qrcode(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """QR-Code abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/qrcodes/get_qrcode``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``qrcode_id`` (int, Pflicht): Die numerische ID des QR-Codes, wie sie in `id` von `get_qrcodes` oder `create_qrcode` zurückkommt. Pflichtangabe. Codes anderer Firmen werden wie nicht vorhanden behandelt.
        """
        return self._platform.call("qrcodes", "get_qrcode", {**(params or {}), **kwargs})

    def create_qrcode(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """QR-Code anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/qrcodes/create_qrcode``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``name`` (str, Pflicht): Frei wählbarer Name des QR-Codes, zum Beispiel der Einsatzzweck. Pflichtangabe, darf nicht leer sein. Der Wert wird getrimmt und HTML-maskiert gespeichert.
        - ``target`` (str, Pflicht): Ziel-URL, zu der der QR-Code weiterleitet, zum Beispiel `https://www.example.com/angebot`. Pflichtangabe. Aus dieser Adresse werden beim Anlegen Seitentitel und Beschreibung gelesen. Es findet keine URL-Formatprüfung st…
        - ``document_id`` (int): Optional: ID eines Dokuments, mit dem der QR-Code verknüpft wird, als ganze Zahl. Ohne Angabe wird `0` (kein Dokument) gespeichert; in der Antwort steht der Wert als Zeichenkette.
        - ``is_active`` (bool): Optional: `true` (Standard) legt den Code aktiv an, `false` legt ihn deaktiviert an. Ein deaktivierter Code bleibt gespeichert und kann mit `update_qrcode` wieder aktiviert werden.
        """
        return self._platform.call("qrcodes", "create_qrcode", {**(params or {}), **kwargs})

    def update_qrcode(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """QR-Code ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/qrcodes/update_qrcode``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``qrcode_id`` (int, Pflicht): Die ID des zu ändernden QR-Codes, wie sie `get_qrcodes` oder `create_qrcode` liefert. Pflichtangabe; Codes anderer Firmen werden abgelehnt.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern. Wirksame Schlüssel: `name` (Text), `target` (Ziel-URL als Text) und `is_active` (true/false). Pflichtangabe; ein leeres Objekt ändert nichts. Alle anderen Schlüssel werden ignoriert.
        """
        return self._platform.call("qrcodes", "update_qrcode", {**(params or {}), **kwargs})

    def delete_qrcode(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """QR-Code löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/qrcodes/delete_qrcode``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``qrcode_id`` (int, Pflicht): Die ID des zu löschenden QR-Codes. Pflichtangabe. Der Code muss zu deiner Firma gehören, sonst kommt die Fehlermeldung „QR-Code nicht gefunden oder kein Zugriff“.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("qrcodes", "delete_qrcode", {**(params or {}), **kwargs}, confirmed=confirmed)

    def copy_qrcode(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """QR-Code kopieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/qrcodes/copy_qrcode``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``qrcode_id`` (int, Pflicht): Die ID des QR-Codes, der kopiert werden soll. Pflichtangabe; der Code muss zu deiner Firma gehören.
        - ``name`` (str): Optional: Name der Kopie. Ohne Angabe wird der Originalname mit dem Zusatz „ (Kopie)“ verwendet. Der Wert wird getrimmt und HTML-maskiert gespeichert.
        - ``is_active`` (bool): Optional: Aktivstatus der Kopie (`true` oder `false`). Ohne Angabe übernimmt die Kopie den Status des Originals.
        """
        return self._platform.call("qrcodes", "copy_qrcode", {**(params or {}), **kwargs})

    def get_qrcode_analytics(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """QR-Code-Analytics abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/qrcodes/get_qrcode_analytics``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``qrcode_id`` (int, Pflicht): Die ID des QR-Codes, für den die Kennzahlen geliefert werden sollen. Pflichtangabe; der Code muss zu deiner Firma gehören.
        """
        return self._platform.call("qrcodes", "get_qrcode_analytics", {**(params or {}), **kwargs})

    def get_qrcode_stats(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """QR-Code-Statistik abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/qrcodes/get_qrcode_stats``
        """
        return self._platform.call("qrcodes", "get_qrcode_stats", {**(params or {}), **kwargs})

    def get_qrcode_scans(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Scan-Historie abrufen (Platzhalter)

        Recht am Schlüssel: ``lesen`` · ``POST /platform/qrcodes/get_qrcode_scans``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``qrcode_id`` (int, Pflicht): Die ID des QR-Codes, dessen Scan-Historie abgefragt wird. Pflichtangabe; der Code muss zu deiner Firma gehören, sonst kommt eine Fehlermeldung.
        """
        return self._platform.call("qrcodes", "get_qrcode_scans", {**(params or {}), **kwargs})

    def get_qr_image(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """QR-Code-Bild abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/qrcodes/get_qr_image``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``qrcode_id`` (int, Pflicht): Die ID des QR-Codes, dessen Bild geliefert werden soll. Pflichtangabe; der Code muss zu deiner Firma gehören, sonst kommt „QR-Code nicht gefunden oder kein Zugriff“.
        """
        return self._platform.call("qrcodes", "get_qr_image", {**(params or {}), **kwargs})


class TestimonialsArea(_Area):
    """Kundenstimmen — Dieser Bereich verwaltet die Kundenstimmen (Testimonials) deines Unternehmens."""

    def get_testimonials(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kundenstimmen auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/testimonials/get_testimonials``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``min_rating`` (int): Optional: Mindestbewertung als ganze Zahl. Es werden nur Testimonials mit `rating` größer oder gleich diesem Wert geliefert. Sinnvoll sind Werte von 1 bis 5; 0 oder keine Angabe schaltet den Filter aus.
        - ``limit`` (int): Maximale Anzahl Einträge pro Antwort als ganze Zahl. Standard ist 25, der kleinste Wert ist 1. Es gibt keine feste Obergrenze.
        - ``offset`` (int): Anzahl der Einträge, die am Anfang der sortierten Liste übersprungen werden, zum seitenweisen Blättern. Standard ist 0, negative Werte werden zu 0.
        """
        return self._platform.call("testimonials", "get_testimonials", {**(params or {}), **kwargs})

    def get_testimonial(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kundenstimme abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/testimonials/get_testimonial``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``testimonial_id`` (int, Pflicht): Die numerische ID des Testimonials, wie sie in `id` von `get_testimonials` oder `create_testimonial` zurückkommt. Pflichtangabe. Einträge anderer Firmen werden wie nicht vorhanden behandelt.
        """
        return self._platform.call("testimonials", "get_testimonial", {**(params or {}), **kwargs})

    def create_testimonial(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kundenstimme anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/testimonials/create_testimonial``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``data`` (dict, Pflicht): Objekt mit den Inhalten der Kundenstimme. Wirksame Schlüssel: `name`, `company`, `city`, `ceo`, `position`, `quote`, `problem`, `solution`, `future`, `image1desc`, `image2desc` (alle Text), `rating` (ganze Zahl, üblich…
        """
        return self._platform.call("testimonials", "create_testimonial", {**(params or {}), **kwargs})

    def update_testimonial(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kundenstimme ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/testimonials/update_testimonial``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``testimonial_id`` (int, Pflicht): Die ID des zu ändernden Testimonials, wie sie `get_testimonials` oder `create_testimonial` liefert. Pflichtangabe; Einträge anderer Firmen werden abgelehnt.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern. Wirksame Schlüssel: `name`, `company`, `city`, `ceo`, `position`, `quote`, `problem`, `solution`, `future`, `image1desc`, `image2desc`, `rating` (ganze Zahl), `variante` und `state`.…
        """
        return self._platform.call("testimonials", "update_testimonial", {**(params or {}), **kwargs})

    def delete_testimonial(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Kundenstimme löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/testimonials/delete_testimonial``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``testimonial_id`` (int, Pflicht): Die ID des zu löschenden Testimonials. Pflichtangabe. Der Eintrag muss zu deiner Firma gehören, sonst kommt die Fehlermeldung „Testimonial nicht gefunden oder kein Zugriff“.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("testimonials", "delete_testimonial", {**(params or {}), **kwargs}, confirmed=confirmed)

    def scrape_testimonials_from_url(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kundenstimmen aus Webseite importieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/testimonials/scrape_testimonials_from_url``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``url`` (str, Pflicht): Vollständige Adresse der Webseite mit den Kundenstimmen, zum Beispiel `https://www.example.com/referenzen`. Pflichtangabe. Die Adresse muss ein gültiges URL-Format haben und öffentlich abrufbar sein.
        """
        return self._platform.call("testimonials", "scrape_testimonials_from_url", {**(params or {}), **kwargs})

    def filter_by_rating(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kundenstimmen nach Bewertung filtern

        Recht am Schlüssel: ``lesen`` · ``POST /platform/testimonials/filter_by_rating``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``min_rating`` (int, Pflicht): Mindestbewertung als ganze Zahl (sinnvoll 1 bis 5). Pflichtangabe; mit 0 werden alle Stimmen geliefert. Geliefert werden alle Stimmen mit `rating` größer oder gleich diesem Wert.
        """
        return self._platform.call("testimonials", "filter_by_rating", {**(params or {}), **kwargs})

    def get_testimonial_statistics(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kennzahlen der Kundenstimmen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/testimonials/get_testimonial_statistics``
        """
        return self._platform.call("testimonials", "get_testimonial_statistics", {**(params or {}), **kwargs})

    def export_testimonials(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kundenstimmen als JSON exportieren

        Recht am Schlüssel: ``lesen`` · ``POST /platform/testimonials/export_testimonials``
        """
        return self._platform.call("testimonials", "export_testimonials", {**(params or {}), **kwargs})


class OffersArea(_Area):
    """Angebote im Katalog — Dieser Bereich verwaltet die Angebote im Katalog deines Unternehmens, also die Leistungen und Pakete, die du anbietest (nicht die Angebotsbelege der Buchhaltung)."""

    def get_offers(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Angebote auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/offers/get_offers``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``state`` (str): Optionaler Status-Filter als Text, zum Beispiel `present`. Es werden nur Angebote mit genau diesem Status geliefert (Groß-/Kleinschreibung nach Datenbank-Vergleich). Die bekannten Werte liefert `list_offer_states`.
        - ``search`` (str): Optionaler Suchtext. Es werden Angebote geliefert, in deren Titel oder Inhalt der Text als Teilzeichenfolge vorkommt. Der Suchtext wird getrimmt und HTML-maskiert, Sonderzeichen wie `&` oder Anführungszeichen können des…
        - ``interview_id`` (int): Optional: ID eines Interviews als ganze Zahl. Es werden nur Angebote geliefert, die diesem Interview zugeordnet sind.
        - ``limit`` (int): Maximale Anzahl Einträge pro Antwort als ganze Zahl. Standard ist 25, der kleinste Wert ist 1. Es gibt keine feste Obergrenze.
        - ``offset`` (int): Anzahl der Einträge, die am Anfang der sortierten Liste übersprungen werden, zum seitenweisen Blättern. Standard ist 0, negative Werte werden zu 0.
        """
        return self._platform.call("offers", "get_offers", {**(params or {}), **kwargs})

    def get_offer(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Angebot abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/offers/get_offer``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``offer_id`` (int, Pflicht): Die numerische ID des Angebots, wie sie in `id` von `get_offers` oder `create_offer` zurückkommt. Pflichtangabe. Angebote anderer Firmen werden wie nicht vorhanden behandelt.
        """
        return self._platform.call("offers", "get_offer", {**(params or {}), **kwargs})

    def create_offer(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Angebot anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/offers/create_offer``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``title`` (str, Pflicht): Titel des Angebots. Pflichtangabe, darf nicht leer sein. Der Wert wird getrimmt und HTML-maskiert gespeichert und dient auch als Grundlage für den internen Schlüssel.
        - ``content`` (dict): Optional: Inhalt als JSON-Objekt, zum Beispiel mit den Schlüsseln `title`, `description`, `price`, `needs`, `targetAudience` und `processSteps` (Liste), die `summarize_offer` auswertet. Weitere Schlüssel sind erlaubt un…
        - ``state`` (str): Optional: Status des Angebots als Text, zum Beispiel `present` (aktuell) oder `future` (geplant). Standard ist `present`. Die bekannten Werte nennt `list_offer_states`; eine Prüfung findet nicht statt.
        - ``interview_id`` (int): Optional: ID eines Interviews, mit dem das Angebot verknüpft wird, als ganze Zahl. Ohne Angabe bleibt das Feld leer.
        """
        return self._platform.call("offers", "create_offer", {**(params or {}), **kwargs})

    def update_offer(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Angebot ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/offers/update_offer``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``offer_id`` (int, Pflicht): Die ID des zu ändernden Angebots, wie sie `get_offers` oder `create_offer` liefert. Pflichtangabe; Angebote anderer Firmen werden abgelehnt.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern. Wirksame Schlüssel: `title` (Text), `state` (Text), `interview_id` (ganze Zahl) und `content` (JSON-Objekt oder Text, ersetzt den gesamten Inhalt). Pflichtangabe und nicht leer; unbe…
        """
        return self._platform.call("offers", "update_offer", {**(params or {}), **kwargs})

    def delete_offer(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Angebot löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/offers/delete_offer``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``offer_id`` (int, Pflicht): Die ID des zu löschenden Angebots. Pflichtangabe. Das Angebot muss zu deiner Firma gehören, sonst kommt die Fehlermeldung „Angebot nicht gefunden oder kein Zugriff“.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("offers", "delete_offer", {**(params or {}), **kwargs}, confirmed=confirmed)

    def copy_offer(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Angebot kopieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/offers/copy_offer``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``offer_id`` (int, Pflicht): Die ID des Quell-Angebots, das kopiert werden soll. Pflichtangabe; das Angebot muss zu deiner Firma gehören.
        - ``title`` (str): Optional: Titel der Kopie. Ohne Angabe wird der Originaltitel mit dem Zusatz „ (Kopie)“ verwendet. Der Wert wird getrimmt und HTML-maskiert gespeichert.
        - ``state`` (str): Optional: Status der Kopie als Text, zum Beispiel `draft` oder `future`. Ohne Angabe wird der Status des Originals übernommen.
        """
        return self._platform.call("offers", "copy_offer", {**(params or {}), **kwargs})

    def summarize_offer(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Angebot zusammenfassen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/offers/summarize_offer``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``offer_id`` (int, Pflicht): Die ID des Angebots, das zusammengefasst werden soll. Pflichtangabe; das Angebot muss zu deiner Firma gehören, sonst kommt eine Fehlermeldung.
        """
        return self._platform.call("offers", "summarize_offer", {**(params or {}), **kwargs})

    def list_offer_states(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Bekannte Angebotsstatus auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/offers/list_offer_states``
        """
        return self._platform.call("offers", "list_offer_states", {**(params or {}), **kwargs})


class ExpertiseArea(_Area):
    """Expertise — Dieser Bereich verwaltet die Expertise-Einträge deines Unternehmens: strukturiertes Fachwissen, das du zum Beispiel aus Interviews gewinnst."""

    def get_expertises(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Expertise-Einträge auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/expertise/get_expertises``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``state`` (str): Optionaler Status-Filter als Text, zum Beispiel `active`. Es werden nur Einträge mit genau diesem Status geliefert. Die bekannten Werte liefert `list_expertise_states`.
        - ``search`` (str): Optionaler Suchtext. Es werden Einträge geliefert, in deren Titel oder Inhalt der Text als Teilzeichenfolge vorkommt. Der Suchtext wird getrimmt und HTML-maskiert, Sonderzeichen wie `&` oder Anführungszeichen können des…
        - ``interview_id`` (int): Optional: ID eines Interviews als ganze Zahl. Es werden nur Einträge geliefert, die diesem Interview zugeordnet sind.
        - ``limit`` (int): Maximale Anzahl Einträge pro Antwort als ganze Zahl. Standard ist 25, der kleinste Wert ist 1. Es gibt keine feste Obergrenze.
        - ``offset`` (int): Anzahl der Einträge, die am Anfang der sortierten Liste übersprungen werden, zum seitenweisen Blättern. Standard ist 0, negative Werte werden zu 0.
        """
        return self._platform.call("expertise", "get_expertises", {**(params or {}), **kwargs})

    def get_expertise(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Expertise-Eintrag abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/expertise/get_expertise``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``expertise_id`` (int, Pflicht): Die numerische ID des Expertise-Eintrags, wie sie in `id` von `get_expertises` oder `create_expertise` zurückkommt. Pflichtangabe. Einträge anderer Firmen werden wie nicht vorhanden behandelt.
        """
        return self._platform.call("expertise", "get_expertise", {**(params or {}), **kwargs})

    def create_expertise(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Expertise-Eintrag anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/expertise/create_expertise``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``title`` (str, Pflicht): Titel des Expertise-Eintrags. Pflichtangabe, darf nicht leer sein. Der Wert wird getrimmt und HTML-maskiert gespeichert und dient auch als Grundlage für den internen Schlüssel.
        - ``content`` (dict): Optional: Inhalt als JSON-Objekt, zum Beispiel mit den Schlüsseln `title`, `initial_expertise_identification`, `process_analysis`, `experience_and_learning_curve` und `recommendations_and_methods`, die `summarize_expert…
        - ``state`` (str): Optional: Status des Eintrags als Text, zum Beispiel `active` oder `draft`. Standard ist `active`. Die bekannten Werte nennt `list_expertise_states`; eine Prüfung findet nicht statt.
        - ``interview_id`` (int): Optional: ID eines Interviews, aus dem der Eintrag stammt, als ganze Zahl. Ohne Angabe bleibt das Feld leer.
        """
        return self._platform.call("expertise", "create_expertise", {**(params or {}), **kwargs})

    def update_expertise(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Expertise-Eintrag ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/expertise/update_expertise``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``expertise_id`` (int, Pflicht): Die ID des zu ändernden Eintrags, wie sie `get_expertises` oder `create_expertise` liefert. Pflichtangabe; Einträge anderer Firmen werden abgelehnt.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern. Wirksame Schlüssel: `title` (Text), `state` (Text), `interview_id` (ganze Zahl) und `content` (JSON-Objekt oder Text, ersetzt den gesamten Inhalt). Pflichtangabe und nicht leer; unbe…
        """
        return self._platform.call("expertise", "update_expertise", {**(params or {}), **kwargs})

    def delete_expertise(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Expertise-Eintrag löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/expertise/delete_expertise``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``expertise_id`` (int, Pflicht): Die ID des zu löschenden Expertise-Eintrags. Pflichtangabe. Der Eintrag muss zu deiner Firma gehören, sonst kommt die Fehlermeldung „Expertise nicht gefunden oder kein Zugriff“.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("expertise", "delete_expertise", {**(params or {}), **kwargs}, confirmed=confirmed)

    def copy_expertise(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Expertise-Eintrag kopieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/expertise/copy_expertise``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``expertise_id`` (int, Pflicht): Die ID des Eintrags, der kopiert werden soll. Pflichtangabe; der Eintrag muss zu deiner Firma gehören.
        - ``title`` (str): Optional: Titel der Kopie. Ohne Angabe wird der Originaltitel mit dem Zusatz „ (Kopie)“ verwendet. Der Wert wird getrimmt und HTML-maskiert gespeichert.
        - ``state`` (str): Optional: Status der Kopie als Text, zum Beispiel `draft`. Ohne Angabe wird der Status des Originals übernommen.
        """
        return self._platform.call("expertise", "copy_expertise", {**(params or {}), **kwargs})

    def summarize_expertise(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Expertise-Eintrag zusammenfassen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/expertise/summarize_expertise``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``expertise_id`` (int, Pflicht): Die ID des Expertise-Eintrags, der zusammengefasst werden soll. Pflichtangabe; der Eintrag muss zu deiner Firma gehören, sonst kommt eine Fehlermeldung.
        """
        return self._platform.call("expertise", "summarize_expertise", {**(params or {}), **kwargs})

    def list_expertise_states(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Bekannte Expertise-Status auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/expertise/list_expertise_states``
        """
        return self._platform.call("expertise", "list_expertise_states", {**(params or {}), **kwargs})


class GlossaryArea(_Area):
    """Glossar — Dieser Bereich verwaltet das Glossar deines Unternehmens: Fachbegriffe mit Definition, zweisprachig in Deutsch und Englisch."""

    def get_glossary_entries(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Glossar-Einträge auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/glossary/get_glossary_entries``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``search`` (str): Optionaler Suchtext. Es werden Einträge geliefert, in deren deutschem oder englischem Begriff oder in deren Definition der Text als Teilzeichenfolge vorkommt. Der Suchtext wird getrimmt und HTML-maskiert.
        - ``category`` (str): Optionaler Filter auf die Kategorie als exakter Text. Im Datenmodell vorgesehen sind `Business`, `Technology`, `Legal` und `Marketing`; es werden nur Einträge mit genau diesem Wert geliefert.
        - ``status`` (str): Optionaler Filter auf den Status als exakter Text. Im Datenmodell vorgesehen sind `active`, `draft` und `archived`; es werden nur Einträge mit genau diesem Wert geliefert.
        - ``include_global`` (bool): Optional: `true` nimmt zusätzlich globale Begriffe ohne Firmenzuordnung in die Treffer auf. Standard ist `false`, dann kommen nur Einträge deiner Firma. Die Filter gelten auch für die globalen Begriffe.
        - ``limit`` (int): Maximale Anzahl Einträge pro Antwort als ganze Zahl. Standard ist 25, der kleinste Wert ist 1. Es gibt keine feste Obergrenze.
        - ``offset`` (int): Anzahl der Einträge, die am Anfang der sortierten Liste übersprungen werden, zum seitenweisen Blättern. Standard ist 0, negative Werte werden zu 0.
        """
        return self._platform.call("glossary", "get_glossary_entries", {**(params or {}), **kwargs})

    def get_glossary_entry(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Glossar-Eintrag abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/glossary/get_glossary_entry``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``entry_id`` (int, Pflicht): Die numerische ID des Glossar-Eintrags, wie sie in `id` von `get_glossary_entries` oder `create_glossary_entry` zurückkommt. Pflichtangabe.
        """
        return self._platform.call("glossary", "get_glossary_entry", {**(params or {}), **kwargs})

    def create_glossary_entry(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Glossar-Eintrag anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/glossary/create_glossary_entry``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``term_de`` (str, Pflicht): Deutscher Begriff, zum Beispiel „Lead-Qualifizierung“. Pflichtangabe, darf nicht leer sein. Aus ihm wird auch der interne Schlüssel des Eintrags gebildet.
        - ``definition_de`` (str, Pflicht): Deutsche Definition bzw. Erklärung des Begriffs als Text. Pflichtangabe, darf nicht leer sein. In der Kurzfassung von `summarize_glossary_entry` wird sie auf 160 Zeichen gekürzt.
        - ``term_en`` (str): Optional: englische Übersetzung des Begriffs. Ohne Angabe bleibt das Feld leer; die Suche in `get_glossary_entries` berücksichtigt es, sobald es gefüllt ist.
        - ``definition_en`` (str): Optional: englische Definition als Text. Ohne Angabe bleibt das Feld leer. Fehlt die deutsche Definition, nutzt die Kurzfassung ersatzweise diese.
        - ``category`` (str): Optional: Kategorie des Begriffs als Text. Im Datenmodell vorgesehen sind `Business`, `Technology`, `Legal` und `Marketing`; die Schreibweise muss für den Kategorie-Filter exakt passen.
        - ``status`` (str): Optional: Status des Eintrags als Text. Im Datenmodell vorgesehen sind `active`, `draft` und `archived`. Ohne Angabe bleibt der Status leer.
        - ``priority`` (str): Optional: Priorität als Text. Im Datenmodell vorgesehen sind `high`, `medium` und `low`. Ohne Angabe bleibt die Priorität leer.
        - ``synonyms_de`` (str): Optional: deutsche Synonyme als ein einzelner Text, zum Beispiel kommagetrennt („Anfragenbewertung, Lead-Check“). Es wird kein Listenformat erzwungen.
        - ``synonyms_en`` (str): Optional: englische Synonyme als ein einzelner Text, zum Beispiel kommagetrennt („lead scoring, lead vetting“). Es wird kein Listenformat erzwungen.
        """
        return self._platform.call("glossary", "create_glossary_entry", {**(params or {}), **kwargs})

    def update_glossary_entry(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Glossar-Eintrag ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/glossary/update_glossary_entry``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``entry_id`` (int, Pflicht): Die ID des zu ändernden Glossar-Eintrags, wie sie `get_glossary_entries` oder `create_glossary_entry` liefert. Pflichtangabe; Einträge anderer Firmen werden abgelehnt.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern. Wirksame Schlüssel (alle Text): `term_de`, `term_en`, `definition_de`, `definition_en`, `examples_de`, `examples_en`, `synonyms_de`, `synonyms_en`, `category`, `priority`, `status`.…
        """
        return self._platform.call("glossary", "update_glossary_entry", {**(params or {}), **kwargs})

    def delete_glossary_entry(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Glossar-Eintrag löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/glossary/delete_glossary_entry``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``entry_id`` (int, Pflicht): Die ID des zu löschenden Glossar-Eintrags. Pflichtangabe. Einträge anderer Firmen werden abgelehnt, unbekannte IDs liefern „Glossar-Eintrag nicht gefunden“.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("glossary", "delete_glossary_entry", {**(params or {}), **kwargs}, confirmed=confirmed)

    def summarize_glossary_entry(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Glossar-Eintrag zusammenfassen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/glossary/summarize_glossary_entry``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``entry_id`` (int, Pflicht): Die ID des Glossar-Eintrags, der zusammengefasst werden soll. Pflichtangabe; der Eintrag muss zu deiner Firma gehören, sonst kommt eine Fehlermeldung.
        """
        return self._platform.call("glossary", "summarize_glossary_entry", {**(params or {}), **kwargs})


class HandbookArea(_Area):
    """Handbuch — Das Betriebshandbuch besteht aus Handbuch-Seiten (SOPs, Richtlinien, Workflows, Schulungsunterlagen)."""

    def get_handbook_pages(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Handbuch-Seiten auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/handbook/get_handbook_pages``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Filtert auf genau diesen Status (Textvergleich, z. B. `draft`, `review`, `active`, `archived`). Ohne Angabe werden alle Status geliefert.
        - ``category`` (str): Filtert auf genau diese Kategorie, z. B. `02-sops`. Es wird nur exakt verglichen, keine Teilstrings.
        - ``page_type`` (str): Filtert auf den Seitentyp, z. B. `sop`, `workflow`, `training`, `documentation` oder `overview`. Exakter Vergleich.
        - ``search`` (str): Im Schema als Freitextsuche beschrieben, wird von dieser Funktion aber nicht ausgewertet und hat keine Wirkung. Nutze `search_handbook_pages` für die Suche in Titel, Slug, Inhalt und Tags.
        - ``include_global`` (bool): Wenn `true`, werden zusätzlich Seiten ohne Unternehmenszuordnung (globale Seiten) eingeschlossen. Standard `false`.
        - ``include_internal`` (bool): Steuert, ob systemweite Seiten (`is_internal: true`) mitgeliefert werden. Standard `true`; mit `false` erhältst du nur Seiten deines Unternehmens.
        - ``limit`` (int): Maximale Anzahl Einträge pro Antwort. Standard 25, Minimum 1; eine feste Obergrenze gibt es im Code nicht.
        - ``offset`` (int): Anzahl der zu überspringenden Einträge für die Seiteneinteilung. Standard 0, negative Werte werden zu 0.
        """
        return self._platform.call("handbook", "get_handbook_pages", {**(params or {}), **kwargs})

    def get_handbook_page(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Eine Handbuch-Seite abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/handbook/get_handbook_page``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``page_id`` (int, Pflicht): Numerische ID der Handbuch-Seite (Pflicht). Wird als Ganzzahl interpretiert; IDs fremder Unternehmen führen zu einem Zugriffsfehler.
        """
        return self._platform.call("handbook", "get_handbook_page", {**(params or {}), **kwargs})

    def search_handbook_pages(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Handbuch per Stichwort durchsuchen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/handbook/search_handbook_pages``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``query`` (str, Pflicht): Suchbegriff (Pflicht). Wird in Titel, Slug, Inhalt und Tags als Teilstring gesucht, ohne Berücksichtigung von Wortgrenzen.
        - ``limit`` (int): Maximale Trefferzahl pro Antwort. Standard 10, Minimum 1.
        - ``offset`` (int): Anzahl zu überspringender Treffer für die Seiteneinteilung. Standard 0.
        - ``category`` (str): Optionaler Filter auf eine exakte Kategorie, z. B. `02-sops`.
        - ``status`` (str): Optionaler Filter auf einen exakten Status, z. B. `active`.
        - ``include_internal`` (bool): Wenn `false`, werden systemweite Seiten (`is_internal`) ausgeschlossen. Standard `true`.
        """
        return self._platform.call("handbook", "search_handbook_pages", {**(params or {}), **kwargs})

    def semantic_search_handbook(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Handbuch semantisch durchsuchen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/handbook/semantic_search_handbook``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``query`` (str, Pflicht): Natürlichsprachige Suchanfrage (Pflicht), z. B. eine Frage oder ein Thema. Muss kein Stichwort enthalten, das wörtlich im Text steht.
        - ``limit`` (int): Anzahl der gewünschten Treffer. Standard 5, Minimum 1.
        - ``category`` (str): Optionaler Filter: nur Seiten dieser exakten Kategorie bleiben im Ergebnis.
        - ``page_type`` (str): Optionaler Filter auf den Seitentyp, z. B. `sop` oder `training`.
        - ``include_internal`` (bool): Wenn `false`, werden systemweite Seiten ausgeschlossen, die nicht deinem Unternehmen gehören. Standard `true`.
        """
        return self._platform.call("handbook", "semantic_search_handbook", {**(params or {}), **kwargs})

    def get_internal_handbook_pages(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Systemweite Handbuch-Seiten auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/handbook/get_internal_handbook_pages``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``category`` (str): Optionaler Filter auf eine exakte Kategorie, z. B. `02-sops`.
        - ``status`` (str): Optionaler Filter auf einen exakten Status, z. B. `active`.
        - ``page_type`` (str): Optionaler Filter auf den Seitentyp, z. B. `sop` oder `workflow`.
        - ``limit`` (int): Maximale Anzahl Einträge pro Antwort. Standard 25, Minimum 1.
        - ``offset`` (int): Anzahl der zu überspringenden Einträge. Standard 0.
        """
        return self._platform.call("handbook", "get_internal_handbook_pages", {**(params or {}), **kwargs})

    def create_handbook_page(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Handbuch-Seite anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/handbook/create_handbook_page``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``title`` (str, Pflicht): Titel der Seite (Pflicht, nicht leer).
        - ``slug`` (str): URL-tauglicher Bezeichner. Optional; wird sonst aus dem Titel erzeugt (nur Buchstaben und Ziffern, getrennt durch Bindestriche).
        - ``category`` (str): Kategorie der Seite als Freitext. Standard `02-sops`.
        - ``subcategory`` (str): Optionale Unterkategorie als Freitext, z. B. ein Abteilungsname.
        - ``page_type`` (str): Seitentyp. Das Datenmodell kennt `sop`, `workflow`, `training`, `documentation` und `overview`; Standard `sop`. Der Code prüft den Wert nicht gegen diese Liste.
        - ``status`` (str): Status der Seite. Das Datenmodell kennt `draft`, `review`, `active` und `archived`; Standard `draft`. Ein Abgleich mit dieser Liste findet nicht statt.
        - ``content`` (str): Hauptinhalt der Seite als Text, üblicherweise Markdown. Wird unverändert gespeichert.
        - ``goal`` (str): Kurze Zielbeschreibung der Seite bzw. des Prozesses.
        - ``steps`` (list): Liste von Prozessschritten, jeweils ein Objekt mit frei wählbaren Feldern (z. B. `title`, `description`). Wird als JSON gespeichert.
        - ``checklist`` (list): Checkliste als Liste von Objekten (z. B. `item`). Wird als JSON gespeichert.
        - ``kpis`` (list): Kennzahlen als Liste von Objekten (z. B. `name`, `target`). Wird als JSON gespeichert.
        - ``tags`` (list): Liste von Schlagwörtern als Strings. Die Tags werden bei der Stichwortsuche mit durchsucht.
        - ``responsible`` (str): Name der verantwortlichen Person als Freitext.
        - ``author`` (str): Name des Autors als Freitext.
        - ``access_level`` (str): Zugriffsstufe der Seite. Das Datenmodell kennt `admin`, `employee`, `partner`, `ai` und `public`. Die Funktion prüft den Wert nicht.
        - ``is_internal`` (bool): Markiert die Seite als systemweit sichtbare SOP. Standard `false`; bei `true` erscheint die Seite auch in den Listen anderer Unternehmen.
        - ``auto_index`` (bool): Wenn `true`, wird die Seite nach dem Speichern direkt in den Suchindex aufgenommen. Nur wirksam, wenn der Index eingerichtet ist.
        """
        return self._platform.call("handbook", "create_handbook_page", {**(params or {}), **kwargs})

    def update_handbook_page(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Handbuch-Seite aktualisieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/handbook/update_handbook_page``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``page_id`` (int, Pflicht): Numerische ID der zu ändernden Seite (Pflicht).
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern in snake_case, z. B. `{"status": "active", "tags": ["sop"]}`. Muss mindestens einen Schlüssel enthalten; `null`-Werte werden übergangen.
        - ``reindex`` (bool): Wenn `true`, wird die Seite nach dem Speichern im Suchindex aktualisiert, damit `semantic_search_handbook` die Änderung findet. Standard `false`.
        """
        return self._platform.call("handbook", "update_handbook_page", {**(params or {}), **kwargs})

    def delete_handbook_page(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Handbuch-Seite löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/handbook/delete_handbook_page``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``page_id`` (int, Pflicht): Numerische ID der zu löschenden Seite (Pflicht).
        - ``remove_index`` (bool): Wenn `true`, wird der Eintrag der Seite zusätzlich aus dem Suchindex gelöscht, bevor die Seite entfällt. Standard `false`.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("handbook", "delete_handbook_page", {**(params or {}), **kwargs}, confirmed=confirmed)

    def copy_handbook_page(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Handbuch-Seite kopieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/handbook/copy_handbook_page``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``page_id`` (int, Pflicht): Numerische ID der Quellseite (Pflicht).
        - ``title`` (str): Neuer Titel für die Kopie. Ohne Angabe: Originaltitel plus ` (Kopie)`.
        - ``slug`` (str): Optionaler neuer Slug. Ohne Angabe wird er aus dem Titel der Kopie erzeugt.
        - ``status`` (str): Status der Kopie, Standard `draft`. Der Wert wird nicht gegen eine Liste geprüft.
        - ``auto_index`` (bool): Wenn `true`, wird die Kopie nach dem Speichern direkt in den Suchindex aufgenommen (nur wenn der Index eingerichtet ist).
        """
        return self._platform.call("handbook", "copy_handbook_page", {**(params or {}), **kwargs})

    def reindex_handbook_page(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Suchindex einer Seite pflegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/handbook/reindex_handbook_page``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``page_id`` (int, Pflicht): Numerische ID der Seite (Pflicht).
        - ``action`` (str): Index-Aktion: `index` (neu aufnehmen), `update` (erneuern, Standard) oder `delete` (aus dem Index entfernen).
        """
        return self._platform.call("handbook", "reindex_handbook_page", {**(params or {}), **kwargs})

    def summarize_handbook_page(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Handbuch-Seite zusammenfassen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/handbook/summarize_handbook_page``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``page_id`` (int, Pflicht): Numerische ID der Seite (Pflicht).
        - ``focus`` (str): Optionaler Schwerpunkt der Auswertung als Freitext, z. B. `onboarding`, `qa` oder `training`. Ohne Angabe wird `standard` verwendet.
        """
        return self._platform.call("handbook", "summarize_handbook_page", {**(params or {}), **kwargs})


class SpeechanalysisArea(_Area):
    """Sprachprofile — Ein Sprachprofil (Linguistic-Profil) beschreibt, wie eine Person spricht und kommuniziert: Wortschatz, Satzbau, Kommunikationsstil und limbischer Typ."""

    def get_speech_profiles(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Sprachprofile auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/speechanalysis/get_speech_profiles``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Optionaler Filter auf einen exakten Status-Text, z. B. `generated`. Ohne Angabe werden alle Status geliefert.
        - ``limit`` (int): Maximale Anzahl Profile pro Antwort. Standard 25, Minimum 1; eine feste Obergrenze gibt es im Code nicht.
        - ``offset`` (int): Anzahl der zu überspringenden Profile für die Seiteneinteilung. Standard 0, negative Werte werden zu 0.
        """
        return self._platform.call("speechanalysis", "get_speech_profiles", {**(params or {}), **kwargs})

    def get_speech_profile(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Ein Sprachprofil abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/speechanalysis/get_speech_profile``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``profile_id`` (int, Pflicht): Numerische ID des Sprachprofils (Pflicht). Die ID stammt aus `get_speech_profiles`.
        """
        return self._platform.call("speechanalysis", "get_speech_profile", {**(params or {}), **kwargs})

    def update_speech_profile(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Sprachprofil aktualisieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/speechanalysis/update_speech_profile``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``profile_id`` (int, Pflicht): Numerische ID des zu ändernden Profils (Pflicht).
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern: `name`, `status`, `lang` (Texte), `analysis` (Text) und `profile_data` (Objekt oder Text). Es muss mindestens ein Schlüssel enthalten sein.
        """
        return self._platform.call("speechanalysis", "update_speech_profile", {**(params or {}), **kwargs})

    def delete_speech_profile(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Sprachprofil löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/speechanalysis/delete_speech_profile``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``profile_id`` (int, Pflicht): Numerische ID des zu löschenden Profils (Pflicht).
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("speechanalysis", "delete_speech_profile", {**(params or {}), **kwargs}, confirmed=confirmed)

    def summarize_speech_profile(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Sprachprofil kurz zusammenfassen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/speechanalysis/summarize_speech_profile``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``profile_id`` (int, Pflicht): Numerische ID des Sprachprofils (Pflicht).
        """
        return self._platform.call("speechanalysis", "summarize_speech_profile", {**(params or {}), **kwargs})


class InterviewsArea(_Area):
    """Interviews — Der Bereich verwaltet Interviews und deren Vorlagen (Templates)."""

    def get_templates(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Interview-Vorlagen auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/interviews/get_templates``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``include_catalog`` (bool): Wenn `true` (Standard), werden zusätzlich die globalen Katalog-Vorlagen geliefert; bei `false` nur die Vorlagen deines Unternehmens.
        """
        return self._platform.call("interviews", "get_templates", {**(params or {}), **kwargs})

    def get_template(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Eine Interview-Vorlage abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/interviews/get_template``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int, Pflicht): Numerische ID der Vorlage (Pflicht), z. B. aus `get_templates`.
        """
        return self._platform.call("interviews", "get_template", {**(params or {}), **kwargs})

    def create_template(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Interview-Vorlage anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/interviews/create_template``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``data`` (dict, Pflicht): Objekt mit den Vorlagenfeldern: `name`, `status`, `interviewtype`, `userprompt`, `intro`, `outtro`, `interviewquestions` (Liste von Objekten mit `question`, `wanttoreach`, `prompt` oder JSON-Text), `locale`, `ispartner`…
        """
        return self._platform.call("interviews", "create_template", {**(params or {}), **kwargs})

    def update_template(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Interview-Vorlage ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/interviews/update_template``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int, Pflicht): Numerische ID der zu ändernden Vorlage (Pflicht).
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern (`name`, `status`, `interviewtype`, `userprompt`, `intro`, `outtro`, `interviewquestions`, `locale`, `ispartner`, `iscatalog`). `interviewquestions` ersetzt die gesamte Liste.
        """
        return self._platform.call("interviews", "update_template", {**(params or {}), **kwargs})

    def delete_template(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Interview-Vorlage löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/interviews/delete_template``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int, Pflicht): Numerische ID der zu löschenden Vorlage (Pflicht).
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("interviews", "delete_template", {**(params or {}), **kwargs}, confirmed=confirmed)

    def duplicate_template(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Interview-Vorlage duplizieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/interviews/duplicate_template``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int, Pflicht): Numerische ID der Quellvorlage (Pflicht).
        - ``name`` (str): Optionaler Name der Kopie. Ohne Angabe: Originalname plus ` (Kopie)`.
        """
        return self._platform.call("interviews", "duplicate_template", {**(params or {}), **kwargs})

    def export_template_as_json(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Interview-Vorlage exportieren

        Recht am Schlüssel: ``lesen`` · ``POST /platform/interviews/export_template_as_json``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int, Pflicht): Numerische ID der zu exportierenden Vorlage (Pflicht). Zugänglich sind eigene Vorlagen und solche ohne Unternehmenszuordnung.
        """
        return self._platform.call("interviews", "export_template_as_json", {**(params or {}), **kwargs})

    def import_template_from_json(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Interview-Vorlage importieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/interviews/import_template_from_json``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``data`` (dict, Pflicht): Objekt mit den Vorlagenfeldern (`name`, `status`, `interviewtype`, `userprompt`, `intro`, `outtro`, `interviewquestions`, `locale`, `ispartner`, `iscatalog`). Fragen sind eine Liste von Objekten mit `question`, `wanttor…
        """
        return self._platform.call("interviews", "import_template_from_json", {**(params or {}), **kwargs})

    def get_interviews(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Interviews auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/interviews/get_interviews``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Optionaler Filter auf einen exakten Status-Text. Neue Interviews haben den Status `new`; weitere Werte vergibst du selbst über `update_interview`.
        - ``limit`` (int): Maximale Anzahl Interviews pro Antwort. Standard 20, Minimum 1.
        - ``offset`` (int): Anzahl zu überspringender Interviews für die Seiteneinteilung. Standard 0.
        """
        return self._platform.call("interviews", "get_interviews", {**(params or {}), **kwargs})

    def get_interview(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Ein Interview abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/interviews/get_interview``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``interview_id`` (int, Pflicht): Numerische ID des Interviews (Pflicht), z. B. aus `get_interviews` oder `create_interview`.
        """
        return self._platform.call("interviews", "get_interview", {**(params or {}), **kwargs})

    def create_interview(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Interview anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/interviews/create_interview``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``name`` (str, Pflicht): Name des Interviews (Pflicht), z. B. ein Titel mit Gesprächspartner.
        - ``template_id`` (int): Optionale ID einer Vorlage. Typ und Fragen werden daraus übernommen. Muss zu deinem Unternehmen gehören oder global sein, sonst Fehler.
        - ``interview_person`` (str): Name des Gesprächspartners als Freitext.
        - ``locale`` (str): Sprachcode des Interviews, z. B. `de` oder `en`. Standard `de`.
        - ``status`` (str): Anfangsstatus als Freitext. Standard `new`.
        - ``lead_id`` (int): Optionale ID eines Leads, auf den sich das Interview bezieht. Es wird nicht geprüft, ob der Lead existiert.
        """
        return self._platform.call("interviews", "create_interview", {**(params or {}), **kwargs})

    def update_interview(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Interview aktualisieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/interviews/update_interview``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``interview_id`` (int, Pflicht): Numerische ID des zu ändernden Interviews (Pflicht).
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern: `name`, `status`, `interview_person`, `locale`, `template_id` (Ganzzahl), `transcript` (Text), `insights` (Text). Mindestens ein bekannter Schlüssel ist sinnvoll.
        """
        return self._platform.call("interviews", "update_interview", {**(params or {}), **kwargs})

    def delete_interview(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Interview löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/interviews/delete_interview``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``interview_id`` (int, Pflicht): Numerische ID des zu löschenden Interviews (Pflicht).
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("interviews", "delete_interview", {**(params or {}), **kwargs}, confirmed=confirmed)

    def get_interview_insights(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Insights und Qualitätswerte lesen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/interviews/get_interview_insights``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``interview_id`` (int, Pflicht): Numerische ID des Interviews (Pflicht). Es muss zu deinem Unternehmen gehören.
        """
        return self._platform.call("interviews", "get_interview_insights", {**(params or {}), **kwargs})


class AcademyArea(_Area):
    """Akademie — Der Bereich Academy verwaltet die Lerninhalte deiner Firma in drei Ebenen: Kurse enthalten Module, Module enthalten Lektionen."""

    def get_courses(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kurse auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/academy/get_courses``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Optionaler Statusfilter, exakte Übereinstimmung, z. B. `draft`. Leer oder weggelassen: alle Status. Welche Werte tatsächlich vorkommen, siehst du in den Kursen selbst; `list_course_statuses` liefert nur eine feste Beisp…
        - ``search`` (str): Optionaler Suchbegriff. Gefunden werden Kurse, deren Titel oder Beschreibung den Begriff enthalten (Teilstring, ohne Beachtung weiterer Felder). Leer oder weggelassen: keine Einschränkung.
        - ``limit`` (int): Maximale Anzahl Kurse pro Antwort, ganze Zahl. Standard 25, Mindestwert 1 (kleinere Werte werden auf 1 angehoben). Eine feste Obergrenze gibt es nicht.
        - ``offset`` (int): Anzahl Kurse, die übersprungen werden, ganze Zahl ab 0 (Standard 0, negative Werte werden zu 0). Zum Blättern setzt du `offset` auf das Vielfache von `limit`.
        """
        return self._platform.call("academy", "get_courses", {**(params or {}), **kwargs})

    def get_course(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kurs im Detail abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/academy/get_course``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``course_id`` (int, Pflicht): ID des Kurses (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_courses` oder aus der Antwort von `create_course`. Der Kurs muss zur Firma deines Schlüssels gehören, sonst antwortet die Funktion mit „Kurs nicht…
        """
        return self._platform.call("academy", "get_course", {**(params or {}), **kwargs})

    def create_course(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kurs anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/academy/create_course``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``title`` (str, Pflicht): Titel des Kurses (Pflicht, nicht leer). Wird getrimmt und HTML-maskiert gespeichert; aus dem Titel entsteht auch der interne Objektschlüssel.
        - ``status`` (str): Optionaler Kursstatus als Text, z. B. `draft`. Im Datenmodell sind `draft` und `publish` als Auswahlwerte vorgesehen. Weggelassen bleibt der Status leer.
        - ``lang`` (str): Optionale Sprache des Kurses als Text, z. B. `de` oder `en`. Es wird kein Format geprüft; der Wert wird so gespeichert (getrimmt, HTML-maskiert).
        - ``price`` (float): Optionaler Preis als Zahl, z. B. `490` oder `49.9`. Wird als Dezimalzahl übernommen; die Währung gibst du getrennt in `currency` an.
        - ``currency`` (str): Optionale Währung als Text, z. B. `EUR`. Es erfolgt keine Prüfung gegen eine Währungsliste.
        - ``is_free`` (bool): Optional `true`, wenn der Kurs kostenlos ist, sonst `false`. Wird nur gesetzt, wenn der Schlüssel im Körper vorhanden ist; weggelassen bleibt der Standard des Datenmodells.
        - ``content`` (dict): Optionales Objekt mit Inhaltsfeldern. Erkannt werden die Schlüssel `short_description`, `description`, `meta_description`, `learnings`, `target_audience`, `benefit`, `image_prompt` und `video_prompt` (jeweils Text, HTML…
        """
        return self._platform.call("academy", "create_course", {**(params or {}), **kwargs})

    def update_course(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kurs aktualisieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/academy/update_course``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``course_id`` (int, Pflicht): ID des Kurses (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_courses` oder aus der Antwort von `create_course`. Der Kurs muss zur Firma deines Schlüssels gehören, sonst antwortet die Funktion mit „Kurs nicht…
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern (Pflicht, nicht leer). Erkannt werden title, status, lang, coursetype, accessibility, price (Zahl), currency, is_free (boolean), duration (Text) sowie `content` als Unterobjekt mit sh…
        """
        return self._platform.call("academy", "update_course", {**(params or {}), **kwargs})

    def delete_course(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Kurs löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/academy/delete_course``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``course_id`` (int, Pflicht): ID des Kurses (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_courses` oder aus der Antwort von `create_course`. Der Kurs muss zur Firma deines Schlüssels gehören, sonst antwortet die Funktion mit „Kurs nicht…
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("academy", "delete_course", {**(params or {}), **kwargs}, confirmed=confirmed)

    def get_course_modules(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Module eines Kurses auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/academy/get_course_modules``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``course_id`` (int, Pflicht): ID des Kurses (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_courses` oder aus der Antwort von `create_course`. Der Kurs muss zur Firma deines Schlüssels gehören, sonst antwortet die Funktion mit „Kurs nicht…
        """
        return self._platform.call("academy", "get_course_modules", {**(params or {}), **kwargs})

    def get_module(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Modul im Detail abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/academy/get_module``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``module_id`` (int, Pflicht): ID des Moduls (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_course_modules` oder aus der Antwort von `create_module`. Zugriff besteht nur, wenn der zugehörige Kurs zur Firma deines Schlüssels gehört.
        """
        return self._platform.call("academy", "get_module", {**(params or {}), **kwargs})

    def create_module(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Modul anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/academy/create_module``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``course_id`` (int, Pflicht): ID des Kurses (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_courses` oder aus der Antwort von `create_course`. Der Kurs muss zur Firma deines Schlüssels gehören, sonst antwortet die Funktion mit „Kurs nicht…
        - ``title`` (str, Pflicht): Titel des Moduls (Pflicht, nicht leer). Wird getrimmt und HTML-maskiert gespeichert.
        - ``order`` (int): Optionale Position im Kurs als ganze Zahl, z. B. `1` für das erste Modul. Es wird nicht auf Doppelungen geprüft. Weggelassen bleibt die Position leer.
        - ``description`` (str): Optionale Beschreibung des Moduls als Text. Wird unverändert gespeichert (kein Maskieren).
        """
        return self._platform.call("academy", "create_module", {**(params or {}), **kwargs})

    def update_module(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Modul aktualisieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/academy/update_module``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``module_id`` (int, Pflicht): ID des Moduls (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_course_modules` oder aus der Antwort von `create_module`. Zugriff besteht nur, wenn der zugehörige Kurs zur Firma deines Schlüssels gehört.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern (Pflicht, nicht leer). Erkannt werden `title` (Text), `description` (Text) und `order` (ganze Zahl). Andere Schlüssel haben keine Wirkung.
        """
        return self._platform.call("academy", "update_module", {**(params or {}), **kwargs})

    def delete_module(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Modul löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/academy/delete_module``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``module_id`` (int, Pflicht): ID des Moduls (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_course_modules` oder aus der Antwort von `create_module`. Zugriff besteht nur, wenn der zugehörige Kurs zur Firma deines Schlüssels gehört.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("academy", "delete_module", {**(params or {}), **kwargs}, confirmed=confirmed)

    def get_module_lessons(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Lektionen eines Moduls auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/academy/get_module_lessons``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``module_id`` (int, Pflicht): ID des Moduls (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_course_modules` oder aus der Antwort von `create_module`. Zugriff besteht nur, wenn der zugehörige Kurs zur Firma deines Schlüssels gehört.
        """
        return self._platform.call("academy", "get_module_lessons", {**(params or {}), **kwargs})

    def create_lesson(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Lektion anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/academy/create_lesson``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``module_id`` (int, Pflicht): ID des Moduls (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_course_modules` oder aus der Antwort von `create_module`. Zugriff besteht nur, wenn der zugehörige Kurs zur Firma deines Schlüssels gehört.
        - ``title`` (str, Pflicht): Titel der Lektion (Pflicht, nicht leer). Wird getrimmt und HTML-maskiert gespeichert.
        - ``order`` (int): Optionale Position innerhalb des Moduls als ganze Zahl, z. B. `1`. Doppelte Positionen werden nicht geprüft. Weggelassen bleibt die Position leer.
        - ``description`` (str): Optionale Beschreibung der Lektion als Text. Wird unverändert gespeichert (kein Maskieren).
        - ``learnings`` (str): Optionale Lernziele der Lektion als Text (im Datenmodell ein Formatierungsfeld, HTML ist möglich). Wird unverändert gespeichert.
        """
        return self._platform.call("academy", "create_lesson", {**(params or {}), **kwargs})

    def update_lesson(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Lektion aktualisieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/academy/update_lesson``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``lesson_id`` (int, Pflicht): ID der Lektion (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_module_lessons` oder `get_module` (Feld lessons) bzw. aus der Antwort von `create_lesson`. Zugriff besteht nur, wenn Modul und Kurs zur Firma dein…
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern (Pflicht, nicht leer). Erkannt werden `title` (Text), `description` (Text), `order` (ganze Zahl) und `learnings` (Text). Andere Schlüssel haben keine Wirkung.
        """
        return self._platform.call("academy", "update_lesson", {**(params or {}), **kwargs})

    def delete_lesson(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Lektion löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/academy/delete_lesson``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``lesson_id`` (int, Pflicht): ID der Lektion (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_module_lessons` oder `get_module` (Feld lessons) bzw. aus der Antwort von `create_lesson`. Zugriff besteht nur, wenn Modul und Kurs zur Firma dein…
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("academy", "delete_lesson", {**(params or {}), **kwargs}, confirmed=confirmed)

    def summarize_course(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kurs zusammenfassen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/academy/summarize_course``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``course_id`` (int, Pflicht): ID des Kurses (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_courses` oder aus der Antwort von `create_course`. Der Kurs muss zur Firma deines Schlüssels gehören, sonst antwortet die Funktion mit „Kurs nicht…
        """
        return self._platform.call("academy", "summarize_course", {**(params or {}), **kwargs})

    def list_course_statuses(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Bekannte Kursstatus auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/academy/list_course_statuses``
        """
        return self._platform.call("academy", "list_course_statuses", {**(params or {}), **kwargs})


class CampaignsArea(_Area):
    """Werbekampagnen — Der Bereich Kampagnen verwaltet die Werbekampagnen deiner Firma."""

    def get_campaigns(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kampagnen auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/campaigns/get_campaigns``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Optionaler Filter auf den Aktivstatus: `active` (nur aktive) oder `inactive` (nur inaktive); Groß-/Kleinschreibung egal. Andere Werte und leer: kein Statusfilter.
        - ``provider`` (str): Optionaler Filter auf den Provider, exakte Übereinstimmung, z. B. `google`. Im Datenmodell sind google, facebook, instagram, tiktok, linkedin und x vorgesehen. Leer oder weggelassen: alle Provider.
        - ``limit`` (int): Maximale Anzahl Kampagnen pro Antwort, ganze Zahl. Standard 20, Mindestwert 1 (kleinere Werte werden auf 1 angehoben). Eine feste Obergrenze gibt es nicht.
        - ``offset`` (int): Anzahl Kampagnen, die übersprungen werden, ganze Zahl ab 0 (Standard 0, negative Werte werden zu 0). Zum Blättern setzt du `offset` auf das Vielfache von `limit`.
        """
        return self._platform.call("campaigns", "get_campaigns", {**(params or {}), **kwargs})

    def get_campaign(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kampagne im Detail abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/campaigns/get_campaign``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``campaign_id`` (int, Pflicht): ID der Kampagne (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_campaigns` oder aus der Antwort von `create_campaign`. Die Kampagne muss zur Firma deines Schlüssels gehören, sonst antwortet die Funktion mit „K…
        """
        return self._platform.call("campaigns", "get_campaign", {**(params or {}), **kwargs})

    def create_campaign(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kampagne manuell anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/campaigns/create_campaign``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``name`` (str, Pflicht): Name der Kampagne (Pflicht, nicht leer). Wird getrimmt und HTML-maskiert gespeichert.
        - ``provider`` (str): Optionaler Provider als Text, z. B. `google`. Standard `custom`. Im Datenmodell vorgesehen sind google, facebook, instagram, tiktok, linkedin und x; es wird nicht gegen diese Liste geprüft.
        - ``campaign_type`` (str): Optionaler Kampagnentyp als Text, z. B. `search`. Standard `custom`. Im Datenmodell vorgesehen sind image, video, lead, text und search; es wird nicht gegen diese Liste geprüft.
        - ``content`` (str): Optionaler Kampagneninhalt als Text (z. B. Anzeigentext oder JSON als Zeichenkette). Wird unverändert gespeichert. Standard: leere Zeichenkette.
        - ``keyword_id`` (int): Optionale ID eines Keyword-Objekts als ganze Zahl. Sie wird nur gespeichert; es erfolgt keine Prüfung, ob das Keyword existiert oder zu deiner Firma gehört.
        - ``template_id`` (int): Optionale ID einer Landingpage-Vorlage als ganze Zahl. Sie wird nur gespeichert, ohne Existenz- oder Zugehörigkeitsprüfung.
        - ``document_id`` (int): Optionale ID des verknüpften Dokuments (Landingpage) als ganze Zahl. Sie wird nur gespeichert, ohne Existenz- oder Zugehörigkeitsprüfung.
        - ``budget`` (float): Optionales Budget als Zahl, z. B. `25` oder `49.9`. Die Funktion gibt die Zahl ohne Währungs- oder Zeitraumangabe weiter; die Bedeutung (z. B. Tagesbudget) legst du selbst fest.
        - ``channels`` (str): Optionale Kanalangabe als Text. Im Datenmodell ist ein Auswahlfeld mit den Werten `ppc`, `socialmedia` und `email` vorgesehen; der Wert wird nicht gegen diese Liste geprüft.
        - ``is_active`` (bool): Aktivstatus der neuen Kampagne, `true` oder `false`. Standard `true`. Wird nur ausgewertet, wenn der Schlüssel im Körper steht.
        """
        return self._platform.call("campaigns", "create_campaign", {**(params or {}), **kwargs})

    def update_campaign(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kampagne aktualisieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/campaigns/update_campaign``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``campaign_id`` (int, Pflicht): ID der Kampagne (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_campaigns` oder aus der Antwort von `create_campaign`. Die Kampagne muss zur Firma deines Schlüssels gehören, sonst antwortet die Funktion mit „K…
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern (Pflicht). Erkannt werden `name`, `provider`, `campaign_type`, `content` (Text), `is_active` (boolean), `keyword_id`, `template_id`, `document_id` (ganze Zahlen), `budget` (Zahl), `ch…
        """
        return self._platform.call("campaigns", "update_campaign", {**(params or {}), **kwargs})

    def delete_campaign(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Kampagne löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/campaigns/delete_campaign``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``campaign_id`` (int, Pflicht): ID der Kampagne (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_campaigns` oder aus der Antwort von `create_campaign`. Die Kampagne muss zur Firma deines Schlüssels gehören, sonst antwortet die Funktion mit „K…
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("campaigns", "delete_campaign", {**(params or {}), **kwargs}, confirmed=confirmed)

    def copy_campaign(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kampagne kopieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/campaigns/copy_campaign``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``campaign_id`` (int, Pflicht): ID der Kampagne (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_campaigns` oder aus der Antwort von `create_campaign`. Die Kampagne muss zur Firma deines Schlüssels gehören, sonst antwortet die Funktion mit „K…
        - ``name`` (str): Optionaler Name der Kopie. Weggelassen heißt sie „<Name der Quelle> (Kopie)“. Wird getrimmt und HTML-maskiert gespeichert.
        - ``is_active`` (bool): Optionaler Aktivstatus der Kopie, `true` oder `false`. Weggelassen übernimmt die Kopie den Aktivstatus der Quellkampagne.
        """
        return self._platform.call("campaigns", "copy_campaign", {**(params or {}), **kwargs})

    def create_google_search_campaign(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Google-Suchkampagne mit KI-Texten anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/campaigns/create_google_search_campaign``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``template_id`` (int, Pflicht): ID der Landingpage-Vorlage (ganze Zahl, Pflicht). Sie wird an der Kampagne gespeichert und dient zusammen mit dem Keyword zum Wiederfinden der angelegten Kampagne. Es wird nicht geprüft, ob die Vorlage existiert.
        - ``keyword_id`` (int, Pflicht): ID des Keyword-Objekts (ganze Zahl, Pflicht). Aus dem Keyword (Suchbegriff, Intention, Schmerz, Lösung) entstehen die Anzeigentexte; der Suchbegriff wird als Keyword der Anzeigengruppe eingetragen.
        - ``document_id`` (int, Pflicht): ID des verknüpften Dokuments bzw. der Landingpage (ganze Zahl, Pflicht). Sie wird an der Kampagne gespeichert; die Ziel-URL der Anzeige wird dadurch nicht gesetzt.
        """
        return self._platform.call("campaigns", "create_google_search_campaign", {**(params or {}), **kwargs})

    def update_google_search_campaign(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Google-Suchkampagne neu texten

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/campaigns/update_google_search_campaign``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``campaign_id`` (int, Pflicht): ID der Kampagne (ganze Zahl, Pflicht). Sie muss zu deiner Firma gehören und ein Keyword (`keyword_id`) hinterlegt haben, aus dem die neuen Texte entstehen. Typischerweise ist es eine Kampagne aus `create_google_search_c…
        """
        return self._platform.call("campaigns", "update_google_search_campaign", {**(params or {}), **kwargs})

    def activate_campaign(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Kampagne aktivieren

        Recht am Schlüssel: ``veroeffentlichen`` · ``POST /platform/campaigns/activate_campaign``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``campaign_id`` (int, Pflicht): ID der Kampagne (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_campaigns` oder aus der Antwort von `create_campaign`. Die Kampagne muss zur Firma deines Schlüssels gehören, sonst antwortet die Funktion mit „K…
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("campaigns", "activate_campaign", {**(params or {}), **kwargs}, confirmed=confirmed)

    def pause_campaign(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kampagne pausieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/campaigns/pause_campaign``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``campaign_id`` (int, Pflicht): ID der Kampagne (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_campaigns` oder aus der Antwort von `create_campaign`. Die Kampagne muss zur Firma deines Schlüssels gehören, sonst antwortet die Funktion mit „K…
        """
        return self._platform.call("campaigns", "pause_campaign", {**(params or {}), **kwargs})

    def get_campaign_performance(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kampagnen-Performance abrufen (Platzhalter)

        Recht am Schlüssel: ``lesen`` · ``POST /platform/campaigns/get_campaign_performance``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``campaign_id`` (int, Pflicht): ID der Kampagne (Pimcore-Objekt-ID, ganze Zahl). Du bekommst sie aus `get_campaigns` oder aus der Antwort von `create_campaign`. Die Kampagne muss zur Firma deines Schlüssels gehören, sonst antwortet die Funktion mit „K…
        """
        return self._platform.call("campaigns", "get_campaign_performance", {**(params or {}), **kwargs})

    def get_campaign_stats(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kampagnen-Statistik der Firma

        Recht am Schlüssel: ``lesen`` · ``POST /platform/campaigns/get_campaign_stats``
        """
        return self._platform.call("campaigns", "get_campaign_stats", {**(params or {}), **kwargs})


class CrmArea(_Area):
    """CRM — Der Bereich CRM gibt dir Zugriff auf die Leads, Termine und Firmen deines Unternehmens."""

    def get_leads(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Leads auflisten und filtern

        Recht am Schlüssel: ``lesen`` · ``POST /platform/crm/get_leads``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Exakter Status-Wert, nach dem gefiltert wird, z. B. `new`, `won` oder `lost`. Welche Werte vorkommen, hängt von deiner Pipeline ab; es wird nur auf Gleichheit geprüft. Leer lassen für alle Status.
        - ``pipeline_id`` (int): ID der CRM-Pipeline, deren Leads du sehen willst (Ganzzahl). Die IDs liefert `list_pipelines`. Ohne Angabe werden Leads aller Pipelines geliefert.
        - ``search`` (str): Suchbegriff, der als Teilstring in Vorname, Nachname, E-Mail-Adresse oder Firma gesucht wird (ohne Beachtung der Groß-/Kleinschreibung, je nach Datenbank-Einstellung). Sonderzeichen wie & oder Anführungszeichen werden v…
        - ``marketplace_status`` (str): Exakter Marketplace-Status des Leads, z. B. wenn Leads im Lead-Marktplatz angeboten werden. Es wird nur auf Gleichheit geprüft; leer lassen für alle.
        - ``limit`` (int): Maximale Anzahl der zurückgegebenen Leads (Ganzzahl ab 1, Standard 25). Werte unter 1 werden auf 1 angehoben; ein Maximum gibt es nicht.
        - ``offset`` (int): Anzahl der Leads, die übersprungen werden (Ganzzahl ab 0, Standard 0). Zusammen mit `limit` zum Blättern: Seite 2 bei `limit` 25 ist `offset` 25.
        """
        return self._platform.call("crm", "get_leads", {**(params or {}), **kwargs})

    def get_lead(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Einen Lead im Detail abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/crm/get_lead``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``lead_id`` (int, Pflicht): Numerische ID des Leads, wie sie in `id` von `get_leads` und `create_lead` steht. Leads anderer Unternehmen werden nicht herausgegeben und führen zum selben Fehler wie eine unbekannte ID.
        """
        return self._platform.call("crm", "get_lead", {**(params or {}), **kwargs})

    def create_lead(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Lead anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/crm/create_lead``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``data`` (dict, Pflicht): Objekt mit den Lead-Feldern, z. B. `firstname`, `lastname`, `email`, `phone`, `company`, `status`, `description`, `pipeline_id`. Muss mindestens ein Feld enthalten, sonst Fehler „Leaddaten fehlen“. Text als String sende…
        """
        return self._platform.call("crm", "create_lead", {**(params or {}), **kwargs})

    def update_lead(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Lead aktualisieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/crm/update_lead``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``lead_id`` (int, Pflicht): Numerische ID des Leads, den du ändern willst (aus `get_leads`). Der Lead muss zu deinem Unternehmen gehören.
        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern, z. B. `{"phone": "+49 211 5550199", "status": "contacted"}`. Nicht genannte Felder bleiben unverändert. Zum Leeren eines Textfelds sende einen leeren String. Ohne `data` werden die ü…
        """
        return self._platform.call("crm", "update_lead", {**(params or {}), **kwargs})

    def delete_lead(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Lead dauerhaft löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/crm/delete_lead``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``lead_id`` (int, Pflicht): Numerische ID des zu löschenden Leads (aus `get_leads`). Leads anderer Unternehmen und unbekannte IDs führen zu einem Fehler und werden nicht gelöscht.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("crm", "delete_lead", {**(params or {}), **kwargs}, confirmed=confirmed)

    def change_lead_status(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Status oder Pipeline eines Leads ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/crm/change_lead_status``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``lead_id`` (int, Pflicht): Numerische ID des Leads (aus `get_leads`). Pflichtangabe; der Lead muss zu deinem Unternehmen gehören.
        - ``status`` (str): Neuer Status als Text, z. B. `contacted`, `qualified`, `won` oder `lost`. Die zulässigen Werte hängen von deiner Pipeline ab und werden nicht serverseitig geprüft. Weglassen, um den Status zu behalten.
        - ``pipeline_id`` (int): ID der Pipeline, in die der Lead verschoben wird (Ganzzahl, siehe `list_pipelines`). Weglassen, um die Pipeline zu behalten.
        - ``marketplace_status`` (str): Neuer Marketplace-Status als Text. Weglassen, um den bisherigen Wert zu behalten.
        """
        return self._platform.call("crm", "change_lead_status", {**(params or {}), **kwargs})

    def get_appointments(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Termine auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/crm/get_appointments``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Exakter Termin-Status, z. B. `scheduled`, `confirmed`, `cancelled`. Es wird auf Gleichheit geprüft; leer lassen für alle Status (abgesagte Termine eingeschlossen).
        - ``lead_id`` (int): ID des Leads, dessen Termine du sehen willst (Ganzzahl, aus `get_leads`). Ohne Angabe werden Termine aller Leads geliefert.
        - ``from`` (str): Beginn des Zeitraums als ISO-8601-Zeitpunkt, z. B. `2026-11-01T00:00:00+01:00`; auch ein reines Datum `2026-11-01` oder ein Unix-Zeitstempel wird verstanden. Es werden Termine ab diesem Zeitpunkt geliefert. Ungültige We…
        - ``to`` (str): Ende des Zeitraums, gleiches Format wie `from`. Es werden Termine bis einschließlich diesem Zeitpunkt geliefert; ein reines Datum bedeutet 00:00 Uhr dieses Tages.
        - ``limit`` (int): Maximale Anzahl der Termine (Ganzzahl ab 1, Standard 25). Ein Maximum gibt es nicht.
        - ``offset`` (int): Anzahl der zu überspringenden Termine (Ganzzahl ab 0, Standard 0), zum Blättern zusammen mit `limit`.
        """
        return self._platform.call("crm", "get_appointments", {**(params or {}), **kwargs})

    def schedule_appointment(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Termin anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/crm/schedule_appointment``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``date`` (str, Pflicht): Startzeit des Termins als ISO-8601-Zeitpunkt mit Offset, z. B. `2026-11-12T10:00:00+01:00`. Ohne Offset gilt die Zeitzone des Servers. Auch Unix-Zeitstempel werden akzeptiert. Pflichtangabe.
        - ``appointment_type`` (str): Art des Termins als Text, z. B. `firstcall`, `followup`, `interview`, `consulting`. Der Wert wird auch zur Bildung des internen Schlüssels verwendet. Frei wählbar, es gibt keine feste Liste.
        - ``status`` (str): Status des Termins, z. B. `scheduled` (Standard, wenn weggelassen) oder `confirmed`. Es wird nicht gegen eine feste Liste geprüft.
        - ``duration`` (int): Dauer in Minuten (Ganzzahl), z. B. 45. Fehlt sie, bleibt das Feld leer; `check_availability` rechnet bei leerer Dauer mit 45 Minuten.
        - ``lead_id`` (int): ID des verknüpften Leads (Ganzzahl, aus `get_leads`). Es wird nicht geprüft, ob der Lead zu deinem Unternehmen gehört – übergib nur eigene IDs.
        - ``interview_id`` (int): Optionale ID eines bestehenden Interviews, das mit dem Termin verknüpft wird (Ganzzahl). Es wird kein Interview angelegt.
        - ``channel`` (str): Kanal des Termins als Text, z. B. `video`, `phone`, `onsite`. Frei wählbar.
        - ``meeting_link`` (str): Link zum Online-Meeting oder Adresse des Treffpunkts als Text. Wird unverändert (HTML-codiert) gespeichert, nicht auf Gültigkeit geprüft.
        - ``contact`` (str): Kontaktperson oder Kurzbeschreibung als Text, z. B. `Mira Beispiel (mira.beispiel@example.com)`. Erscheint in `check_availability` unter den belegten Zeitfenstern.
        - ``notes`` (str): Interne Notizen zum Termin. HTML-Tags werden entfernt. Spätere Absagegründe (`cancel_appointment`) werden an diesen Text angehängt.
        - ``follow_up_required`` (bool): Wahrheitswert: `true`, wenn nach dem Termin eine Nachbearbeitung nötig ist. Standard ist `false`.
        """
        return self._platform.call("crm", "schedule_appointment", {**(params or {}), **kwargs})

    def update_appointment(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Termin ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/crm/update_appointment``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``appointment_id`` (int, Pflicht): Numerische ID des Termins (Feld `id` aus `get_appointments`). Der Termin muss zu deinem Unternehmen gehören, sonst Fehler „Termin nicht gefunden oder kein Zugriff“.
        - ``changes`` (dict, Pflicht): Objekt mit den zu ändernden Feldern, z. B. `{"date": "2026-11-13T14:00:00+01:00", "status": "confirmed"}`. Datumsfelder als ISO-8601-Zeitpunkt, Wahrheitswerte als `true`/`false`, `duration` in Minuten. Mit `null` bei `l…
        """
        return self._platform.call("crm", "update_appointment", {**(params or {}), **kwargs})

    def cancel_appointment(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Termin absagen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/crm/cancel_appointment``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``appointment_id`` (int, Pflicht): Numerische ID des Termins (Feld `id` aus `get_appointments`). Pflichtangabe; der Termin muss zu deinem Unternehmen gehören.
        - ``reason`` (str): Grund der Absage als Text. Wird mit Datum und Uhrzeit an die Notizen des Termins angehängt; HTML-Tags werden entfernt. Leerer Text wird ignoriert.
        - ``status`` (str): Optional ein eigener Status statt `cancelled`, z. B. `no-show`. Ist der Wert leer, gilt `cancelled`. `cancelled` und `no-show` gelten in `check_availability` als frei.
        """
        return self._platform.call("crm", "cancel_appointment", {**(params or {}), **kwargs})

    def list_pipelines(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CRM-Pipelines auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/crm/list_pipelines``
        """
        return self._platform.call("crm", "list_pipelines", {**(params or {}), **kwargs})

    def list_workflows(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """CRM-Workflows auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/crm/list_workflows``
        """
        return self._platform.call("crm", "list_workflows", {**(params or {}), **kwargs})

    def list_email_templates(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """E-Mail-Vorlagen auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/crm/list_email_templates``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``active_only`` (bool): Wahrheitswert. Bei `true` werden nur aktive Vorlagen geliefert, bei `false` oder ohne Angabe alle Vorlagen, auch deaktivierte.
        """
        return self._platform.call("crm", "list_email_templates", {**(params or {}), **kwargs})

    def summarize_lead(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Lead zusammenfassen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/crm/summarize_lead``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``lead_id`` (int, Pflicht): Numerische ID des Leads (aus `get_leads`). Pflichtangabe; der Lead muss zu deinem Unternehmen gehören.
        """
        return self._platform.call("crm", "summarize_lead", {**(params or {}), **kwargs})

    def check_availability(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Freie Termine an einem Tag prüfen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/crm/check_availability``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``date`` (str, Pflicht): Der zu prüfende Tag im Format `YYYY-MM-DD`, z. B. `2026-11-12`. Muss genau in dieser Schreibweise angegeben werden, da sie direkt mit dem Terminbestand verglichen wird. Pflichtangabe.
        - ``preferred_time`` (str): Gewünschte Startzeit im Format `HH:MM` (24 Stunden), z. B. `14:00`. Mit der Angabe liefert die Antwort `preferred_time_available` und eine passende Empfehlung samt bis zu drei Alternativen. Ohne Angabe ist der Wert `fal…
        - ``duration`` (int): Gewünschte Dauer in Minuten (Ganzzahl). Standard 45, Werte unter 15 werden auf 15 angehoben. Bestimmt, welche Startzeiten als frei gelten.
        - ``appointment_type`` (str): Im Schema vorgesehene Terminart (z. B. `firstcall`, `interview`). Der Wert wird derzeit nicht ausgewertet; das Ergebnis ist für alle Arten gleich.
        """
        return self._platform.call("crm", "check_availability", {**(params or {}), **kwargs})

    def trigger_website_crawl(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Website-Analyse starten

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/crm/trigger_website_crawl``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``url`` (str): Adresse der zu analysierenden Webseite, mit oder ohne `https://` (z. B. `www.example.com`). Optional; ohne Angabe wird die bei der Firma gespeicherte Domain bzw. URL genommen. Der Text wird getrimmt und HTML-codiert.
        """
        return self._platform.call("crm", "trigger_website_crawl", {**(params or {}), **kwargs})


class ArangoArea(_Area):
    """Wissensgraph — Der Bereich Wissensgraph bildet die Daten deines Unternehmens als Netz ab: Datensätze (Leads, Termine, Bücher, Angebote, Mitglieder, Kurse …) liegen in Sammlungen und sind über Kanten miteinander verbunden."""

    def get_company_knowledge_graph(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Überblick über den Wissensgraphen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/arango/get_company_knowledge_graph``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``depth`` (int): Traversierungstiefe als Ganzzahl von 1 bis 3, Standard 2. Werte außerhalb des Bereichs werden auf 1 bzw. 3 begrenzt, 0 oder nicht angegeben ergibt 2. Tiefe 1 zählt nur direkte Nachbarn der Firma, höhere Werte auch deren…
        """
        return self._platform.call("arango", "get_company_knowledge_graph", {**(params or {}), **kwargs})

    def get_company_summary(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kompakte Firmenübersicht mit Zählungen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/arango/get_company_summary``
        """
        return self._platform.call("arango", "get_company_summary", {**(params or {}), **kwargs})

    def find_connections(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kürzeste Verbindung zwischen zwei Datensätzen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/arango/find_connections``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``from_collection`` (str, Pflicht): Name der Sammlung des Startdatensatzes in Kleinschreibung, z. B. `leads`, `books`, `members`. Die möglichen Namen liefert `get_company_summary`.
        - ``from_key`` (str, Pflicht): Schlüssel (`_key`) des Startdatensatzes innerhalb der Sammlung, z. B. `lead_12345`. Wird aus `search_graph` oder `get_entity_context` übernommen.
        - ``to_collection`` (str, Pflicht): Name der Sammlung des Zieldatensatzes, z. B. `books`. Gleiche Schreibweise wie bei `from_collection`.
        - ``to_key`` (str, Pflicht): Schlüssel (`_key`) des Zieldatensatzes, z. B. `book_67890`. Der Datensatz muss zu deinem Unternehmen gehören.
        """
        return self._platform.call("arango", "find_connections", {**(params or {}), **kwargs})

    def get_entity_context(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Nachbarn eines Datensatzes anzeigen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/arango/get_entity_context``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``collection`` (str, Pflicht): Name der Sammlung des Startdatensatzes in Kleinschreibung, z. B. `members`, `books`, `leads`. Die vorhandenen Sammlungen siehst du in `get_company_summary`.
        - ``key`` (str, Pflicht): Schlüssel (`_key`) des Startdatensatzes, z. B. `member_123`. Erlaubt sind Buchstaben, Ziffern und einige Sonderzeichen wie `_`, `-` und `:`.
        - ``depth`` (int): Traversierungstiefe, Ganzzahl bis 3, Standard 1. Tiefe 1 liefert direkte Nachbarn, 2 auch deren Nachbarn usw. Mit der Tiefe wächst die Treffermenge schnell; gedeckelt bei 200 Knoten.
        """
        return self._platform.call("arango", "get_entity_context", {**(params or {}), **kwargs})

    def search_graph(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Datensätze einer Sammlung filtern

        Recht am Schlüssel: ``lesen`` · ``POST /platform/arango/search_graph``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``collection`` (str, Pflicht): Name der Sammlung in Kleinschreibung, z. B. `leads`, `books`, `offers`, `testimonials`, `interviews`, `appointments`, `podcasts`, `courses`. Welche Sammlungen bei dir Daten haben, zeigt `get_company_summary`.
        - ``filters`` (list): Liste von Bedingungen, höchstens 8 (weitere werden ignoriert); alle müssen zutreffen. Jede Bedingung ist ein Objekt mit `field` (Feldname, nur Buchstaben, Ziffern, Unterstrich, höchstens 64 Zeichen) und `op`; `value` is…
        - ``fields`` (list): Liste der Feldnamen, die je Treffer zurückgegeben werden, höchstens 20. `_key` und `_className` kommen immer mit. Fehlt die Angabe, werden Standardfelder geliefert (name, firstname, lastname, title, email, status, _modi…
        - ``sort_field`` (str): Feldname, nach dem sortiert wird, z. B. `_modificationDate` für die zuletzt geänderten Datensätze zuerst. Optional; muss ein gültiger Feldname sein.
        - ``sort_dir`` (str): Sortierrichtung `ASC` (aufsteigend) oder `DESC` (absteigend, Standard). Wirkt nur, wenn `sort_field` gesetzt ist.
        - ``limit`` (int): Maximale Zahl der zurückgegebenen Treffer, Ganzzahl. Standard 25, größter Wert 50; kleinere Werte als 1 ergeben den Standard. `count` in der Antwort nennt trotzdem die Gesamtzahl.
        """
        return self._platform.call("arango", "search_graph", {**(params or {}), **kwargs})

    def get_activity_timeline(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Letzte Änderungen im Unternehmen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/arango/get_activity_timeline``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``limit`` (int): Anzahl der zurückgegebenen Einträge, Ganzzahl. Standard 20, größter Wert 50. Nicht angegeben oder 0 ergibt 20.
        """
        return self._platform.call("arango", "get_activity_timeline", {**(params or {}), **kwargs})

    def wissen_suche(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Unternehmenswissen durchsuchen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/arango/wissen_suche``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``query`` (str, Pflicht): Suchanfrage in natürlicher Sprache oder als Stichwort, z. B. `Garantie Werkzeugwartung`. Pflichtangabe, nicht leer. Für die Bedeutungssuche sind ganze Fragen geeignet, für die Textsuche in den Unternehmensdaten kurze Be…
        - ``limit`` (int): Maximale Anzahl der Treffer aus Wissensartikeln und Unternehmensdaten, Ganzzahl. Standard 5, größter Wert 15. Dateifunde (bis zu 3) kommen zusätzlich dazu.
        """
        return self._platform.call("arango", "wissen_suche", {**(params or {}), **kwargs})

    def wissen_graph(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Verknüpfte Inhalte zu einem Dokument

        Recht am Schlüssel: ``lesen`` · ``POST /platform/arango/wissen_graph``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``collection`` (str, Pflicht): Sammlung des Ausgangsdokuments in Kleinschreibung, z. B. `stories` oder `handbook_pages`. Bei Treffern aus `wissen_suche` steht der Wert in `collection`; Sammlungsnamen mit Daten liefert `get_company_summary`.
        - ``key`` (str, Pflicht): Schlüssel des Ausgangsdokuments (`_key`) im Graph-Format, z. B. `handbook_page_204`. Bei Treffern aus `wissen_suche` steht er in `id`.
        - ``depth`` (int): Tiefe der Verknüpfungssuche als Ganzzahl bis 3, Standard 2. Tiefe 1 liefert nur direkt verbundene Inhalte; größere Werte liefern deutlich mehr Knoten (gedeckelt bei 200).
        """
        return self._platform.call("arango", "wissen_graph", {**(params or {}), **kwargs})


class BusinessModelArea(_Area):
    """Geschäftsmodell — Das Geschäftsmodell beschreibt, wie dein Unternehmen Geld verdient und Angebote kalkuliert."""

    def get_business_model(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Geschäftsmodell lesen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/business_model/get_business_model``
        """
        return self._platform.call("business_model", "get_business_model", {**(params or {}), **kwargs})

    def update_business_model(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Geschäftsmodell ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/business_model/update_business_model``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``data`` (dict, Pflicht): Objekt mit den zu ändernden Feldern. `offer_components`: Liste von `{name, role (mandatory|optional|alternative), cycle (once|monthly|yearly), note}`. `calculation_basis`: `{hourly_rate (Cent), target_margin_pct, notes,…
        """
        return self._platform.call("business_model", "update_business_model", {**(params or {}), **kwargs})


class ProductsArea(_Area):
    """Produkte — Der Bereich durchsucht den Produktkatalog deines Unternehmens."""

    def search_products(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Produkte suchen und filtern

        Recht am Schlüssel: ``lesen`` · ``POST /platform/products/search_products``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``query`` (str): Suchtext, z. B. „Roboter mit langer Akkulaufzeit“. Optional, wenn `filters` gesetzt ist; dann bestimmt der Text nur die Reihenfolge der gefilterten Produkte.
        - ``limit`` (int): Maximale Anzahl gelieferter Treffer. Ganzzahl von 1 bis 20, Standard 12; Werte außerhalb werden auf diesen Bereich begrenzt.
        - ``filters`` (list): Liste von bis zu 4 Zahlenfiltern, alle müssen erfüllt sein. Jeder Filter ist ein Objekt mit `attr` (`akkulaufzeit_min`, `akkukapazitaet_wh`, `ladezeit_min`, `gewicht_kg`, `flaechenleistung_m2h`, `arbeitsbreite_cm`, `ste…
        """
        return self._platform.call("products", "search_products", {**(params or {}), **kwargs})


class SparringArea(_Area):
    """Content-Ideen — Der Bereich sparring verwaltet Content-Ideen, die aus Sparring-Gesprächen entstehen oder manuell angelegt werden."""

    def get_content_ideas(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Content-Ideen auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/sparring/get_content_ideas``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Optionaler Statusfilter, exakt verglichen: `active`, `in_progress` oder `archived`. Ohne Angabe werden alle Ideen außer archivierten geliefert.
        - ``content_type`` (str): Optionaler Filter auf den Ziel-Typ: `podcast_episode`, `book_chapter`, `blog_post`, `social_media` oder `landingpage`. Wird nach der Begrenzung durch `limit` angewendet.
        - ``min_score`` (float): Optionale Mindestgrenze für den Composite-Score als Zahl zwischen 0.0 und 1.0. Ideen mit niedrigerem oder fehlendem Score (zählt als 0) werden aussortiert; die Prüfung erfolgt nach der Begrenzung durch `limit`.
        - ``limit`` (int): Maximale Zahl der zunächst geladenen Ideen als ganze Zahl, mindestens 1. Standard ist 10. Beachte, dass die übrigen Filter danach greifen und die Antwort kleiner ausfallen kann.
        """
        return self._platform.call("sparring", "get_content_ideas", {**(params or {}), **kwargs})

    def get_idea_backlog(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Beste Ideen (Backlog)

        Recht am Schlüssel: ``lesen`` · ``POST /platform/sparring/get_idea_backlog``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``limit`` (int): Anzahl der zurückgegebenen Ideen als ganze Zahl, mindestens 1. Standard ist 5. Mehr als 50 Ideen kann der Backlog nie enthalten.
        """
        return self._platform.call("sparring", "get_idea_backlog", {**(params or {}), **kwargs})

    def create_content_idea(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Content-Idee anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/sparring/create_content_idea``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``title`` (str, Pflicht): Titel der Content-Idee als Text. Pflichtangabe.
        - ``content_type`` (str, Pflicht): Ziel-Typ der Idee. Dokumentierte Werte: `podcast_episode`, `book_chapter`, `blog_post`, `social_media`, `landingpage`. Pflichtangabe; andere Werte werden zwar gespeichert, aber ohne sprechende Beschriftung ausgegeben.
        - ``description`` (str): Optionale Beschreibung oder Begründung der Idee. Ohne Angabe bleibt das Feld leer.
        - ``keyword`` (str): Optionales Haupt-Keyword, auf das die Idee zielt. Es wird als `keyword` der Idee gespeichert und für die Anreicherung herangezogen.
        - ``target_audience`` (str): Optionale Zielgruppe, für die der Inhalt gedacht ist, z. B. „Inhaber kleiner Betriebe“. Wird im Feld `target_audience` ausgegeben.
        - ``urgency`` (float): Optionale Dringlichkeit als Zahl von 0.0 (nicht dringend) bis 1.0 (sehr dringend). Werte außerhalb werden auf diesen Bereich begrenzt. Standard 0.5; bestimmt die Sortierung in `get_content_ideas`.
        - ``impact`` (float): Optionaler erwarteter Geschäftsnutzen als Zahl von 0.0 bis 1.0. Werte außerhalb werden begrenzt. Standard 0.5. Wird in `business_impact` ausgegeben.
        """
        return self._platform.call("sparring", "create_content_idea", {**(params or {}), **kwargs})

    def approve_idea(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Content-Idee genehmigen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/sparring/approve_idea``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``idea_id`` (int, Pflicht): Numerische ID der Content-Idee, wie sie `get_content_ideas`, `get_idea_backlog` oder `create_content_idea` als `id` liefern. Pflichtangabe.
        """
        return self._platform.call("sparring", "approve_idea", {**(params or {}), **kwargs})

    def archive_idea(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Content-Idee archivieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/sparring/archive_idea``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``idea_id`` (int, Pflicht): Numerische ID der Content-Idee, die archiviert werden soll. Pflichtangabe; die Idee muss zu deiner Firma gehören.
        - ``reason`` (str): Optionale Begründung als Text, z. B. „Thema inzwischen bereits veröffentlicht“. Wird bei der Idee abgelegt und HTML-maskiert gespeichert. Leere Angaben werden ignoriert.
        """
        return self._platform.call("sparring", "archive_idea", {**(params or {}), **kwargs})


class BaukastenArea(_Area):
    """Agenten und Anwendungen — Der Baukasten ist die Werkstatt für Anwendungen (kleine Bildschirmabläufe aus festen Bausteinen) und Agenten (Abläufe, die Schritt für Schritt ohne Menschen laufen)."""

    def canvas_oeffnen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Canvas anlegen oder weiterbauen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/canvas_oeffnen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``titel`` (str, Pflicht): Name der Anwendung, z. B. „Inbetriebnahme Reinigungsroboter“. Wird auf 160 Zeichen gekürzt; ein leerer Text ergibt „Neue Anwendung“. Wird ignoriert, wenn die Funktion einen jungen vorhandenen Entwurf zurückgibt.
        - ``beschreibung`` (str): Optionale Beschreibung in ein bis zwei Sätzen, was die Anwendung leistet. Wird auf 600 Zeichen gekürzt und später in der Anwendungsliste angezeigt.
        - ``kontext_typ`` (str): Optional: Für welchen Datensatz die Anwendung gestartet wird. Erlaubt sind `geraet` (ein Gerät) und `lead` (ein Lead). Dann stehen beim Ausführen die Daten dieses Objekts über Platzhalter wie `{{kontext.…}}` bereit. Ohn…
        """
        return self._platform.call("baukasten", "canvas_oeffnen", {**(params or {}), **kwargs})

    def canvas_lesen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Canvas lesen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/baukasten/canvas_lesen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``app_id`` (int, Pflicht): ID der Anwendung (des Canvas) als ganze Zahl. Du bekommst sie aus `canvas_oeffnen` (Feld `app_id`) oder aus `anwendungen_liste` (Feld `id`). Bearbeiten darf die Anwendung nur ihr Ersteller oder ein Administrator der Fir…
        """
        return self._platform.call("baukasten", "canvas_lesen", {**(params or {}), **kwargs})

    def canvas_setzen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Alle Bausteine setzen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/canvas_setzen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``app_id`` (int, Pflicht): ID der Anwendung (des Canvas) als ganze Zahl. Du bekommst sie aus `canvas_oeffnen` (Feld `app_id`) oder aus `anwendungen_liste` (Feld `id`). Bearbeiten darf die Anwendung nur ihr Ersteller oder ein Administrator der Fir…
        - ``bausteine`` (list, Pflicht): Vollständige Liste der Bausteine als Array von Objekten, jeweils `{id, typ, …Felder des Typs}`. Beispiele: `text {titel, inhalt (Markdown)}`, `hinweis {ton: info|tipp|warnung|pflicht, inhalt}`, `checkliste {punkte[{id,…
        """
        return self._platform.call("baukasten", "canvas_setzen", {**(params or {}), **kwargs})

    def canvas_baustein_einfuegen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Baustein einfügen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/canvas_baustein_einfuegen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``app_id`` (int, Pflicht): ID der Anwendung (des Canvas) als ganze Zahl. Du bekommst sie aus `canvas_oeffnen` (Feld `app_id`) oder aus `anwendungen_liste` (Feld `id`). Bearbeiten darf die Anwendung nur ihr Ersteller oder ein Administrator der Fir…
        - ``baustein`` (dict, Pflicht): Der neue Baustein als Objekt `{id, typ, …Felder des Typs}`. Erlaubte Typen: text, hinweis, ablauf, tabelle, bild, checkliste, formular, schritte, liste, kennzahl, eintraege, aktion, abschnitt, spalten. Die `id` besteht…
        - ``nach`` (str): Optional: ID des Bausteins, hinter den der neue gesetzt wird (auch ein verschachtelter). Der Sonderwert `anfang` setzt ihn an die erste Stelle. Fehlt die Angabe, landet der Baustein am Ende der obersten Ebene.
        """
        return self._platform.call("baukasten", "canvas_baustein_einfuegen", {**(params or {}), **kwargs})

    def canvas_baustein_aendern(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Baustein ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/canvas_baustein_aendern``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``app_id`` (int, Pflicht): ID der Anwendung (des Canvas) als ganze Zahl. Du bekommst sie aus `canvas_oeffnen` (Feld `app_id`) oder aus `anwendungen_liste` (Feld `id`). Bearbeiten darf die Anwendung nur ihr Ersteller oder ein Administrator der Fir…
        - ``id`` (str, Pflicht): ID des Bausteins, der geändert werden soll, z. B. `intro`. Die IDs erfährst du aus `canvas_lesen` oder aus der Kurzliste `bausteine` der letzten Antwort.
        - ``felder`` (dict, Pflicht): Objekt mit nur den Feldern, die sich ändern, z. B. `{"inhalt": "Neuer Text"}` oder `{"titel": "Neuer Titel"}`. Die Werte ersetzen die bisherigen komplett. `id` und `typ` in diesem Objekt werden ignoriert.
        """
        return self._platform.call("baukasten", "canvas_baustein_aendern", {**(params or {}), **kwargs})

    def canvas_baustein_entfernen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Baustein entfernen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/canvas_baustein_entfernen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``app_id`` (int, Pflicht): ID der Anwendung (des Canvas) als ganze Zahl. Du bekommst sie aus `canvas_oeffnen` (Feld `app_id`) oder aus `anwendungen_liste` (Feld `id`). Bearbeiten darf die Anwendung nur ihr Ersteller oder ein Administrator der Fir…
        - ``id`` (str, Pflicht): ID des Bausteins, der entfernt werden soll, z. B. `warnhinweis`. Sie steht in der Kurzliste `bausteine` jeder Antwort und im Ergebnis von `canvas_lesen`.
        """
        return self._platform.call("baukasten", "canvas_baustein_entfernen", {**(params or {}), **kwargs})

    def canvas_baustein_verschieben(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Baustein verschieben

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/canvas_baustein_verschieben``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``app_id`` (int, Pflicht): ID der Anwendung (des Canvas) als ganze Zahl. Du bekommst sie aus `canvas_oeffnen` (Feld `app_id`) oder aus `anwendungen_liste` (Feld `id`). Bearbeiten darf die Anwendung nur ihr Ersteller oder ein Administrator der Fir…
        - ``id`` (str, Pflicht): ID des Bausteins, der verschoben werden soll, z. B. `pruefung`.
        - ``nach`` (str): Optional: ID des Bausteins, hinter den der verschobene gesetzt wird. `anfang` bedeutet ganz nach vorn. Ohne Angabe wird der Baustein ans Ende der obersten Ebene gestellt.
        """
        return self._platform.call("baukasten", "canvas_baustein_verschieben", {**(params or {}), **kwargs})

    def canvas_rueckgaengig(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Letzte Änderung rückgängig machen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/canvas_rueckgaengig``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``app_id`` (int, Pflicht): ID der Anwendung (des Canvas) als ganze Zahl. Du bekommst sie aus `canvas_oeffnen` (Feld `app_id`) oder aus `anwendungen_liste` (Feld `id`). Bearbeiten darf die Anwendung nur ihr Ersteller oder ein Administrator der Fir…
        """
        return self._platform.call("baukasten", "canvas_rueckgaengig", {**(params or {}), **kwargs})

    def baukasten_werkzeuge(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Erlaubte Werkzeuge suchen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/baukasten/baukasten_werkzeuge``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``art`` (str, Pflicht): Welche Sorte Werkzeug du suchst: `lesen` für Datenquellen (Liste, Kennzahl, lesende Agenten-Schritte) oder `schreiben` für Aktionen, die Daten verändern. Pflichtangabe im Schema; ein anderer Wert wird wie „keine Angabe“…
        - ``suche`` (str): Optionales Stichwort, z. B. `ticket` oder `wartung`. Gesucht wird in Name und Beschreibung der Werkzeuge. Ohne Angabe kommen die ersten Werkzeuge der gewählten Art.
        """
        return self._platform.call("baukasten", "baukasten_werkzeuge", {**(params or {}), **kwargs})

    def anwendungen_liste(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Anwendungen auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/baukasten/anwendungen_liste``
        """
        return self._platform.call("baukasten", "anwendungen_liste", {**(params or {}), **kwargs})

    def anwendung_oeffnen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Anwendung im Chat öffnen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/anwendung_oeffnen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``app_id`` (int, Pflicht): ID der Anwendung als ganze Zahl (aus `anwendungen_liste`). Im Chat der Zentrale wird die Anwendung damit an den aktuellen Chat gebunden; über die API wird der Wert nicht ausgewertet, weil vorher der Chat-Fehler kommt.
        """
        return self._platform.call("baukasten", "anwendung_oeffnen", {**(params or {}), **kwargs})

    def agent_entwurf(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Agenten-Entwurf anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/agent_entwurf``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``name`` (str, Pflicht): Name des Agenten, z. B. „Anfragen sichten“. Wird auf 160 Zeichen gekürzt; ein leerer Name ergibt „Neuer Agent“. Der Name wird in Listen und beim Start über `agent_starten` verwendet.
        - ``beschreibung`` (str): Optionale Beschreibung, wozu der Agent da ist, in ein bis zwei Sätzen. Wird auf 600 Zeichen gekürzt und in der Agentenliste gezeigt.
        - ``anweisungen`` (str): Optional: Was der Agent wissen muss, in ganzen Sätzen (Fachbegriffe, Regeln des Hauses, Tonfall). Wird auf 6000 Zeichen gekürzt und jedem KI-Schritt als Hintergrundwissen mitgegeben.
        """
        return self._platform.call("baukasten", "agent_entwurf", {**(params or {}), **kwargs})

    def agent_oeffnen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Agent im Chat öffnen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/agent_oeffnen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``agent_id`` (int, Pflicht): ID des Agenten als ganze Zahl. Du bekommst sie aus `agent_entwurf` (Feld `agent_id`) oder `agenten_liste` (Feld `id`). Ändern darf den Agenten nur sein Ersteller oder ein Administrator der Firma; eine fremde, archiviert…
        """
        return self._platform.call("baukasten", "agent_oeffnen", {**(params or {}), **kwargs})

    def agent_briefing(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Briefing, Leitplanken und KI-Stufe setzen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/agent_briefing``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``agent_id`` (int, Pflicht): ID des Agenten als ganze Zahl. Du bekommst sie aus `agent_entwurf` (Feld `agent_id`) oder `agenten_liste` (Feld `id`). Ändern darf den Agenten nur sein Ersteller oder ein Administrator der Firma; eine fremde, archiviert…
        - ``briefing`` (dict): Objekt mit `ziel` (wozu es den Agenten gibt) und `fertig_wenn` (woran man erkennt, dass die Arbeit erledigt ist), jeweils bis 1000 Zeichen. Beide Felder werden zusammen gesetzt; ein fehlendes wird leer.
        - ``anweisungen`` (str): Wissen des Agenten in ganzen Sätzen, bis 6000 Zeichen. Ersetzt den bisherigen Text. Wird jedem KI-Schritt als Hintergrund mitgegeben.
        - ``leitplanken`` (list): Liste kurzer Regeln wie „Nie …“, „Immer …“, „Nur …“; höchstens 20 Einträge zu je 300 Zeichen. Die Liste ersetzt die bisherigen Leitplanken vollständig. Sie gelten in KI-Schritten vor jeder anderen Anweisung; verletzt ei…
        - ``modell`` (str): KI-Stufe des Agenten als Standard für alle KI-Schritte: `schnell` (Standard), `ausgewogen`, `gruendlich` oder `tiefgang`. Eine unbekannte Stufe wird mit dem Satz „Das KI-Modell … gibt es nicht.“ abgelehnt.
        """
        return self._platform.call("baukasten", "agent_briefing", {**(params or {}), **kwargs})

    def agent_setzen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Schritte, Auslöser und Werkzeuge setzen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/agent_setzen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``agent_id`` (int, Pflicht): ID des Agenten als ganze Zahl. Du bekommst sie aus `agent_entwurf` (Feld `agent_id`) oder `agenten_liste` (Feld `id`). Ändern darf den Agenten nur sein Ersteller oder ein Administrator der Firma; eine fremde, archiviert…
        - ``schritte`` (list, Pflicht): Vollständige Liste der Schritte, jeweils `{key, typ, titel, …}`. `key`: a-z, 0-9, _ (höchstens 40 Zeichen), eindeutig; `ende`, `eingabe`, `kontext` und `schritte` sind reserviert. `typ` und seine Felder: `werkzeug {werk…
        - ``werkzeuge`` (list): Liste der Werkzeuge, die der Agent benutzen darf, als Objekte `{name, ohne_rueckfrage, aussen_bestaetigt}` (beide Schalter Standard `false`). Jedes in einem `werkzeug`- oder `frei`-Schritt benutzte Werkzeug muss hier st…
        - ``ausloeser`` (dict): Wann Läufe entstehen. `hand` ist immer wahr. `ereignisse`: Liste von Ereignissen der Plattform, z. B. `lead.neu`, `rueckruf.gewuenscht`, `mail.neu`, `ticket.neu`, `angebot.angenommen`, `rechnung.bezahlt`, `rechnung.uebe…
        - ``budget`` (dict): Obergrenzen je Lauf als Objekt `{schritte, ki, minuten}`: `schritte` 1–200 (Standard 60), `ki` 0–100 KI-Aufrufe (Standard 40), `minuten` 1–120 (Standard 30). Werte außerhalb werden begrenzt. Ist ein Limit erreicht, wird…
        - ``anweisungen`` (str): Wissen des Agenten in ganzen Sätzen, bis 6000 Zeichen. Fehlt das Feld, bleibt der bisherige Text.
        - ``briefing`` (dict): Objekt `{ziel, fertig_wenn}` mit je bis zu 1000 Zeichen: wozu es den Agenten gibt und woran man erkennt, dass er fertig ist. Fehlt das Feld, bleibt das bisherige Briefing.
        - ``leitplanken`` (list): Liste kurzer Regeln („Nie …“, „Immer …“, „Nur …“), höchstens 20 zu je 300 Zeichen. Ersetzt die bisherigen. Fehlt das Feld, bleiben die bisherigen.
        - ``modell`` (str): KI-Stufe des Agenten: `schnell` (Standard), `ausgewogen`, `gruendlich` oder `tiefgang`. Einzelne KI-, Datei-, Browser- und freie Schritte können mit ihrem Feld `modell` eine eigene Stufe wählen.
        - ``benachrichtigung`` (dict): Wer nach einem Lauf Bescheid bekommt: Objekt `{glocke: bool, email: bool, auch_fehler: bool}`. Benachrichtigt wird der Inhaber der Firma (Glocke oben bzw. E-Mail); mit `auch_fehler: true` auch bei Fehler oder Anhalten,…
        """
        return self._platform.call("baukasten", "agent_setzen", {**(params or {}), **kwargs})

    def agent_schritt_einfuegen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Schritt einfügen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/agent_schritt_einfuegen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``agent_id`` (int, Pflicht): ID des Agenten als ganze Zahl. Du bekommst sie aus `agent_entwurf` (Feld `agent_id`) oder `agenten_liste` (Feld `id`). Ändern darf den Agenten nur sein Ersteller oder ein Administrator der Firma; eine fremde, archiviert…
        - ``schritt`` (dict, Pflicht): Der neue Schritt als Objekt `{key, typ, titel, …Felder des Typs}`. `typ` ist einer von werkzeug, ki, datei, browser, frei, frage, entscheidung, tabelle, pdf_werte, berechnen. Der `key` besteht aus a-z, 0-9, _ (höchstens…
        - ``nach`` (str): Optional: Key des Schritts, hinter den der neue gesetzt wird. `anfang` bedeutet ganz nach vorn, ohne Angabe wird der Schritt ans Ende gehängt. Ein unbekannter Key ergibt den Satz „Den Schritt „…“ gibt es nicht.“
        """
        return self._platform.call("baukasten", "agent_schritt_einfuegen", {**(params or {}), **kwargs})

    def agent_schritt_aendern(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Schritt ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/agent_schritt_aendern``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``agent_id`` (int, Pflicht): ID des Agenten als ganze Zahl. Du bekommst sie aus `agent_entwurf` (Feld `agent_id`) oder `agenten_liste` (Feld `id`). Ändern darf den Agenten nur sein Ersteller oder ein Administrator der Firma; eine fremde, archiviert…
        - ``key`` (str, Pflicht): Key des Schritts, der geändert werden soll, z. B. `einschaetzen`. Die Keys stehen in der Liste `schritte` jeder Antwort und in `agent_lesen`.
        - ``felder`` (dict, Pflicht): Objekt mit den zu ändernden Feldern, z. B. `{"anweisung": "…"}`, `{"parameter": {…}}` oder `{"titel": "…"}`. Unbekannte Felder des Schritttyps werden bei der Prüfung verworfen; `key` und `typ` in diesem Objekt werden ig…
        """
        return self._platform.call("baukasten", "agent_schritt_aendern", {**(params or {}), **kwargs})

    def agent_schritt_entfernen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Schritt entfernen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/agent_schritt_entfernen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``agent_id`` (int, Pflicht): ID des Agenten als ganze Zahl. Du bekommst sie aus `agent_entwurf` (Feld `agent_id`) oder `agenten_liste` (Feld `id`). Ändern darf den Agenten nur sein Ersteller oder ein Administrator der Firma; eine fremde, archiviert…
        - ``key`` (str, Pflicht): Key des Schritts, der entfernt werden soll, z. B. `freigabe`. Er steht in der Liste `schritte` jeder Antwort und in `agent_lesen`.
        """
        return self._platform.call("baukasten", "agent_schritt_entfernen", {**(params or {}), **kwargs})

    def agent_lesen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Agenten lesen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/baukasten/agent_lesen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``agent_id`` (int, Pflicht): ID des Agenten als ganze Zahl. Du bekommst sie aus `agent_entwurf` (Feld `agent_id`) oder `agenten_liste` (Feld `id`). Ändern darf den Agenten nur sein Ersteller oder ein Administrator der Firma; eine fremde, archiviert…
        """
        return self._platform.call("baukasten", "agent_lesen", {**(params or {}), **kwargs})

    def agenten_liste(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Agenten auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/baukasten/agenten_liste``
        """
        return self._platform.call("baukasten", "agenten_liste", {**(params or {}), **kwargs})

    def agent_starten(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Agenten starten oder simulieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/agent_starten``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``agent_id`` (int): ID des Agenten als ganze Zahl (aus `agent_entwurf` oder `agenten_liste`). Alternativ kannst du `name` angeben. Fehlen beide oder passt keiner, kommt „Diesen Agenten gibt es nicht.“ bzw. „Einen Agenten mit diesem Namen g…
        - ``name`` (str): Name oder Namensteil des Agenten, Groß-/Kleinschreibung egal. Es muss genau ein sichtbarer Agent passen; bei mehreren Treffern nennt `error` die Namen und fragt, welcher gemeint ist. Wird nur ausgewertet, wenn `agent_id…
        - ``eingabe`` (dict): Objekt mit den Eingabewerten des Laufs. Im Ablauf sind sie als `{{eingabe.<name>}}` abrufbar, z. B. `{"lead_id": 2088}` als `{{eingabe.lead_id}}`. Passwörter und ähnliche Felder werden im Protokoll geschwärzt. Ohne Anga…
        - ``simulation`` (bool): Boolean, Standard `false`. Bei `true` läuft der gespeicherte Entwurf als Probe: nichts wird verändert, nichts geht nach außen, Rückfragen werden automatisch bejaht. Nur Verwalter des Agenten dürfen das („Simulieren dürf…
        """
        return self._platform.call("baukasten", "agent_starten", {**(params or {}), **kwargs})

    def agent_lauf_status(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Stand eines Laufs

        Recht am Schlüssel: ``lesen`` · ``POST /platform/baukasten/agent_lauf_status``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``lauf_id`` (int, Pflicht): ID des Laufs als ganze Zahl. Du bekommst sie aus der Antwort von `agent_starten` (Feld `lauf_id`) oder aus `agent_rueckfragen` (Feld `lauf_id`). Eingreifen darf die Person, die den Lauf gestartet hat, sowie die Verwalte…
        """
        return self._platform.call("baukasten", "agent_lauf_status", {**(params or {}), **kwargs})

    def agent_rueckfragen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Offene Rückfragen der Agenten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/baukasten/agent_rueckfragen``
        """
        return self._platform.call("baukasten", "agent_rueckfragen", {**(params or {}), **kwargs})

    def agent_anhalten(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Lauf anhalten

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/agent_anhalten``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``lauf_id`` (int, Pflicht): ID des Laufs als ganze Zahl. Du bekommst sie aus der Antwort von `agent_starten` (Feld `lauf_id`) oder aus `agent_rueckfragen` (Feld `lauf_id`). Eingreifen darf die Person, die den Lauf gestartet hat, sowie die Verwalte…
        """
        return self._platform.call("baukasten", "agent_anhalten", {**(params or {}), **kwargs})

    def agent_fortsetzen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Lauf fortsetzen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/agent_fortsetzen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``lauf_id`` (int, Pflicht): ID des Laufs als ganze Zahl. Du bekommst sie aus der Antwort von `agent_starten` (Feld `lauf_id`) oder aus `agent_rueckfragen` (Feld `lauf_id`). Eingreifen darf die Person, die den Lauf gestartet hat, sowie die Verwalte…
        """
        return self._platform.call("baukasten", "agent_fortsetzen", {**(params or {}), **kwargs})

    def agent_pausieren(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Pausiert einen Agenten ganz: er startet nicht mehr von selbst (Zeitplan, Ereignisse), bis er wieder eingeschal

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/agent_pausieren``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``agent_id`` (int): ID des Agenten
        - ``name`` (str): Name oder Teil des Namens, wenn die ID nicht bekannt ist
        """
        return self._platform.call("baukasten", "agent_pausieren", {**(params or {}), **kwargs})

    def agent_aktivieren(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Schaltet einen pausierten Agenten wieder ein.

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/baukasten/agent_aktivieren``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``agent_id`` (int): ID des Agenten
        - ``name`` (str): Name oder Teil des Namens, wenn die ID nicht bekannt ist
        """
        return self._platform.call("baukasten", "agent_aktivieren", {**(params or {}), **kwargs})


class AgentTeamsArea(_Area):
    """Agent-Teams — Agent-Teams fassen mehrere Chat-Agenten und Avatare zu einer Gruppe mit gemeinsamem Ziel und festen Rollen zusammen."""

    def list_teams(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Agent-Teams auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/agent_teams/list_teams``
        """
        return self._platform.call("agent_teams", "list_teams", {**(params or {}), **kwargs})

    def create_team(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Agent-Team anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/agent_teams/create_team``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``name`` (str, Pflicht): Name des Teams, z. B. „Angebots-Taskforce“. Pflichtfeld. Der Text wird getrimmt und HTML-bereinigt gespeichert.
        - ``team_type`` (str): Typ des Teams. Die Klasse kennt `optimization`, `implementation`, `process`, `strategy` und `custom`. Ohne Angabe wird `custom` verwendet. Nutze nur diese Werte.
        - ``goal`` (str): Ziel des Teams in einem oder zwei Sätzen, z. B. „Angebote in unter 24 Stunden versenden“. Wird als `teamGoal` gespeichert und im Team-Chat als Ausgangspunkt benutzt. Ohne Angabe bleibt das Ziel leer.
        - ``members`` (list): Mitglieder als Liste von Objekten, z. B. `{"chatAgentId": 1201, "teamRole": "Texter", "roleDescription": "Formuliert den Angebotstext"}`. `chatAgentId` verweist auf einen Chat-Agenten, `avatarId` auf einen Avatar, `team…
        """
        return self._platform.call("agent_teams", "create_team", {**(params or {}), **kwargs})


class ReflectionsArea(_Area):
    """Reflexionen und Benachrichtigungen — Der Bereich hat zwei Teile."""

    def get_reflections(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Reflexionen auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/reflections/get_reflections``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``status`` (str): Optional: exakter Status als Text, z. B. `pending`, `ready`, `in_progress` oder `completed`. Es wird exakt verglichen; ohne Angabe kommen alle Status.
        - ``emotion`` (str): Optional: exakte Emotion als Text, z. B. `frustration` oder `neutral`. Gefiltert wird auf Gleichheit.
        - ``urgency_min`` (int): Optional: Mindest-Dringlichkeit als ganze Zahl. Beachte, dass die Dringlichkeit intern zwischen 0 und 1 liegt; praktisch wirkt nur 1 (nur Höchstwerte), 0 deaktiviert den Filter.
        - ``search`` (str): Optional: Suchtext, der als Teilstring in Titel oder Beschreibung gesucht wird. Der Text wird HTML-escaped und getrimmt.
        - ``include_private`` (bool): Optional (Wahrheitswert, Standard `false`). Mit `true` kommen auch als privat markierte Reflexionen zurück (soweit sie dir gehören); ohne Angabe nur nicht private.
        - ``limit`` (int): Optional: Höchstzahl der Reflexionen in der Antwort (ganze Zahl, Standard 25, mindestens 1). Eine Obergrenze erzwingt der Code nicht.
        - ``offset`` (int): Optional: Anzahl der Reflexionen, die am Anfang übersprungen werden (ganze Zahl, Standard 0). Mit `limit` blätterst du seitenweise.
        """
        return self._platform.call("reflections", "get_reflections", {**(params or {}), **kwargs})

    def get_notifications(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Benachrichtigungen auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/reflections/get_notifications``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``nur_ungelesen`` (bool): Optional (Wahrheitswert, Standard `false`). Mit `true` werden nur ungelesene Benachrichtigungen geliefert, ebenfalls begrenzt durch `limit`.
        - ``limit`` (int): Optional: Höchstzahl der Einträge (ganze Zahl, Standard 20). Werte unter 1 werden zu 1, Werte über 100 zu 100.
        """
        return self._platform.call("reflections", "get_notifications", {**(params or {}), **kwargs})

    def get_notification_count(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Ungelesene Benachrichtigungen zählen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/reflections/get_notification_count``
        """
        return self._platform.call("reflections", "get_notification_count", {**(params or {}), **kwargs})

    def mark_notification_read(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Benachrichtigung als gelesen markieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/reflections/mark_notification_read``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``notification_id`` (int): Optional: Datenbank-ID der Benachrichtigung (ganze Zahl), wie sie in `get_notifications` unter `notifications[].id` steht. Ohne diese Angabe musst du `alle` setzen.
        - ``alle`` (bool): Optional (Wahrheitswert): mit `true` werden alle ungelesenen Benachrichtigungen der Person als gelesen markiert, `notification_id` wird dann nicht beachtet.
        """
        return self._platform.call("reflections", "mark_notification_read", {**(params or {}), **kwargs})

    def create_notification(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Benachrichtigung anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/reflections/create_notification``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``titel`` (str, Pflicht): Kurze Überschrift der Benachrichtigung (Text, Pflichtangabe). Sie wird getrimmt und HTML-escaped.
        - ``nachricht`` (str, Pflicht): Fließtext der Benachrichtigung (Pflichtangabe). Er wird getrimmt und HTML-escaped gespeichert.
        - ``typ`` (str): Optional: technischer Typ als Text, z. B. `crm_lead`. Standard ist `external`. Der Typ dient der Einordnung in der Oberfläche.
        - ``icon`` (str): Optional: Symbolname als Text, z. B. `bell`, `phone`, `mail` oder `calendar`. Standard ist `bell`.
        - ``link`` (str): Optional: Ziel beim Anklicken als interner Pfad, z. B. `/crm`. Ohne Angabe ist die Meldung nicht anklickbar.
        """
        return self._platform.call("reflections", "create_notification", {**(params or {}), **kwargs})

    def delete_notification(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Benachrichtigung löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/reflections/delete_notification``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``notification_id`` (int, Pflicht): Datenbank-ID der zu löschenden Benachrichtigung (ganze Zahl, Pflichtangabe), wie sie in `get_notifications` unter `notifications[].id` steht.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("reflections", "delete_notification", {**(params or {}), **kwargs}, confirmed=confirmed)

    def get_reflection(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Reflexion im Detail abrufen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/reflections/get_reflection``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``reflection_id`` (int, Pflicht): ID der Reflexion (ganze Zahl, Pflichtangabe), wie sie in `get_reflections` unter `items[].id` steht. Eine unbekannte ID führt zu `Reflexion nicht gefunden`.
        """
        return self._platform.call("reflections", "get_reflection", {**(params or {}), **kwargs})

    def create_reflection(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Reflexion anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/reflections/create_reflection``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``title`` (str, Pflicht): Kurzer Titel der Reflexion (Pflichtangabe). Er dient auch als Grundlage für den Objektschlüssel.
        - ``core_insight`` (str, Pflicht): Die Kernerkenntnis in ein bis drei Sätzen (Pflichtangabe). Sie wird als Beschreibung der Reflexion gespeichert, sofern du nicht zusätzlich `description` angibst.
        - ``raw_input`` (str): Optional: Originaltranskript oder Notizen, aus denen die Erkenntnis stammt. Wird in den Zusatzdaten der Reflexion abgelegt.
        - ``description`` (str): Optional: ausführlichere Beschreibung oder Kontext. Überschreibt die aus `core_insight` übernommene Beschreibung.
        - ``emotion`` (str): Optional: Emotion als Text, z. B. `frustration`. Standard ist `neutral`.
        - ``urgency`` (int): Optional: Bewertung 0 bis 10 (ganze Zahl, Standard 5). Der Wert wird beim Anlegen auf eine Skala von 0 bis 1 umgerechnet. Beachte den Hinweis zur doppelten Verarbeitung.
        - ``status`` (str): Optional: Status als Text. Beim Anlegen steht er auf `pending`; ein hier angegebener Wert überschreibt ihn danach (z. B. `ready` oder `completed`).
        - ``theme`` (str): Optional: Thema oder Kategorie der Reflexion als Text, z. B. `Prozesse`.
        - ``is_private`` (bool): Optional (Wahrheitswert): markiert die Reflexion als privat. Private Reflexionen erscheinen in `get_reflections` nur mit `include_private`.
        - ``needs_follow_up`` (bool): Optional (Wahrheitswert): kennzeichnet, dass eine Nachverfolgung nötig ist.
        - ``source_type`` (str): Optional: Quelle der Erkenntnis, z. B. `voice_chat`, `note` oder `meeting`. Standard ist `assistant`.
        - ``source_id`` (int): Optional: ID des Ursprungs (ganze Zahl), z. B. eines Gesprächs. Wird in den Zusatzdaten der Reflexion gespeichert.
        - ``potential_action`` (str): Optional: empfohlene Handlung als Text.
        - ``root_cause`` (str): Optional: vermutete Ursache als Text.
        """
        return self._platform.call("reflections", "create_reflection", {**(params or {}), **kwargs})

    def update_reflection(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Reflexion aktualisieren

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/reflections/update_reflection``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``reflection_id`` (int, Pflicht): ID der Reflexion (ganze Zahl, Pflichtangabe), wie sie in `get_reflections` unter `items[].id` steht.
        - ``data`` (dict, Pflicht): Objekt mit den Feldern, die geändert werden sollen, z. B. `{"status": "completed", "measured_impact": "Freigabezeit von 2 auf 1 Tag gesunken"}`. Erlaubt sind die oben genannten Schlüssel; Wahrheitswerte für `is_private`…
        """
        return self._platform.call("reflections", "update_reflection", {**(params or {}), **kwargs})

    def delete_reflection(self, params: Optional[Mapping[str, Any]] = None, *, confirmed: bool = False, **kwargs: Any) -> Dict[str, Any]:
        """Reflexion löschen

        Recht am Schlüssel: ``loeschen`` · ``POST /platform/reflections/delete_reflection``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``reflection_id`` (int, Pflicht): ID der zu löschenden Reflexion (ganze Zahl, Pflichtangabe), wie sie in `get_reflections` unter `items[].id` steht.
        - ``bestaetigt`` (bool, Pflicht): Muss `true` sein, damit die Aktion ausgeführt wird. Ohne Bestätigung antwortet die Schnittstelle mit `409` und führt nichts aus.

        ``confirmed=True`` bestätigt die Aktion (sendet ``bestaetigt: true``).
        """
        return self._platform.call("reflections", "delete_reflection", {**(params or {}), **kwargs}, confirmed=confirmed)

    def get_reflection_statistics(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Statistik der Reflexionen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/reflections/get_reflection_statistics``
        """
        return self._platform.call("reflections", "get_reflection_statistics", {**(params or {}), **kwargs})


class VerbindungenArea(_Area):
    """E-Mail-Vorlagen und Webhooks — Dieser Bereich verbindet deine Abläufe mit E-Mail, Webhooks und Dateien."""

    def list_email_vorlagen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """E-Mail-Vorlagen auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/verbindungen/list_email_vorlagen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``suche`` (str): Optionales Stichwort. Es bleiben Vorlagen, in deren Namen oder Betreff das Wort vorkommt (Groß-/Kleinschreibung egal). Ohne Angabe kommen alle Vorlagen.
        """
        return self._platform.call("verbindungen", "list_email_vorlagen", {**(params or {}), **kwargs})

    def preview_email_vorlage(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """E-Mail-Vorlage als Vorschau füllen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/verbindungen/preview_email_vorlage``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``vorlage_id`` (int, Pflicht): ID der Vorlage aus `list_email_vorlagen`. Pflicht. Die Vorlage muss dir gehören oder für alle Firmen gelten.
        - ``lead_id`` (int): Optional: ID eines Leads deiner Firma. Dessen Daten füllen die `{lead.…}`-Platzhalter und `an`. Ohne Angabe werden Beispieldaten genutzt.
        - ``werte`` (dict): Optionales Objekt mit eigenen Werten für `{wert.name}` in Betreff und Text, zum Beispiel `{"termin": "Dienstag, 10. November, 14 Uhr"}`. Einfache Werte werden als Text eingesetzt, Listen und Objekte als JSON.
        """
        return self._platform.call("verbindungen", "preview_email_vorlage", {**(params or {}), **kwargs})

    def create_email_vorlage(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """E-Mail-Vorlage anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/verbindungen/create_email_vorlage``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``name`` (str, Pflicht): Anzeigename der Vorlage, höchstens 120 Zeichen. Pflicht. Er erscheint in den Auswahllisten des Dashboards.
        - ``betreff`` (str, Pflicht): Betreffzeile der Mail. Pflicht. Platzhalter wie `{lead.lastname}` und eigene Werte `{wert.name}` sind erlaubt.
        - ``text`` (str, Pflicht): Text der Mail. Pflicht. Platzhalter: `{lead.gruss}`, `{lead.anrede}`, `{lead.firstname}`, `{lead.lastname}`, `{lead.company}`, `{company.company}`, `{member.name}`, `{system.date}`; eigene Werte als `{wert.name}`; Bedin…
        - ``typ`` (str): Verwendungszweck der Vorlage: `general` (Allgemein), `callback` (Rückruf) oder `followup` (Follow-up). Standard ist `general`.
        """
        return self._platform.call("verbindungen", "create_email_vorlage", {**(params or {}), **kwargs})

    def update_email_vorlage(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """E-Mail-Vorlage ändern

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/verbindungen/update_email_vorlage``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``vorlage_id`` (int, Pflicht): ID der eigenen Vorlage aus `list_email_vorlagen`. Pflicht. Vorlagen anderer Firmen werden als nicht vorhanden gemeldet.
        - ``name`` (str): Neuer Anzeigename, höchstens 120 Zeichen. Ein leerer Wert lässt den Namen unverändert.
        - ``betreff`` (str): Neue Betreffzeile. Platzhalter und `{wert.name}` sind erlaubt. Wird sie weggelassen, bleibt der bisherige Betreff.
        - ``text`` (str): Neuer Mailtext mit denselben Platzhaltern und Bedingungen wie bei `create_email_vorlage`. Wird er weggelassen, bleibt der bisherige Text.
        - ``aktiv`` (bool): `true` schaltet die Vorlage ein, `false` aus. Ohne Angabe bleibt der Zustand unverändert.
        """
        return self._platform.call("verbindungen", "update_email_vorlage", {**(params or {}), **kwargs})

    def list_webhook_ziele(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Webhook-Ziele auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/verbindungen/list_webhook_ziele``
        """
        return self._platform.call("verbindungen", "list_webhook_ziele", {**(params or {}), **kwargs})

    def create_datei(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Datei erzeugen und ablegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/verbindungen/create_datei``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``format`` (str, Pflicht): Dateiformat: `docx`, `xlsx`, `csv`, `json`, `md` oder `txt`. Pflicht. Das Format bestimmt, wie `inhalt` gelesen wird.
        - ``name`` (str, Pflicht): Dateiname ohne Endung, zum Beispiel `Leads Oktober`. Pflicht. Sonderzeichen wie `/ \\ : * ? " < > |` werden durch Leerzeichen ersetzt; die Endung ergänzt die Funktion.
        - ``inhalt`` (Any, Pflicht): Der Inhalt. Bei `txt`, `md`, `docx` ein Text (in `docx` bedeuten `# Überschrift` eine Überschrift, `- Punkt` eine Liste, eine Leerzeile einen neuen Absatz). Bei `csv`, `xlsx` eine Liste von Zeilen: Objekte ergeben Spalt…
        """
        return self._platform.call("verbindungen", "create_datei", {**(params or {}), **kwargs})


class KundensupportArea(_Area):
    """Kundensupport — Der Kundensupport führt Kundennachrichten, Kommentare unter Postings, eure Antworten und die Postings selbst aus E-Mail und Social-Media-Kanälen zusammen."""

    def kundensupport_suche(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Kundensupport nach Themen durchsuchen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/kundensupport/kundensupport_suche``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``frage`` (str, Pflicht): Wonach gesucht wird, in eigenen Worten, zum Beispiel `Kommentare zur Lieferzeit`. Pflicht. Ein leerer Text liefert den Fehler „Wonach soll ich suchen?“.
        - ``art`` (str): Optional: `beitrag` (nur Postings), `nachricht` (nur Kundennachrichten und Kommentare) oder `antwort` (nur eure Antworten). Ohne Angabe wird alles durchsucht.
        - ``kanal`` (str): Optional: nur ein Kanal, angegeben als Kanalart wie `email`, `instagram`, `linkedin`, `amazon` oder als Name eines Kanals deiner Firma. Gibt es den Kanal nicht, kommt keine Trefferliste.
        """
        return self._platform.call("kundensupport", "kundensupport_suche", {**(params or {}), **kwargs})

    def kundensupport_muster(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Wiederkehrende Muster finden

        Recht am Schlüssel: ``lesen`` · ``POST /platform/kundensupport/kundensupport_muster``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``frage`` (str, Pflicht): Thema, zu dem Muster gesucht werden, zum Beispiel `Fragen unter Postings zum Preis`. Pflicht. Ein leerer Text liefert den Fehler „Zu welchem Thema soll ich Muster suchen?“.
        - ``tage`` (int): Zeitraum in Tagen, den die Nachrichten höchstens zurückliegen dürfen. Ganze Zahl von 1 bis 730, Standard 90. Werte außerhalb werden auf diesen Bereich begrenzt.
        """
        return self._platform.call("kundensupport", "kundensupport_muster", {**(params or {}), **kwargs})


class BuchhaltungArea(_Area):
    """Rechnungen lesen — Dieser Bereich liest die Rechnungen deiner Firma aus der Buchhaltung, ohne etwas zu verändern."""

    def offene_rechnungen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Offene Rechnungen auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/buchhaltung/offene_rechnungen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``limit`` (int): Wie viele Rechnungen die Liste höchstens enthält. Ganze Zahl von 1 bis 50, Standard 10. Werte außerhalb werden auf diesen Bereich begrenzt.
        """
        return self._platform.call("buchhaltung", "offene_rechnungen", {**(params or {}), **kwargs})

    def rechnung_lesen(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Rechnung anhand der Nummer lesen

        Recht am Schlüssel: ``lesen`` · ``POST /platform/buchhaltung/rechnung_lesen``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``nummer`` (str, Pflicht): Rechnungsnummer genau so, wie sie auf der Rechnung steht, zum Beispiel `RE-2026-0142`. Pflicht. Führende und nachfolgende Leerzeichen werden entfernt, sonst wird exakt verglichen.
        """
        return self._platform.call("buchhaltung", "rechnung_lesen", {**(params or {}), **kwargs})


class ToniCallArea(_Area):
    """Telefon-Agenten — Toni Call lässt Agenten deiner Firma telefonieren, eingehend und ausgehend, über ein eigenes Telefonkonto oder eine Nebenstelle der Firma."""

    def list_telefon_agenten(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Telefon-Agenten auflisten

        Recht am Schlüssel: ``lesen`` · ``POST /platform/toni_call/list_telefon_agenten``
        """
        return self._platform.call("toni_call", "list_telefon_agenten", {**(params or {}), **kwargs})


class QuoteArea(_Area):
    """Angebote und Rechnungsentwürfe — Dieser Bereich legt Entwürfe in der Buchhaltung deiner Firma an."""

    def create_invoice_draft(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Rechnungsentwurf anlegen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/quote/create_invoice_draft``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``lead_id`` (int, Pflicht): ID des Leads (Kunden) in deinem CRM. Pflicht. Der Lead liefert Name, Anschrift und E-Mail für den Rechnungsempfänger.
        - ``positionen`` (list, Pflicht): Liste der Rechnungspositionen. Jede Position ist ein Objekt mit `titel` (Text, Pflicht), `menge` (Zahl, Standard 1), `preis_netto` (Einzelpreis netto in Euro), `steuersatz` (Prozent, zum Beispiel 19 oder 7, Standard 19)…
        - ``betreff`` (str): Optionaler Betreff der Rechnung, höchstens 200 Zeichen. Ohne Angabe bleibt er leer.
        - ``leistungszeitraum_von`` (str): Optional: Beginn des Leistungszeitraums im Format `JJJJ-MM-TT`, zum Beispiel `2026-10-01`. Andere Formate werden ignoriert.
        - ``leistungszeitraum_bis`` (str): Optional: Ende des Leistungszeitraums im Format `JJJJ-MM-TT`, zum Beispiel `2026-10-31`. Andere Formate werden ignoriert.
        """
        return self._platform.call("quote", "create_invoice_draft", {**(params or {}), **kwargs})

    def draft_quote(self, params: Optional[Mapping[str, Any]] = None, **kwargs: Any) -> Dict[str, Any]:
        """Angebotsentwurf aus Gesprächen erstellen

        Recht am Schlüssel: ``schreiben`` · ``POST /platform/quote/draft_quote``

        Parameter (als ``params``-Dict oder Schlüsselwort):

        - ``briefing`` (str, Pflicht): Kurze Beschreibung dessen, was das Angebot enthalten oder berücksichtigen soll, zum Beispiel Umfang, Standorte, Starttermin. Pflicht. Das Briefing steht an erster Stelle der Grundlage und genügt auch, wenn es sonst kein…
        - ``lead_id`` (int): ID des Leads (Kunden) deiner Firma, falls bekannt. Eine fremde oder unbekannte ID gilt als nicht gefunden; ist zusätzlich `company_name` gesetzt, wird damit weitergesucht.
        - ``company_name`` (str): Firmenname des Kunden, falls die `lead_id` nicht bekannt ist; mindestens 2 Zeichen. Ein genauer Treffer (Groß-/Kleinschreibung egal) gewinnt gegen mehrere Teiltreffer, mehrere Teiltreffer ohne genauen Treffer sind mehrd…
        """
        return self._platform.call("quote", "draft_quote", {**(params or {}), **kwargs})


#: Bereichsname → Klasse
AREAS: Dict[str, Type[_Area]] = {
    "books": BooksArea,
    "audiobooks": AudiobooksArea,
    "podcasts": PodcastsArea,
    "podcast_guests": PodcastGuestsArea,
    "stories": StoriesArea,
    "landingpages": LandingpagesArea,
    "landingcards": LandingcardsArea,
    "qrcodes": QrcodesArea,
    "testimonials": TestimonialsArea,
    "offers": OffersArea,
    "expertise": ExpertiseArea,
    "glossary": GlossaryArea,
    "handbook": HandbookArea,
    "speechanalysis": SpeechanalysisArea,
    "interviews": InterviewsArea,
    "academy": AcademyArea,
    "campaigns": CampaignsArea,
    "crm": CrmArea,
    "arango": ArangoArea,
    "business_model": BusinessModelArea,
    "products": ProductsArea,
    "sparring": SparringArea,
    "baukasten": BaukastenArea,
    "agent_teams": AgentTeamsArea,
    "reflections": ReflectionsArea,
    "verbindungen": VerbindungenArea,
    "kundensupport": KundensupportArea,
    "buchhaltung": BuchhaltungArea,
    "toni_call": ToniCallArea,
    "quote": QuoteArea,
}


class AreaAccess:
    """Die Bereiche der Plattform als Eigenschaften des Clients."""

    def _area(self, name: str) -> Any:  # vom Client überschrieben
        raise NotImplementedError

    @property
    def books(self) -> BooksArea:
        """Bücher"""
        return self._area("books")

    @property
    def audiobooks(self) -> AudiobooksArea:
        """Hörbücher"""
        return self._area("audiobooks")

    @property
    def podcasts(self) -> PodcastsArea:
        """Podcasts"""
        return self._area("podcasts")

    @property
    def podcast_guests(self) -> PodcastGuestsArea:
        """Podcast-Gäste"""
        return self._area("podcast_guests")

    @property
    def stories(self) -> StoriesArea:
        """Magazin und Storyfilter"""
        return self._area("stories")

    @property
    def landingpages(self) -> LandingpagesArea:
        """Landingpages"""
        return self._area("landingpages")

    @property
    def landingcards(self) -> LandingcardsArea:
        """Landingcards"""
        return self._area("landingcards")

    @property
    def qrcodes(self) -> QrcodesArea:
        """QR-Codes"""
        return self._area("qrcodes")

    @property
    def testimonials(self) -> TestimonialsArea:
        """Kundenstimmen"""
        return self._area("testimonials")

    @property
    def offers(self) -> OffersArea:
        """Angebote im Katalog"""
        return self._area("offers")

    @property
    def expertise(self) -> ExpertiseArea:
        """Expertise"""
        return self._area("expertise")

    @property
    def glossary(self) -> GlossaryArea:
        """Glossar"""
        return self._area("glossary")

    @property
    def handbook(self) -> HandbookArea:
        """Handbuch"""
        return self._area("handbook")

    @property
    def speechanalysis(self) -> SpeechanalysisArea:
        """Sprachprofile"""
        return self._area("speechanalysis")

    @property
    def interviews(self) -> InterviewsArea:
        """Interviews"""
        return self._area("interviews")

    @property
    def academy(self) -> AcademyArea:
        """Akademie"""
        return self._area("academy")

    @property
    def campaigns(self) -> CampaignsArea:
        """Werbekampagnen"""
        return self._area("campaigns")

    @property
    def crm(self) -> CrmArea:
        """CRM"""
        return self._area("crm")

    @property
    def arango(self) -> ArangoArea:
        """Wissensgraph"""
        return self._area("arango")

    @property
    def business_model(self) -> BusinessModelArea:
        """Geschäftsmodell"""
        return self._area("business_model")

    @property
    def products(self) -> ProductsArea:
        """Produkte"""
        return self._area("products")

    @property
    def sparring(self) -> SparringArea:
        """Content-Ideen"""
        return self._area("sparring")

    @property
    def baukasten(self) -> BaukastenArea:
        """Agenten und Anwendungen"""
        return self._area("baukasten")

    @property
    def agent_teams(self) -> AgentTeamsArea:
        """Agent-Teams"""
        return self._area("agent_teams")

    @property
    def reflections(self) -> ReflectionsArea:
        """Reflexionen und Benachrichtigungen"""
        return self._area("reflections")

    @property
    def verbindungen(self) -> VerbindungenArea:
        """E-Mail-Vorlagen und Webhooks"""
        return self._area("verbindungen")

    @property
    def kundensupport(self) -> KundensupportArea:
        """Kundensupport"""
        return self._area("kundensupport")

    @property
    def buchhaltung(self) -> BuchhaltungArea:
        """Rechnungen lesen"""
        return self._area("buchhaltung")

    @property
    def toni_call(self) -> ToniCallArea:
        """Telefon-Agenten"""
        return self._area("toni_call")

    @property
    def quote(self) -> QuoteArea:
        """Angebote und Rechnungsentwürfe"""
        return self._area("quote")
