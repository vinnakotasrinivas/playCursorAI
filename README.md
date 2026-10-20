# Agent App (FastAPI + Streamlit)

Beginner agentic app: FastAPI backend (Groq LLM) and Streamlit chat UI.

## Setup

From the project root (`playCursorAI`):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set your free Groq key from [console.groq.com/keys](https://console.groq.com/keys):

```text
GROQ_API_KEY=your_key_here
```

Never commit `.env`.

## Run

Use two terminals (both with the venv activated, from the project root).

**Terminal A — API**

```powershell
uvicorn backend.main:app --reload --port 8000
```

Health check: [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health)

**Terminal B — UI**

```powershell
streamlit run frontend/app.py
```

Or use **Run and Debug → Debug Full Stack (both)** in Cursor for breakpoints.

Open the URL Streamlit prints (usually [http://localhost:8501](http://localhost:8501)).

### Try health

In the sidebar, click **Check API health**. You should see `status: ok`.

### Try chat

Type a message in the chat box. The backend calls Groq (`qwen/qwen3.8-27b`) and returns a model reply (not an echo).

## Layout

```text
backend/          FastAPI app + agent/llm.py (Groq)
frontend/         Streamlit UI
requirements.txt  Dependencies
.env.example      Template for GROQ_API_KEY (copy to .env)
```

See `AGENTS.md` for Cursor/agent project conventions.
