# 04 — Handling of Ambiguous Request

**Date tested:** 2026-05-20
**Model:** claude-sonnet-4-5
**Prompt version:** v2 (post Day 2 edge case handling)

## Question

> Customer wants order some products from our catalog for a client in Europe. What is the quote?

## Response

QUOTE ASSISTANT RESPONSE:
I need some additional information before I can provide you with a quote:

1. **Which specific product(s)** would you like to order? Please provide the SKU (e.g., ROLL-STD-001) or product name.
2. **What quantity** do you need for each product?
3. **Which specific country in Europe** will this be shipped to? (I need the exact country, not just "Europe" or "EU", to determine the correct currency and applicable discounts.)

Once you provide these details, I'll be able to generate an accurate quote for you.

## What this demonstrates

That CLAUDE respects the input rules and asks for all the information it requires before it can generate a quote