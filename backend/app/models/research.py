from pydantic import BaseModel, Field
from typing import Literal

class ResearchRequest(BaseModel):
    ticker: str = Field(min_length=1, max_length=10)

class StageResult(BaseModel):
    stage: int
    prompt_id: int
    agent: str
    output_path: str
    status: Literal["queued", "running", "completed", "failed"]
    content: str | None = None

class DebateRequest(BaseModel):
    ticker: str
    challenge: str
    stance: Literal["bullish", "bearish", "neutral"] = "neutral"
