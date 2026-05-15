"""
hello.py — Day 1 of the CPQ Quote Assistant sprint.

Loads the toy catalog, sends a sample quoting question to Claude
with the catalog stuffed into the system prompt, prints the response.

This is the naive baseline. RAG retrieval comes Day 3, agent loop Day 6.
"""

import json
import os
from pathlib import Path

from anthropic import Anthropic
from dotenv import load_dotenv

# ---------------------------------------------------------------------------
# 1. Load environment variables from .env into the process environment.
#    The Anthropic SDK reads ANTHROPIC_API_KEY automatically once loaded.
# ---------------------------------------------------------------------------
load_dotenv()

# ---------------------------------------------------------------------------
# 2. Load the toy catalog from disk.
#    Path(__file__) is the path to this script; .parent is its folder.
#    This makes the script work no matter what folder you run it from.
# ---------------------------------------------------------------------------
CATALOG_PATH = Path(__file__).parent / "catalog" / "products.json"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

# ---------------------------------------------------------------------------
# 3. Build the system prompt. The system prompt sets Claude's role and
#    gives it the catalog as background knowledge for this conversation.
# ---------------------------------------------------------------------------
SYSTEM_PROMPT = f"""You are a CPQ Quote Assistant for an industrial roll manufacturer.
You help sales reps configure quotes by reasoning over the product catalog
and discount rules below.

When asked for a quote, you must:
1. Identify the requested products by SKU.
2. List line items with quantity and base price.
3. Evaluate every discount rule and apply the ones that qualify.
   Cite each applied rule by its ID (e.g. "Applied VOL-1000").
4. Show the math: subtotal, discounts, final total.
5. Use the currency implied by the shipping region (EUR for EU, USD otherwise).
6. Be concise. Show your reasoning briefly but clearly.

If a request is ambiguous or missing information, ask one clarifying question
before quoting.

CATALOG AND DISCOUNT RULES:
{json.dumps(catalog, indent=2)}
"""

# ---------------------------------------------------------------------------
# 4. The sample user question. Day 1 we hardcode it; later we'll read
#    real input from a UI.
# ---------------------------------------------------------------------------
USER_QUESTION = (
    "Customer wants 1200 units of ROLL-STD-001 in 1000mm width, "
    "shipping to Germany. They're also asking about adding the annual "
    "premium support contract. What's the quote?"
)

# ---------------------------------------------------------------------------
# 5. Send the request to Claude.
# ---------------------------------------------------------------------------
client = Anthropic()  # reads ANTHROPIC_API_KEY from environment

response = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1024,
    system=SYSTEM_PROMPT,
    messages=[
        {"role": "user", "content": USER_QUESTION},
    ],
)

# ---------------------------------------------------------------------------
# 6. Print the result and a small summary of token usage.
# ---------------------------------------------------------------------------
print("=" * 70)
print("USER QUESTION:")
print(USER_QUESTION)
print("=" * 70)
print("CLAUDE RESPONSE:")
print(response.content[0].text)
print("=" * 70)
print(
    f"Tokens used — input: {response.usage.input_tokens}, "
    f"output: {response.usage.output_tokens}"
)