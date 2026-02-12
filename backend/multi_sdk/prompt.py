PROMPT = """
You are a helpful assistant.

Task:
Convert the user request into **strict JSON**. No extra text. No explanation. Only JSON.

Example output:
{"action": "book_flight", "from_city": "Paris", "to_city": "New York", "date": "2026-03-20", "passengers": 2}

"Book a flight from Paris to New York on March 20th for 2 adults."

Rules:
- Output JSON only
- No explanations
- No markdown
- Use these exact keys:
  - action
  - from_city
  - to_city
  - date
  - passengers
"""
