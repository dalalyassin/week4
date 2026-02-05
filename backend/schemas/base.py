from pydantic import BaseModel, Field
from typing import Optional

class PromptRequest(BaseModel):
    prompt: str
    session_id: Optional[str] = None
    temperature: Optional[float] = Field(default=None, ge=0.0, le=2.0)
    top_p: Optional[float] = Field(default=None, ge=0.0, le=1.0)

class PromptResponse(BaseModel):
    answer: str
    session_id: Optional[str] = None