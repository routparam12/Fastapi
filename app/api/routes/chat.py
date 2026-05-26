from fastapi import APIRouter
from app.services.retriever import get_context
from app.services.generator import generate_response

router = APIRouter()


@router.post("/query")
async def chat_endpoint(query: str):
    # 1. Retrieve context from Vector DB
    context = get_context(query)

    # 2. Generate answer using LLM
    answer = generate_response(query, context)

    return {"query": query, "answer": answer}