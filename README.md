# Autonomous Hedge-Fund Style Stock Research OS (Scaffold)

This repo now includes a full-stack scaffold for a multi-stage AI stock research platform with a sequential prompt orchestration backend.

## Run backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## Run frontend
Create a Next.js app wrapper and mount `frontend/src` (scaffolded UI landing view included).

## API
- `POST /api/research/start` with `{ "ticker": "NVDA" }`
- `POST /api/research/debate` with thesis challenge payload
