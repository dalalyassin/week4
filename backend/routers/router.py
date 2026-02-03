from fastapi import APIRouter
from schemas.base import PromptRequest, PromptResponse
from services.openai_client import call_llm
import uuid
import logging

router = APIRouter(prefix="/ask", tags=["llm"])
logger = logging.getLogger(__name__)


@router.post("", response_model=PromptResponse)
def ask_llm(req: PromptRequest):
    session_id = req.session_id or str(uuid.uuid4())

    response = call_llm(session_id, req.prompt)

    usage = response.usage
    logger.info(
        f"Token usage: "
        f"input={usage.prompt_tokens}, "
        f"output={usage.completion_tokens}, "
        f"total={usage.total_tokens}"
    )

    return PromptResponse(
        prompt=req.prompt,
        answer=response.choices[0].message.content,
        session_id=session_id,
    )
