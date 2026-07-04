from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
)


@app.get("/")
async def root():
    return {
        "message": "Scholar Notes API",
        "status": "running",
    }

