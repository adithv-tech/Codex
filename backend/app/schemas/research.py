from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class StartResearchRequest(BaseModel):
    ticker: str = Field(..., min_length=1, max_length=10)

class StageResult(BaseModel):
    stage: str
    prompt_id: int
    agent: str
    prompt: str
    output: str
    sources: List[str] = []

class DebateRequest(BaseModel):
    ticker: str
    message: str
    attachments: Optional[List[str]] = None

class DebateResponse(BaseModel):
    revised_thesis: str
    what_changed: List[str]
    risk_weighting_delta: Dict[str, float]
