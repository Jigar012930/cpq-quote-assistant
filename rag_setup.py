"""
rag_setup.py — Day 3 of the CPQ Quote Assistant sprint.

Loads the toy catalog, converts each product and discount rule into a 
text chunk, embeds the chunks using ChromaDB's default embedding model,
and stores them in a local ChromaDB collection on disk.

Run this ONCE to set up the vector database. After that, rag_query.py
and the updated interactive_user_prompt.py will query this collection.
"""

import json
from pathlib import Path

import chromadb

# ---------------------------------------------------------------------------
# 1. Load the toy catalog from disk.
# ---------------------------------------------------------------------------
CATALOG_PATH = Path(__file__).parent / "catalog" / "products.json"

with open(CATALOG_PATH, "r", encoding="utf-8") as f:
    catalog = json.load(f)

# ---------------------------------------------------------------------------
# 2. Convert each product into a text chunk.
#    Each chunk is a self-contained natural-language description of one
#    product, so the embedding captures the product's meaning.
# ---------------------------------------------------------------------------
def product_to_chunk(product: dict) -> str:
    """Convert one product dict into a natural-language chunk."""
    attrs = product.get("attributes", {})
    return (
        f"Product SKU: {product['sku']}. "
        f"Name: {product['name']}. "
        f"Description: {product['description']}. "
        f"Base price: EUR {product['base_price_eur']} / "
        f"USD {product['base_price_usd']}. "
        f"Attributes: {json.dumps(attrs)}."
    )

# ---------------------------------------------------------------------------
# 3. Convert each discount rule into a text chunk.
# ---------------------------------------------------------------------------
def discount_to_chunk(rule: dict) -> str:
    """Convert one discount rule dict into a natural-language chunk."""
    return (
        f"Discount rule ID: {rule['id']}. "
        f"Name: {rule['name']}. "
        f"Type: {rule['type']}. "
        f"Discount: {rule['discount_pct']}%. "
        f"Description: {rule['description']}."
    )

# ---------------------------------------------------------------------------
# 4. Build the lists of chunks, IDs, and metadata.
#    ChromaDB needs three parallel lists when adding documents:
#    - documents: the text to embed
#    - ids: unique identifier per chunk (so we can update or fetch by ID)
#    - metadatas: structured fields we can filter on later (optional but useful)
# ---------------------------------------------------------------------------
documents = []
ids = []
metadatas = []

for product in catalog["products"]:
    documents.append(product_to_chunk(product))
    ids.append(product["sku"])
    metadatas.append({"type": "product", "sku": product["sku"]})

for rule in catalog["discount_rules"]:
    documents.append(discount_to_chunk(rule))
    ids.append(rule["id"])
    metadatas.append({"type": "discount_rule", "rule_id": rule["id"]})

# ---------------------------------------------------------------------------
# 5. Set up ChromaDB and create the collection.
#    PersistentClient stores data on disk so it survives between runs.
# ---------------------------------------------------------------------------
CHROMA_PATH = Path(__file__).parent / "chroma_db"

client = chromadb.PersistentClient(path=str(CHROMA_PATH))

# get_or_create_collection: if it already exists, reuse it; otherwise create it.
# We delete and recreate every time this script runs, to avoid stale data
# from old catalog versions.
collection_name = "cpq_catalog"
try:
    client.delete_collection(name=collection_name)
    print(f"Deleted existing collection '{collection_name}' (clean slate).")
except Exception:
    print(f"No existing collection '{collection_name}' to delete (first run).")

collection = client.create_collection(name=collection_name)

# ---------------------------------------------------------------------------
# 6. Add all chunks to the collection.
#    ChromaDB will embed each document automatically using its default
#    embedding model (no extra API calls, runs locally).
# ---------------------------------------------------------------------------
collection.add(
    documents=documents,
    ids=ids,
    metadatas=metadatas,
)

print(f"Added {len(documents)} chunks to collection '{collection_name}':")
for chunk_id, chunk_type in zip(ids, [m["type"] for m in metadatas]):
    print(f"  - {chunk_id} ({chunk_type})")

# ---------------------------------------------------------------------------
# 7. Sanity check: query the collection with a sample question and print
#    the top 3 matches. This confirms the setup worked end-to-end.
# ---------------------------------------------------------------------------
print("\n" + "=" * 70)
print("Sanity check — querying with: 'premium coated roll for high heat'")
print("=" * 70)

results = collection.query(
    query_texts=["premium coated roll for high heat"],
    n_results=3,
)

for rank, (doc_id, doc, distance) in enumerate(
    zip(results["ids"][0], results["documents"][0], results["distances"][0]),
    start=1,
):
    print(f"\nRank {rank}: {doc_id} (distance: {distance:.4f})")
    print(f"  {doc}")

print("\n" + "=" * 70)
print("Setup complete. Vector DB persisted to:", CHROMA_PATH)
# print("Sanity check — querying with: 'How much discount do I get on 1500 units?'")
# print("=" * 70)

# results = collection.query(
#     query_texts=["How much discount do I get on 1500 units?"],
#     n_results=5,
# )

# for rank, (doc_id, doc, distance) in enumerate(
#     zip(results["ids"][0], results["documents"][0], results["distances"][0]),
#     start=1,
# ):
#     print(f"\nRank {rank}: {doc_id} (distance: {distance:.4f})")
#     print(f"  {doc}")