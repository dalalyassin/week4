from fastapi import APIRouter
from schemas.base import PromptRequest, PromptResponse
from model.openai_client import call_llm
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/ask", tags=["llm"])


@router.post("", response_model=PromptResponse)
def ask_llm(req: PromptRequest):
    response = call_llm(req.prompt)
    answer = response.choices[0].message.content
    
    # Extract token usage
    usage = response.usage
    input_tokens = usage.prompt_tokens
    output_tokens = usage.completion_tokens
    total_tokens = usage.total_tokens
    
    # Log token counts
    logger.info(
        f"Token usage - Input: {input_tokens}, Output: {output_tokens}, Total: {total_tokens}"
    )
    
    return PromptResponse(
        prompt=req.prompt,
        answer=answer
    )