# app/validation/exchange.py

import json

def parse_tool_arguments(tool_call):
    try:
        return json.loads(tool_call.function.arguments)
    except Exception:
        return None


def validate_exchange_args(args):
    if args is None:
        return False, "Arguments are not valid JSON"

    for field in ["base_currency", "target_currency"]:
        if field not in args:
            return False, f"Missing required field: {field}"
        if not isinstance(args[field], str):
            return False, f"{field} must be a string"

    return True, None

