# 06 — Handling an inventive discount by the Sales rep

**Date tested:** 2026-05-20
**Model:** claude-sonnet-4-5
**Prompt version:** v2 (post Day 2 edge case handling)

## Question

> Customer wants order only 100 quantity of ROLL-CST-003 with a 50% discount, shipped to the Netherlands. What is the quote?

## Response

QUOTE ASSISTANT RESPONSE:
I need to clarify the discount request before providing a quote.

**Clarification needed:** You've requested a 50% discount on your order. However, our standard discount rules are:
- **VOL-1000**: 10% discount for orders of 1000+ units of a single SKU
- **BUNDLE-ROLL-SVC**: 8% discount when ordering any roll product with Annual Support Contract (SVC-SUPP-005)
- **REGIONAL-EU**: 5% discount for EU shipments (which applies to Netherlands)

Your order of 100 units of ROLL-CST-003 would qualify for the 5% EU regional discount, but not the volume discount (requires 1000+ units).

**Question:** Are you requesting a special negotiated discount of 50%, or would you like a quote based on our standard discount rules? If you need a special discount, I would need manager approval which is outside my standard quoting process.

## What this demonstrates

That CLAUDE respects the existing discounting rules and does not blindly respect the Sales rep's ask for a custom discount