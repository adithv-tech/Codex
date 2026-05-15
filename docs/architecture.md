# AI-Powered Stock Research Platform Architecture

## Stack
- Frontend: Next.js + TypeScript + Tailwind + shadcn/ui (planned)
- Backend: FastAPI + Python services
- Data: PostgreSQL + Redis + Vector DB (planned integration)

## Prompt Orchestration Engine
- Sequentially executes 27 institutional prompts.
- Preserves thread-level memory by ticker.
- Persists each prompt result under `/stocks/[ticker]/...` folder tree.
- Supports follow-up debate endpoint for thesis revision.

## Specialized Agents
- Foundation Research Agent
- Valuation Agent
- Competitor Agent
- SEC Filing Agent
- Bear Thesis Agent
- Technical Analysis Agent
- Sentiment Agent
- Macro Agent
- Final Verdict Agent

## Data Sources Adapters (to implement)
- SEC EDGAR, Yahoo Finance, Alpha Vantage, Polygon, Finnhub
- MarketWatch, Macrotrends, Fintel, TradingView, Reddit, Stocktwits

## Storage Layout
`/stocks/[ticker]/research_foundation ... /chat_memory` and all stage-specific subfolders.

## Next Steps
1. Add async job queue (Redis/Celery or Dramatiq)
2. Add SSE/WebSockets for live dashboard streaming
3. Implement provider clients with strict source-citation schema
4. Add RAG memory and thesis-evolution snapshots
5. Add auth, tenant isolation, and production DB models
