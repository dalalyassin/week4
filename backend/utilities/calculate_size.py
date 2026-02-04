GPT_3_5_TURBO_INPUT_PRICE = 0.0005   # $0.0005 per 1K tokens
GPT_3_5_TURBO_OUTPUT_PRICE = 0.0015  # $0.0015 per 1K tokens

def calculate_cost(prompt_tokens: int, completion_tokens: int, 
                   input_price: float = GPT_3_5_TURBO_INPUT_PRICE,
                   output_price: float = GPT_3_5_TURBO_OUTPUT_PRICE) -> float:
    """Calculate cost in USD based on token usage"""
    input_cost = (prompt_tokens / 1000) * input_price
    output_cost = (completion_tokens / 1000) * output_price
    return input_cost + output_cost