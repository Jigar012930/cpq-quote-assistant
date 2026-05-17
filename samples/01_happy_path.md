# 01 — Happy path: multi-SKU order with stacking discounts

**Date tested:** 2026-05-20
**Model:** claude-sonnet-4-5
**Prompt version:** v2 (post Day 2 edge case handling)

## Question

> Customer wants 1200 units of ROLL-STD-001 in 1000mm width, shipping to Germany. They're also asking about adding the Annual Support Contract (SVC-SUPP-005). What's the quote?

## Response

QUOTE ASSISTANT RESPONSE:
I have all the information needed to provide a quote. Let me break this down for you:

---

## Quote for Germany Shipment

### Line Items:
1. **ROLL-STD-001** (Standard Industrial Roll, 1000mm width)
   - Quantity: 1,200 units
   - Base price: €450/unit
   - Subtotal: €540,000

2. **SVC-SUPP-005** (Annual Support Contract)
   - Quantity: 1
   - Base price: €600
   - Subtotal: €600

**Order Subtotal: €540,600**

---

### Applied Discounts:

**1. VOL-1000** (Volume discount — 1000+ units)
- Applies to ROLL-STD-001: 1,200 units ≥ 1,000 threshold ✓
- Discount: 10% × €540,000 = **-€54,000**

**2. BUNDLE-ROLL-SVC** (Roll + Annual Support bundle)
- Applies to ROLL-STD-001 (bundled with SVC-SUPP-005) ✓
- Discount: 8% × €540,000 = **-€43,200**

**3. REGIONAL-EU** (EU shipment discount)
- Shipping to Germany (EU member) ✓
- Discount: 5% × €540,600 = **-€27,030**

**Total Discounts: -€124,230**

---

### Final Calculation:
- Subtotal: €540,600
- Total Discounts: -€124,230
- **Final Total: €416,370**

**Currency: EUR**

---

**Summary:** You're saving €124,230 (23%) through volume, bundle, and regional discounts.

## What this demonstrates

Three discount rules firing in sequence — VOL-1000 on the rolls, 
BUNDLE-ROLL-SVC across both line items, REGIONAL-EU on the order total. 
Currency correctly inferred as EUR for an EU destination. Math shown 
step-by-step with rule IDs cited.