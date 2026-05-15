from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Autonomous Stock Research OS", version="0.1.0")
app.include_router(router, prefix="/api")


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}
