import os
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

# Initialize embeddings and LLM
# Ensure GOOGLE_API_KEY is set in your environment
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

def get_vector_db(texts):
    # Create the vector store in memory (or persist to a directory)
    vector_db = Chroma.from_texts(
        texts=texts,
        embedding=embeddings,
        collection_name="professional_profile"
    )
    return vector_db

def ask_rag(query, vector_db):
    retriever = vector_db.as_retriever(search_kwargs={"k": 3})
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )
    return qa_chain.invoke(query)