from fastapi import APIRouter
from schemas.base import PromptRequest, PromptResponse
from model.openai_client import call_llm
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/ask", tags=["llm"])


@router.post("", response_model=PromptResponse)
def ask_llm(req: PromptRequest):
    # Use provided temperature/top_p or default to 0.5
    temperature = req.temperature if req.temperature is not None else 0.5
    top_p = req.top_p if req.top_p is not None else 0.5
    
    # Log the parameters being used
    logger.info(f"Request received - Temperature: {temperature}, Top_p: {top_p}, Session: {req.session_id}")
    logger.info(f"Prompt: {req.prompt[:100]}..." if len(req.prompt) > 100 else f"Prompt: {req.prompt}")
    
    response = call_llm(req.prompt, temperature=temperature, top_p=top_p)
    answer = response.choices[0].message.content

    logger.info(f"Response generated - Length: {len(answer)} characters")

    return PromptResponse(
        prompt=req.prompt,
        answer=answer
    )