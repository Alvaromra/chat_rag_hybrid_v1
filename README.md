# 🤖 Chat RAG Híbrido — OpenAI + Vectorizer + Flask

Este projeto integra **OpenAI GPT-4o-mini** com o **Vectorizer Server (Rust)**, criando um ambiente híbrido de *Retrieval-Augmented Generation (RAG)* que combina **busca vetorial** e **geração contextualizada** de respostas via LLM.

---

## 🧠 Visão Geral

O objetivo é permitir que um modelo de linguagem (LLM) responda perguntas com base em **contextos vetorizados localmente**.  
Isso cria um pipeline de IA híbrido:

> **Usuário → Flask → Vectorizer (busca semântica) → OpenAI GPT-4o-mini → Resposta contextualizada**

---

## 🚀 Tecnologias Utilizadas

| Camada | Ferramenta | Descrição |
|--------|-------------|-----------|
| 💬 LLM | **OpenAI GPT-4o-mini** | Modelo de linguagem para geração de respostas. |
| 🔎 Vetorização | **Vectorizer (Lucas Ferreira)** | Servidor Rust local para busca semântica. |
| 🧠 Backend | **Flask (Python 3.9)** | API intermediária que conecta OpenAI e Vectorizer. |
| ⚙️ Infraestrutura | **dotenv**, **requests**, **python-dotenv** | Gerenciamento de variáveis e integração HTTP. |

---

## 🧩 Estrutura do Projeto

chat_rag_hybrid_v1/
├── app/
│ ├── init.py # Inicialização do Flask + dotenv
│ ├── routes/
│ │ └── chat_rag.py # Endpoints / e /chat (integração com OpenAI + Vectorizer)
│ └── utils/ # Funções auxiliares e integração
├── vectorizer/ # Servidor Rust (submódulo ou build local)
├── tests/ # Scripts de teste de conexão e API
├── run.py # Inicializa o servidor Flask
├── requirements.txt # Dependências Python
├── .env # Variáveis de ambiente (não versionado)
└── README.md

yaml
Copiar código

---

## ⚙️ Instalação

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/alvaromra/chat_rag_hybrid_v1.git
cd chat_rag_hybrid_v

2️⃣ Criar ambiente virtual
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
