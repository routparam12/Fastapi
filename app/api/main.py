from fastapi import FastAPI
from app.api.routes import chat,ingest

from fastapi import APIRouter
from app.api.routes import chat, ingest

api_router = APIRouter()
api_router.include_router(chat.router, prefix="/chat", tags=["chat"])
api_router.include_router(ingest.router, prefix="/ingest", tags=["ingest"])

app = FastAPI(title="RAG API")

# Include all routes from the API layer
app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "online"}