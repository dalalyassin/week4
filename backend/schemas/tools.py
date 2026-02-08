from pydantic import BaseModel, Field
from typing import Dict, Any, Optional, List, Literal


class ToolParameter(BaseModel):
    """JSON Schema parameter definition for a tool"""
    type: str
    description: Optional[str] = None
    enum: Optional[List[Any]] = None
    properties: Optional[Dict[str, "ToolParameter"]] = None
    required: Optional[List[str]] = None
    items: Optional["ToolParameter"] = None


class ToolSchema(BaseModel):
    """JSON Schema definition for a tool"""
    name: str
    description: str
    parameters: ToolParameter


class ToolCall(BaseModel):
    """Tool call request from the model"""
    id: str
    name: str
    arguments: Dict[str, Any]


class ToolResult(BaseModel):
    """Result returned from tool execution"""
    tool_call_id: str
    name: str
    result: Any
    error: Optional[str] = None