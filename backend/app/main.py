from fastapi import FastAPI
from app.api.routes import health, research, debate

app = FastAPI(title="Institutional Stock Research OS", version="0.1.0")
app.include_router(health.router)
app.include_router(research.router, prefix="/api/v1")
app.include_router(debate.router, prefix="/api/v1")
