import requests
import json

BASE_URL = "http://127.0.0.1:15002"

def test_health():
    print("🩺 Testando /health ...")
    try:
        resp = requests.get(f"{BASE_URL}/health", timeout=5)
        print("Status:", resp.status_code)
        print("Resposta:", resp.text)
    except Exception as e:
        print("❌ Erro ao conectar:", e)


def test_vectorize():
    print("\n🧠 Testando /v1/vectorize ...")
    payload = {
        "inputs": ["Engenheiro de redes com experiência em WSO2, Ansible e 6G IoT."],
        "model": "text-embedding-3-small"
    }
    try:
        resp = requests.post(f"{BASE_URL}/v1/vectorize", json=payload, timeout=15)
        print("Status:", resp.status_code)
        print("Resposta:", resp.text)
        data = resp.json()
        if "data" in data and len(data["data"]) > 0:
            print("📏 Tamanho do vetor:", len(data["data"][0]["embedding"]))
    except Exception as e:
        print("❌ Erro ao vetorizar:", e)


def test_search():
    print("\n🔍 Testando /v1/search ...")
    payload = {
        "query": "automação de APIs com WSO2 e Ansible",
        "model": "text-embedding-3-small"
    }
    try:
        resp = requests.post(f"{BASE_URL}/v1/search", json=payload, timeout=15)
        print("Status:", resp.status_code)
        print("Resposta:", resp.text)
    except Exception as e:
        print("❌ Erro ao buscar:", e)



if __name__ == "__main__":
    print("=== 🔧 Teste de Conexão com Vectorizer ===")
    test_health()
    test_vectorize()
    test_search()
