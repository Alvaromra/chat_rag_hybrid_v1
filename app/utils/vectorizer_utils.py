# app/utils/vectorizer_utils.py

from app.utils.vectorizer_client import embed_text, search_query, check_health

# Apenas reexporta as funções do client atualizado
buscar_texto = search_query
gerar_embedding = embed_text
verificar_servidor = check_health
