"""
rag_query.py — Day 4 of the CPQ Quote Assistant sprint.

Interactive query tool for probing retrieval behavior against the
ChromaDB collection built by rag_setup.py.

This is a development utility, not part of the assistant runtime.
Use it to:
  - Observe which chunks get returned for a given question
  - Compare expected vs actual retrieval rankings
  - Build intuition for embedding-based similarity behavior

Prerequisite: rag_setup.py must have been run at least once, so the
chroma_db/ folder and cpq_catalog collection exist.
"""

from pathlib import Path

import chromadb

# ---------------------------------------------------------------------------
# 1. Connect to the existing ChromaDB instance on disk.
#    Same path as rag_setup.py — this is what "persistent" means in practice:
#    one script writes, another script reads, both via the same folder.
# ---------------------------------------------------------------------------
CHROMA_PATH = Path(__file__).parent / "chroma_db"
COLLECTION_NAME = "cpq_catalog"

client = chromadb.PersistentClient(path=str(CHROMA_PATH))

# ---------------------------------------------------------------------------
# 2. Open the existing collection.
#    get_collection (not create_collection) — we EXPECT it to exist.
#    If it doesn't, we fail fast with a clear error message.
# ---------------------------------------------------------------------------
try:
    collection = client.get_collection(name=COLLECTION_NAME)
except Exception as e:
    raise SystemExit(
        f"Collection '{COLLECTION_NAME}' not found. "
        f"Run 'python rag_setup.py' first to build the vector database.\n"
        f"Underlying error: {e}"
    )

print(f"Connected to collection '{COLLECTION_NAME}'.")
print(f"Collection contains {collection.count()} chunks.\n")

# ---------------------------------------------------------------------------
# 3. Interactive query loop.
#    Same pattern as interactive_user_prompt.py but with NO Claude involved —
#    we're only inspecting what the vector DB returns.
# ---------------------------------------------------------------------------
DEFAULT_N_RESULTS = 5

print("=" * 70)
print("RAG Query Tool — type a question to see what gets retrieved.")
print("Type 'quit' or 'exit' to end.")
print("=" * 70)

while True:
    query = input("\nQuery: ").strip()

    if query.lower() in {"quit", "exit", ""}:
        print("Done.")
        break

    # ---------------------------------------------------------------------
    # 4. Run the similarity query against ChromaDB.
    #    query_texts: the question(s) to search for. Can be a list of
    #    multiple queries in one call, but we pass one at a time here.
    #    n_results: how many top matches to return.
    # ---------------------------------------------------------------------
    results = collection.query(
        query_texts=[query],
        n_results=DEFAULT_N_RESULTS,
    )

    # ---------------------------------------------------------------------
    # 5. Print results in a readable format.
    #    results is a dict where each field is a LIST OF LISTS — outer list
    #    is per-query (we only asked one, so we use [0]), inner list is
    #    per-result (top N).
    # ---------------------------------------------------------------------
    ids = results["ids"][0]
    documents = results["documents"][0]
    distances = results["distances"][0]
    metadatas = results["metadatas"][0]

    print(f"\nTop {len(ids)} results for: '{query}'")
    print("-" * 70)

    for rank, (chunk_id, doc, distance, metadata) in enumerate(
        zip(ids, documents, distances, metadatas),
        start=1,
    ):
        chunk_type = metadata.get("type", "unknown")
        print(f"\nRank {rank}: {chunk_id}  ({chunk_type}, distance: {distance:.4f})")
        print(f"  {doc}")

    print("\n" + "=" * 70)