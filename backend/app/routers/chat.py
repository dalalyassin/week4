# app/routers/chat.py

from app.llm.client import call_llm
from app.llm.tools import my_tools
from app.validation.exchange import parse_tool_arguments, validate_exchange_args
from app.services.exchange import get_exchange_rate
from app.utils.tool_messages import tool_success, tool_error

def handle_chat(prompt: str):
    messages = [{"role": "user", "content": prompt}]

    response = call_llm(messages, tools=my_tools)
    message = response.choices[0].message

    if not message.tool_calls:
        return message.content

    tool_call = message.tool_calls[0]

    args = parse_tool_arguments(tool_call)
    is_valid, error = validate_exchange_args(args)

    if not is_valid:
        messages.append(message)
        messages.append(tool_error(tool_call.id, error))
        follow_up = call_llm(messages)
        return follow_up.choices[0].message.content

    result = get_exchange_rate(**args)

    messages.append(message)
    messages.append(tool_success(tool_call.id, result))

    final = call_llm(messages)
    return final.choices[0].message.content

