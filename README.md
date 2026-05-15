# Institutional Stock Research OS

Full-stack autonomous stock research platform with sequential prompt orchestration.

## Highlights
- 27-prompt staged orchestration engine.
- Persistent per-ticker folder memory under `/stocks/[ticker]/...`.
- SSE live streaming from FastAPI to dashboard.
- Debate endpoint for thesis revision with memory persistence.
- Agent map: Foundation, Valuation, Competitor, SEC Filing, Bear Thesis, Technical, Sentiment, Macro, Final Verdict.

## Run
```bash
docker compose up --build
```

API: `POST /api/v1/research/start` with `{ "ticker": "NVDA" }`.
