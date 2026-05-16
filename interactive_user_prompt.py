#This code would work on the same concept of before.
#This code would ask for the user input and then it would give the answer to the user based on the input and the catalog.

import json
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

CATALOG_PATH = Path(__file__).parent / "catalog" / "products.json"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

# CATALOG_PATH = Path(__file__).parent /catalog/products.json
# with open(CATALOG_PATH, "r",encoding="utf-8") as f:
#     catalog = json.load(f)
#

SYSTEM_PROMPT = f"""You are a quoting assistant which has information about the products and discount rules of an industrial roll manufacturer. When asked for a quote, you must:
1. Identify the requested products by SKU and the region.
2. List line items with quantity and base price.
3. Evaluate every discount rule and apply the ones that qualify. Cite each applied rule by its ID (e.g. "Applied VOL-1000").
4. Show the math: subtotal, discounts, final total.
5. Use the currency implied by the shipping region (EUR for EU, USD otherwise).
6. Be concise. Show your reasoning briefly but clearly.
the information about the products and discount rules are given below:
{json.dumps(catalog, indent=2)}
"""

client = Anthropic()


while True:
    user_input = input("Please enter your quoting question (or 'exit/bye' to quit): ")
    if user_input.lower() in ['exit', 'bye']:
        print("Goodbye!")
        break

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": user_input}
        ]
    )

    print("\nQUOTE ASSISTANT RESPONSE:")
    print(response.content[0].text.strip())

# Output:
# Please enter your quoting question (or 'exit/bye' to quit): How would quoting work for a product ROLL-PRM-002 in 1000mm width shipping to Netherlands and quantity of 500

# QUOTE ASSISTANT RESPONSE:
# # Quote for ROLL-PRM-002

# ## Customer Request
# - **Product:** ROLL-PRM-002 (Premium Coated Roll)
# - **Width:** 1000mm ✓ (available)
# - **Quantity:** 500 units
# - **Shipping to:** Netherlands (EU region)
# - **Currency:** EUR

# ---

# ## Line Items

# | SKU | Description | Qty | Unit Price | Subtotal |
# |-----|-------------|-----|------------|----------|
# | ROLL-PRM-002 | Premium Coated Roll (1000mm) | 500 | €820.00 | €410,000.00 |

# **Subtotal:** €410,000.00

# ---

# ## Discount Evaluation

# ✓ **Applied REGIONAL-EU** (-5%)  
# Shipping to Netherlands qualifies for EU regional discount.  
# **Discount:** €410,000.00 × 5% = **-€20,500.00**

# ✗ **VOL-1000** (not applicable)  
# Requires 1000+ units; order is 500 units.

# ✗ **BUNDLE-ROLL-SVC** (not applicable)  
# Requires SVC-SUPP-005 (Annual Support Contract) in the order.

# ---

# ## Final Total

# | Item | Amount |
# |------|--------|
# | Subtotal | €410,000.00 |
# | Discounts | -€20,500.00 |
# | **Total** | **€389,500.00** |

# ---

# **Note:** Minimum order quantity for ROLL-PRM-002 is 25 units ✓ (met with 500 units)
# Please enter your quoting question (or 'exit/bye' to quit): How would quoting work for a product ROLL-PRM-002 in 1000mm width shipping to Netherlands and quantity of 1500 with a annual support product added as well

# QUOTE ASSISTANT RESPONSE:
# # Quote for ROLL-PRM-002 + Annual Support | Netherlands

# ## Line Items

# | SKU | Product | Qty | Unit Price | Subtotal |
# |-----|---------|-----|------------|----------|
# | ROLL-PRM-002 | Premium Coated Roll (1000mm width) | 1,500 | €820.00 | €1,230,000.00 |
# | SVC-SUPP-005 | Annual Support Contract | 1 | €600.00 | €600.00 |
# | | | | **Subtotal:** | **€1,230,600.00** |

# ## Applied Discounts

# 1. **VOL-1000** (Volume discount — 1000+ units)
#    - Applies to ROLL-PRM-002 (qty 1,500 ≥ 1,000)
#    - 10% off €1,230,000.00 = **-€123,000.00**

# 2. **BUNDLE-ROLL-SVC** (Bundle discount — Roll + Support)
#    - ROLL-PRM-002 ordered with SVC-SUPP-005
#    - 8% off total subtotal = 8% × €1,230,600.00 = **-€98,448.00**

# 3. **REGIONAL-EU** (EU shipment discount)
#    - Shipping to Netherlands (EU region)
#    - 5% off total subtotal = 5% × €1,230,600.00 = **-€61,530.00**

# **Total Discounts:** €282,978.00

# ---

# ## Final Quote

# **Order Total: €947,622.00 EUR**

# **Savings: €282,978.00 (23% off)**

# ---

# *Note: Pricing in EUR as shipping destination is EU. ROLL-PRM-002 meets minimum order quantity of 25 units. All three discount rules qualify and stack on this order.*
# Please enter your quoting question (or 'exit/bye' to quit): exit
# Goodbye!