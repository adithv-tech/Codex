from fastapi import APIRouter
from app.schemas.research import StartResearchRequest, DebateRequest, DebateResponse
from app.services.orchestrator import PromptOrchestrator

router = APIRouter()
orchestrator = PromptOrchestrator()

@router.post("/research/start")
def start_research(payload: StartResearchRequest):
    results = orchestrator.run_research(payload.ticker)
    return {"ticker": payload.ticker.upper(), "results": [r.model_dump() for r in results]}

@router.post("/research/debate", response_model=DebateResponse)
def debate(payload: DebateRequest):
    return DebateResponse(
        revised_thesis="Thesis revised with uploaded evidence and counterarguments.",
        what_changed=["Risk weighting updated for competitive threat", "Valuation confidence reduced"],
        risk_weighting_delta={"execution_risk": 0.1, "valuation_risk": 0.15, "macro_risk": -0.05},
    )
