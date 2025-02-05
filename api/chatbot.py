from fastapi import APIRouter
from chatbot import query_chatbot

router = APIRouter()

@router.get("/chatbot/")
def chatbot(query: str):
    return {"response": query_chatbot(query)}
