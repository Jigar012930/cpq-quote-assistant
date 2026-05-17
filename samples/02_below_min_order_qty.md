# 02 — Below Minimum Quantity for a

**Date tested:** 2026-05-20
**Model:** claude-sonnet-4-5
**Prompt version:** v2 (post Day 2 edge case handling)

## Question

> Customer wants order only 1 quantity of ROLL-CST-003, shipped to the Netherlands. What is the quote?

## Response

Please enter your quoting question (or 'exit/bye' to quit): Customer wants order only 1 quantity of ROLL-CST-003, shipped to the Netherlands. What is the quote? 

QUOTE ASSISTANT RESPONSE:
I need to clarify one important point before providing a quote:

**The minimum order quantity for ROLL-CST-003 (Custom Specification Roll) is 10 units, but you've requested only 1 unit.**

Error: Minimum order quantity for ROLL-CST-003 is 10 units.

Would you like to:
- Increase the quantity to at least 10 units of ROLL-CST-003, or
- Consider a different product with a lower minimum order quantity?

## What this demonstrates

That CLAUDE respects the minimum quantity that needs to be ordered for each SKU.