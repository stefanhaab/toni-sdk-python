"""Antwort Stück für Stück. Start: TONI_API_KEY=km_live_… python3 examples/chat_stream.py"""
from toni_sdk import Toni

for stueck in Toni().stream("Erklär in drei Sätzen, was ein Voicebot ist."):
    print(stueck, end="", flush=True)
print()
