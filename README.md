# 🤖 BimBam Buy Agent

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.x-black)
![LangChain](https://img.shields.io/badge/LangChain-RAG-green)
![Railway](https://img.shields.io/badge/Deploy-Railway-purple)
![Netlify](https://img.shields.io/badge/Frontend-Netlify-00C7B7)
![License](https://img.shields.io/badge/License-MIT-yellow)

Asistente Inteligente basado en IA para BimBam Buy.

Utiliza un sistema **RAG (Retrieval-Augmented Generation)** con **FAISS + LangChain + OpenRouter** para responder únicamente con información contenida en la documentación oficial de la empresa.

---

## 🌐 Demo

### Frontend
Ingresa Aquí para mirar el entorno.

**https://agentebimbam.netlify.app/**

<img width="988" height="692" alt="image" src="https://github.com/user-attachments/assets/165c9ffd-3301-4266-b32b-7c22b48de05a" />


### Backend API

https://agente-bimbam-buy-production.up.railway.app

---

## 🚀 Características

- ✅ Chat en tiempo real
- ✅ Interfaz moderna y responsiva
- ✅ Recuperación semántica mediante FAISS
- ✅ Embeddings con HuggingFace
- ✅ LLM mediante OpenRouter
- ✅ Base documental en PDF
- ✅ Índice FAISS persistente
- ✅ API REST con Flask
- ✅ Despliegue en Railway
- ✅ Frontend en Netlify

---

## 🏗 Arquitectura

```
Frontend (Netlify)
        │
        ▼
Flask API (Railway)
        │
        ▼
RAG Manager
        │
 ┌──────────────┐
 │ FAISS Index  │
 └──────────────┘
        │
        ▼
PDFs de conocimiento
        │
        ▼
OpenRouter LLM
```

---

## 📁 Estructura del proyecto

```
Agente_Bim_Bam_Buy/
│
├── app.py
├── routes.py
├── rag_manager.py
├── crear_indice.py
├── config.py
├── requirements.txt
├── render.yaml
├── runtime.txt
│
├── data/
│   ├── pdf/
│   └── vectorstore/
│
├── logs/
│
└── README.md
```

---

## ⚙ Variables de entorno

```
OPENROUTER_API_KEY=

MODEL_NAME=

EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

OPENROUTER_BASE_URL=https://openrouter.ai/api/v1

TEMPERATURE=0
```

---

## 📚 Construcción del índice

```
python crear_indice.py
```

Esto generará automáticamente:

```
data/vectorstore/
    ├── index.faiss
    └── index.pkl
```

---

## ▶ Ejecutar localmente

```
pip install -r requirements.txt

python app.py
```

o

```
flask run
```

---

## 🌐 Endpoints

### Estado

```
GET /health
```

### Información

```
GET /status
```

### Consulta

```
POST /preguntar
```

Body

```json
{
    "pregunta": "¿Qué cubre la garantía?"
}
```

Respuesta

```json
{
    "success": true,
    "data": {
        "respuesta": "..."
    }
}
```

---

## 🛠 Tecnologías

- Python 3.11
- Flask
- LangChain
- FAISS
- HuggingFace Embeddings
- OpenRouter
- PyMuPDF
- Railway
- Netlify

---

## 📄 Licencia

MIT License





