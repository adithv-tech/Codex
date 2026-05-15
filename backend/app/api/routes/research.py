import json
from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.models.research import ResearchRequest
from app.services.orchestrator.engine import PromptOrchestrator

router = APIRouter(tags=["research"])
engine = PromptOrchestrator()

@router.post("/research/start")
async def start_research(request: ResearchRequest) -> StreamingResponse:
    async def event_stream():
        async for result in engine.run(request.ticker):
            yield f"data: {json.dumps(result.model_dump())}\n\n"
    return StreamingResponse(event_stream(), media_type="text/event-stream")
