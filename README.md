# Autonomous Stock Research OS

Full-stack AI-powered stock research platform scaffold with:
- **Frontend**: Next.js + TypeScript + Tailwind + shadcn/ui-ready structure
- **Backend**: FastAPI orchestration engine, multi-agent analysis pipeline, and persistent research thread model
- **Data layer**: PostgreSQL + Redis + Vector DB interface-ready abstractions

## Core Capabilities Implemented

- Sequential, stage-based institutional stock analysis prompt pipeline (27 prompts)
- Persistent research thread per ticker with memory and thesis evolution
- Structured storage for outputs under `/stocks/[ticker]/...`
- Live event streaming support for dashboards
- Debate endpoint to ingest user-uploaded evidence and revise thesis
- Multi-agent system with shared thread context

## Monorepo Layout

- `frontend/` Next.js app scaffold + dashboard UI skeleton
- `backend/` FastAPI services and orchestration engine
- `infra/` deployment-oriented placeholders

## Quick Start

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

