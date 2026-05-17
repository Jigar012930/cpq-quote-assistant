# 05 — Discounts applied on each bundle SKU with a support plan

**Date tested:** 2026-05-20
**Model:** claude-sonnet-4-5
**Prompt version:** v2 (post Day 2 edge case handling)

## Question

> Quote 1200 units of ROLL-STD-001 plus 50 units of anti_static coating ROLL-PRM-002 plus one premium annual support for each SKU, shipping to Switzerland

## Response

QUOTE ASSISTANT RESPONSE:
# Quote for Switzerland

## Line Items

| SKU | Product | Quantity | Base Price (USD) | Subtotal (USD) |
|-----|---------|----------|------------------|----------------|
| ROLL-STD-001 | Standard Industrial Roll | 1,200 | $495 | $594,000 |
| ROLL-PRM-002 | Premium Coated Roll (anti-static) | 50 | $905 | $45,250 |
| SVC-SUPP-005 | Annual Support Contract (premium tier) | 2 | $660 | $1,320 |

**Subtotal:** $640,570

## Applicable Discounts

### 1. Volume Discount (VOL-1000)
- **Applied to ROLL-STD-001:** 1,200 units ≥ 1,000 threshold
- Discount: $594,000 × 10% = **-$59,400**

### 2. Bundle Discount (BUNDLE-ROLL-SVC)
- **Applied to ROLL-STD-001:** Bundled with SVC-SUPP-005
- Discount: $594,000 × 8% = **-$47,520**

- **Applied to ROLL-PRM-002:** Bundled with SVC-SUPP-005
- Discount: $45,250 × 8% = **-$3,620**

**Total Discounts:** -$110,540

## Final Total

| Item | Amount (USD) |
|------|--------------|
| Subtotal | $640,570 |
| Total Discounts | -$110,540 |
| **Final Total** | **$530,030** |

**Currency:** USD (Switzerland is outside the EU)

**Note:** Switzerland is not part of the EU, so the REGIONAL-EU discount does not apply. VOL-1000 and BUNDLE-ROLL-SVC discounts have been applied where qualifying.

## What this demonstrates

That CLAUDE respects the discounting rule where each SKU is given the discount rather than a cummulative discount on the aggregate price of both