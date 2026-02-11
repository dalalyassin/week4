import requests


def get_exchange_rate(base_currency: str, target_currency: str, date: str = "latest") -> float:
    
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/v1/currencies/{base_currency.lower()}.json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data.get(base_currency.lower(), {}).get(target_currency.lower(), None)
    else:
        raise Exception(f"Failed to fetch exchange rate: {response.status_code}")

def tell_joke(category: str = "general") -> str:
    """Return a random joke. You can specify a category like general or animal."""
    jokes = {
        "general": [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "Why don't eggs tell jokes? They'd crack each other up!",
        ],
        "animal": [
            "What do you call a sleeping bull? A bulldozer!",
            "Why don't cats play poker in the jungle? Too many cheetahs!",
            "What's a dog's favorite pizza? Pupperoni!",
        ]
    }
    
    import random
    joke_list = jokes.get(category.lower(), jokes["general"])
    return random.choice(joke_list)

def pprint_response(response):
    print("--- Full Response ---\n")
    print(response, "\n")
    
    print("--- Chat Completion Message ---\n")
    print(response.choices[0].message, "\n")
    
    if response.choices[0].message.tool_calls:
        for i in range(0, len(response.choices[0].message.tool_calls)):
            print(f"--- Tool Call {i+1} ---\n")
            print(f"Function: {response.choices[0].message.tool_calls[i].function.name}\n")
            print(f"Arguments: {response.choices[0].message.tool_calls[i].function.arguments}\n")