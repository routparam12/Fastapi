from fastapi import APIRouter
from app.services.rag_engine import get_vector_db

router = APIRouter()

# Simple mock for your cleaned data chunks
raw_data_chunks = [
    "Paramjeet Rout is a Data Analyst with 1.5 years experience at Unimrkt Response LLP.",
    "Paramjeet's technical skills include Python, SQL, Azure SQL, PostgreSQL, Power BI, Docker, and Django.",
    "Paramjeet is working on an AI-powered customer support chatbot to automate account queries.",
    "Paramjeet's goal is to become a Data Scientist focusing on ML workflows and AI-driven systems."
]

# Create global or scoped db instance
vector_db = get_vector_db(raw_data_chunks)

@router.post("/ingest")
async def ingest_data():
    return {"status": "success", "message": "Knowledge base updated."}