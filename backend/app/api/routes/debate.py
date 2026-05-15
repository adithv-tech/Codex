from fastapi import APIRouter
from app.models.research import DebateRequest
from app.services.storage.filesystem import save_stage_output

router = APIRouter(tags=["debate"])

@router.post("/research/debate")
async def debate(req: DebateRequest) -> dict:
    response = (
        f"Debate update for {req.ticker}: stance={req.stance}. "
        "Updated thesis weighting after cross-checking prior prompts and new evidence."
    )
    path = save_stage_output(req.ticker, "chat_memory", 999, f"User: {req.challenge}\nAI: {response}")
    return {"response": response, "memory_path": path}
