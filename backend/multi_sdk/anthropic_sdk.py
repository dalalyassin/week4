import os
from dotenv import load_dotenv
from anthropic import Anthropic  # Correct import
import json
from prompt import PROMPT

load_dotenv()

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=ANTHROPIC_API_KEY)  # Use Anthropic class directly

# Modern Anthropic API uses messages.create(), not completions.create()
response = client.messages.create(
    model="claude-3-sonnet-20240229",  # Update to a valid Claude 3 model
    max_tokens=500,
    temperature=0,
    messages=[
        {"role": "user", "content": PROMPT}
    ]
)

# Modern API returns response.content[0].text, not response.completion
output = response.content[0].text
print("RAW OUTPUT:")
print(output)

try:
    parsed = json.loads(output)
    print("\nPARSED OUTPUT:")
    print(parsed)
except json.JSONDecodeError:
    print("\nCould not parse as JSON. Output raw text:")
    print(output)