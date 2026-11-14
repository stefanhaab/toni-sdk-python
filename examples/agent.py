"""Ein Agent, der im CRM liest. Start: TONI_API_KEY=km_live_… python3 examples/agent.py"""
from toni_sdk import Toni

toni = Toni()
agent = toni.agent(areas=["crm"], on_step=lambda s: print("→", s.tool, s.args))
print(agent.run("Wer hat sich diese Woche gemeldet, und wer wartet noch auf Antwort?").text)
