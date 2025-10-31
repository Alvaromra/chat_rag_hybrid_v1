from flask import Flask
from dotenv import load_dotenv
import os

# ✅ Força o carregamento do .env usando caminho absoluto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOTENV_PATH = os.path.join(os.path.dirname(BASE_DIR), ".env")
load_dotenv(DOTENV_PATH)

from app.routes.chat_rag import bp as chat_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(chat_bp)
    return app
