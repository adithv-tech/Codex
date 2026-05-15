from fastapi import APIRouter, BackgroundTasks
from app.schemas.research import (
    DebateInput,
    ResearchRunRequest,
    ResearchThreadResponse,
)
from app.services.orchestrator import orchestrator

router = APIRouter()


@router.post("/research/start", response_model=ResearchThreadResponse)
def start_research(payload: ResearchRunRequest, background_tasks: BackgroundTasks) -> ResearchThreadResponse:
    thread = orchestrator.create_thread(payload.ticker)
    background_tasks.add_task(orchestrator.run_full_pipeline, thread.thread_id)
    return thread


@router.post("/research/{thread_id}/debate")
def debate(thread_id: str, payload: DebateInput) -> dict[str, str]:
    orchestrator.process_debate_input(thread_id=thread_id, debate_input=payload)
    return {"status": "accepted", "thread_id": thread_id}
