from fastapi import APIRouter
from schemas.base import PromptRequest, PromptResponse
from services.openai_client import call_llm
import logging
from services.temp_storage import test_messages_storage
logger = logging.getLogger(__name__)


router = APIRouter(prefix="/ask", tags=["llm"])


@router.post("", response_model=PromptResponse)
def ask_llm(req: PromptRequest):
    response = call_llm(req)  
    answer = response.choices[0].message.content
    
    
    # Extract token usage
    usage = response.usage
    input_tokens = usage.prompt_tokens
    output_tokens = usage.completion_tokens
    total_tokens = usage.total_tokens
    
    # Log token counts
    logger.info(
        f"Token usage: "
        f"input={input_tokens}, "
        f"output={output_tokens}, "
        f"total={total_tokens}"
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

