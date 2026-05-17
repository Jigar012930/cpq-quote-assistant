# Samples — CPQ Quote Assistant

This folder contains example input/output pairs from the assistant, captured
during development. Each sample is a single quoting scenario, with the question
asked, the response received, and a short note on what the sample demonstrates.

These samples serve two purposes:
1. They show what the assistant does without requiring the reader to run code
2. They form an informal regression suite — when the prompt or model changes,
   these scenarios are re-run to verify behavior is preserved or improved

## Index

| #  | Scenario | What it demonstrates |
|----|----------|----------------------|
| 01 | [Happy path](01_happy_path.md) | Multi-SKU order with three stacking discounts |
| 02 | [Below min order qty](02_below_min_order_qty.md) | Hard block on quantity below catalog minimum |
| 03 | [Product not found](03_product_not_found.md) | SKU validation refuses to invent products |
| 04 | [Ambiguous request](04_ambiguous_request.md) | Assistant asks one clarifying question |
| 05 | [Bundle across two SKUs](05_bundle_across_two_skus.md) | Bundle discount fires per eligible roll SKU |
| 06 | [Invented discount refused](06_invented_discount_refused.md) | Assistant declines to apply unspecified discount |