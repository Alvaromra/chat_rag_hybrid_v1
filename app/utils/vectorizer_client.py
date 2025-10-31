import requests

# URL base do servidor Vectorizer local
VECTORIZER_URL = "http://127.0.0.1:15002"

def check_health():
    """Verifica se o servidor Vectorizer está ativo."""
    try:
        resp = requests.get(f"{VECTORIZER_URL}/health", timeout=5)
        return resp.json()
    except Exception as e:
        return {"error": str(e)}

def embed_text(text, model="text-embedding-3-small"):
    """
    Gera embedding para um texto usando o Vectorizer local.
    Retorna o vetor numérico (lista de floats).
    """
    try:
        payload = {"input": text, "model": model}
        resp = requests.post(f"{VECTORIZER_URL}/api/embed", json=payload, timeout=15)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}", "details": resp.text}
        data = resp.json()
        if "embedding" in data:
            return data["embedding"]
        elif "data" in data and len(data["data"]) > 0:
            return data["data"][0].get("embedding", [])
        else:
            return {"error": "Resposta inesperada", "raw": data}
    except Exception as e:
        return {"error": str(e)}

def search_query(query, model="text-embedding-3-small"):
    """
    Realiza busca semântica no Vectorizer.
    Retorna documentos similares, se existirem.
    """
    try:
        payload = {"query": query, "model": model}
        resp = requests.post(f"{VECTORIZER_URL}/api/search", json=payload, timeout=15)
        if resp.status_code != 200:
            return {"error": f"HTTP {resp.status_code}", "details": resp.text}
        return resp.json()
    except Exception as e:
        return {"error": str(e)}
