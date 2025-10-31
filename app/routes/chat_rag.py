from flask import Blueprint, request, jsonify
import os
from openai import OpenAI
import requests

bp = Blueprint("chat_rag", __name__)

# Inicializa o cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Configurações do Vectorizer local
VECTOR_HOST = os.getenv("VECTOR_HOST", "http://127.0.0.1:15002")

# ================================
# 🔹 Rota raiz (verificação)
# ================================
@bp.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "message": "🚀 Flask + OpenAI + Vectorizer conectados!",
        "vectorizer": VECTOR_HOST
    })

# ================================
# 🔹 Endpoint de Chat com Vectorizer (RAG)
# ================================
@bp.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        if not user_message:
            return jsonify({"error": "Mensagem vazia."}), 400

        # 1️⃣ Busca contexto no Vectorizer local
        vectorizer_resp = requests.post(
            f"{VECTOR_HOST}/api/search",
            json={"query": user_message, "limit": 5}
        )

        if vectorizer_resp.status_code == 200:
            context_results = vectorizer_resp.json()
            context_texts = [
                r.get("text") or str(r)
                for r in context_results.get("results", [])
            ]
            context = "\n".join(context_texts)
        else:
            context = ""
            print("⚠️ Vectorizer retornou erro:", vectorizer_resp.text)

        # 2️⃣ Envia para o modelo OpenAI com contexto
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Você é um assistente que ajuda o Álvaro com IA e engenharia."},
                {"role": "user", "content": f"Contexto:\n{context}\n\nPergunta: {user_message}"}
            ]
        )

        answer = response.choices[0].message.content
        return jsonify({
            "user_message": user_message,
            "response": answer,
            "context_used": bool(context)
        })

    except Exception as e:
        print("❌ Erro no chat:", e)
        return jsonify({"error": str(e)}), 500

