# app/services/exchange.py

def get_exchange_rate(base_currency, target_currency, date=None):
    # Fake data for now
    return {
        "base_currency": base_currency,
        "target_currency": target_currency,
        "rate": 0.92,
        "date": date or "latest"
    }

