from fastapi import APIRouter
from schemas.base import PromptRequest, PromptResponse
from model.openai_client import call_llm

router = APIRouter(prefix="/ask", tags=["llm"])


@router.post("", response_model=PromptResponse)
def ask_llm(req: PromptRequest):
    response = call_llm(req.prompt)
    answer = response.choices[0].message.content

    return PromptResponse(
        prompt=req.prompt,
        answer=answer
    )

