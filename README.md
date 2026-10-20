# Agent App (FastAPI + Streamlit)

Minimal scaffold for a beginner agentic app: FastAPI backend and Streamlit frontend. No LLM logic yet.

## Setup

From the project root (`playCursorAI`):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

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

Open the URL Streamlit prints (usually [http://localhost:8501](http://localhost:8501)).

### Try health

In the sidebar, click **Check API health**. You should see `status: ok`.

### Try chat

Type a message in the chat box (for example `hello`). The API echoes back `You said: hello`. No LLM yet — that comes in a later step.

## Layout

```text
backend/          FastAPI app (+ agent/ placeholder for later)
frontend/         Streamlit UI
requirements.txt  Dependencies
.env.example      Template for secrets (copy to .env later)
```
