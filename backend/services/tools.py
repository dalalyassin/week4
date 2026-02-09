first_tools = [
        # Tool 1 - Get Exchange Rate
        { 
            "type": "function",
            "function": {
                "name": "get_exchange_rate",
                "description": "Get the current exchange rate of a base currency and target currency",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "base_currency": {
                            "type": "string",
                            "description": "The base currency for exchange rate calculations, i.e. USD, EUR, RUB",
                        },
                        "target_currency": {
                            "type": "string", 
                            "description": "The target currency for exchange rate calculations, i.e. USD, EUR, RUB"
                        },
                        "date": {
                            "type": "string", 
                            "description": "A specific day to reference, in YYYY-MM-DD format."
                        },
                    },
                    "required": ["base_currency", "target_currency"],
                },
            },
        },
    ]