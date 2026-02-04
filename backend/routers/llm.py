from fastapi import APIRouter
from schemas.base import PromptRequest, PromptResponse
from services.openai_client import call_llm
import logging
from services.temp_storage import test_messages_storage
from utilities.calculate_size import calculate_cost
logger = logging.getLogger(__name__)


router = APIRouter(prefix="/ask", tags=["llm"])


@router.post("", response_model=PromptResponse)
def ask_llm(req: PromptRequest):
    response = call_llm(req)
    answer = response.choices[0].message.content
    
    # Log token usage
    usage = response.usage
    cost = calculate_cost(usage.prompt_tokens, usage.completion_tokens)

    logger.info(
        f"Token usage: "
        f"input={usage.prompt_tokens}, "
        f"output={usage.completion_tokens}, "
        f"total={usage.total_tokens}"
        f"cost=${cost:.6f}"

    )
    
    return PromptResponse(
        answer=answer,
        session_id=req.session_id
    )


@router.get("/debug/storage")
def get_storage():
    """Debug endpoint to view server-side message storage"""
    return {
        "sessions": list(test_messages_storage.keys()),
        "storage": {
            session_id: {
                "message_count": len(messages),
                "messages": messages
            }
            for session_id, messages in test_messages_storage.items()
        }
    }

