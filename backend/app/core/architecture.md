# AI Agent and Orchestration Design

## Agents (Shared Memory)

- Foundation Research Agent
- Valuation Agent
- Competitor Agent
- SEC Filing Agent
- Bear Thesis Agent
- Technical Analysis Agent
- Sentiment Agent
- Macro Agent
- Final Verdict Agent

All agents read/write the same thread memory object and emit stage events.

## Data Connectors

Intended integrations:
- SEC EDGAR
- Yahoo Finance
- Alpha Vantage
- Polygon
- Finnhub
- MarketWatch
- Macrotrends
- Fintel
- TradingView
- Reddit APIs
- Stocktwits

## Storage Model

- PostgreSQL for entities and report metadata
- Redis for job queues, distributed locks, event streaming
- Vector DB for memory and RAG retrieval over filings/uploads/debate artifacts
- File storage path: `/stocks/[ticker]/...` for generated artifacts and uploads

## Hallucination Controls

- Source-required responses for each prompt output
- Numeric calculation trace with formulas attached
- Cross-stage consistency checks before final verdict
- Red-team pass mandatory before rating emission
