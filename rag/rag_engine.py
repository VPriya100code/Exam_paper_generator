from sentence_transformers import SentenceTransformer
import faiss

model = SentenceTransformer('all-MiniLM-L6-v2')

def build_rag(units_text):
    docs = [u.strip() for u in units_text.split("\n") if u.strip()]

    embeddings = model.encode(docs)

    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)

    return index, docs

def retrieve_context(index, docs):
    query = "important exam topics"
    q_embed = model.encode([query])

    k = min(3, len(docs))
    D, I = index.search(q_embed, k)

    return "\n".join([docs[i] for i in I[0]])