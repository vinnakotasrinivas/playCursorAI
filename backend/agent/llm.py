import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(_ROOT / ".env")

# Groq free-tier model IDs change over time; this one is available on current accounts.
MODEL = "qwen/qwen3.8-27b"


def get_reply(message: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Copy .env.example to .env and add your key."
        )
    client = Groq(api_key=api_key)
    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant for a beginner agentic app tutorial.",
            },
            {"role": "user", "content": message},
        ],
    )
    return completion.choices[0].message.content or ""
