# app/utils/tool_messages.py

def tool_success(tool_call_id, result):
    return {
        "role": "tool",
        "tool_call_id": tool_call_id,
        "content": str(result)
    }


def tool_error(tool_call_id, error):
    return {
        "role": "tool",
        "tool_call_id": tool_call_id,
        "content": f"ERROR: {error}"
    }

