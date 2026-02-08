# app/llm/tools.py

my_tools = [
    {
        "type": "function",
        "function": {
            "name": "get_exchange_rate",
            "description": "Get the exchange rate between two currencies",
            "parameters": {
                "type": "object",
                "properties": {
                    "base_currency": {
                        "type": "string",
                        "description": "Base currency, e.g. USD"
                    },
                    "target_currency": {
                        "type": "string",
                        "description": "Target currency, e.g. ILS"
                    },
                    "date": {
                        "type": "string",
                        "description": "Optional date YYYY-MM-DD"
                    }
                },
                "required": ["base_currency", "target_currency"]
            }
        }
    }
]

