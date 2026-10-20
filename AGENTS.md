# Agent conventions — playCursorAI

Short rules for Cursor (and humans) working on this repo.

## Stack

- Python, FastAPI (`backend/`), Streamlit (`frontend/`), Groq LLM

## Layout

- `backend/main.py` — HTTP API (`/`, `/health`, `/chat`)
- `backend/agent/llm.py` — Groq calls only; do **not** call Groq from Streamlit
- `frontend/app.py` — UI only; talk to the API with httpx

## Secrets

- Put `GROQ_API_KEY` in `.env` (never commit `.env`)
- Use `.env.example` as the template only

## Workflow in Cursor

- **Ask** — explain / review (no edits)
- **Plan** then **Agent** — prefer this for multi-file changes
- Do not commit secrets or paste API keys into chat

## Out of scope (for now)

- Tool-calling agents
- Multi-turn conversation memory on the server
