# app/routers/chat_api.py
# FastAPI router for chat endpoint

from fastapi import APIRouter
from pydantic import BaseModel
from app.routers.chat import handle_chat

router = APIRouter(prefix="/chat", tags=["chat"])


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    prompt: str
    answer: str


@router.post("", response_model=ChatResponse)
def chat_endpoint(req: ChatRequest):
    answer = handle_chat(req.prompt)
    return ChatResponse(
        prompt=req.prompt,
        answer=answer
    )

