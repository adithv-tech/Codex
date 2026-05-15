from pydantic import BaseModel, Field


class ResearchRunRequest(BaseModel):
    ticker: str = Field(min_length=1, max_length=10)


class ResearchThreadResponse(BaseModel):
    thread_id: str
    ticker: str
    status: str


class DebateInput(BaseModel):
    text: str | None = None
    source_label: str = "user_submission"
