# 🤖 BimBam Agent v2.0

Asistente inteligente desarrollado para **BimBam Buy** utilizando **Flask + LangChain + FAISS + OpenRouter**, capaz de responder preguntas basadas exclusivamente en una base documental compuesta por archivos PDF.

El sistema implementa una arquitectura **RAG (Retrieval-Augmented Generation)**, permitiendo consultar información empresarial de forma rápida, precisa y escalable.

---

# Características

- 🤖 Chat inteligente basado en IA.
- 📚 Base de conocimiento construida a partir de múltiples documentos PDF.
- 🔎 Búsqueda semántica mediante FAISS.
- ⚡ Índice persistente (los embeddings se generan una sola vez).
- 📄 Soporte para múltiples documentos.
- 🧠 Embeddings con Sentence Transformers.
- 🌐 Integración con OpenRouter.
- 🔐 Configuración mediante variables de entorno.
- 🏗 Arquitectura modular y fácil de mantener.
- ☁ Compatible con PythonAnywhere, Render, Railway y Docker.
- 🎨 Frontend web ligero en HTML, CSS y JavaScript.

---

# Arquitectura del proyecto

```
BimBam-Agent-v2/

│
├── app.py
├── config.py
├── routes.py
├── rag_manager.py
├── crear_indice.py
├── utils.py
├── requirements.txt
├── README.md
├── .env.example
│
├── data/
│   ├── documentos_pdf/
│   ├── vectorstore/
│   ├── uploads/
│   └── logs/
│
├── static/
│
└── templates/
    └── index.html
```

---

# Tecnologías utilizadas

- Python 3.11
- Flask
- LangChain
- FAISS
- OpenRouter
- Sentence Transformers
- PyMuPDF
- HTML5
- CSS3
- JavaScript

---

# Instalación

## 1. Clonar el proyecto

```bash
git clone https://github.com/TU_USUARIO/BimBam-Agent-v2.git

cd BimBam-Agent-v2
```

---

## 2. Crear un entorno virtual

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

---

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 4. Configurar variables de entorno

Crear un archivo llamado

```
.env
```

a partir de

```
.env.example
```

y configurar como mínimo:

```
OPENROUTER_API_KEY=
MODEL_NAME=
```

---

## 5. Agregar los documentos

Copiar todos los archivos PDF dentro de

```
data/documentos_pdf/
```

Ejemplo:

```
manual_garantias.pdf

politica_reembolsos.pdf

guia_envios.pdf

metodos_pago.pdf

programa_afiliados.pdf
```

---

## 6. Construir el índice FAISS

Ejecutar:

```bash
python crear_indice.py
```

Se generarán automáticamente:

```
data/vectorstore/index.faiss

data/vectorstore/index.pkl
```

Este proceso solo debe ejecutarse nuevamente cuando se agreguen o modifiquen documentos.

---

## 7. Ejecutar el servidor

```bash
python app.py
```

El sistema quedará disponible en:

```
http://127.0.0.1:5000
```

---

# Flujo de funcionamiento

```
Documentos PDF
        │
        ▼
crear_indice.py
        │
        ▼
Embeddings
        │
        ▼
FAISS
        │
        ▼
Índice persistente
        │
──────────────
        │
Pregunta del usuario
        │
        ▼
Búsqueda semántica
        │
        ▼
Fragmentos relevantes
        │
        ▼
OpenRouter
        │
        ▼
Respuesta del asistente
```

---

# Variables de entorno

| Variable | Descripción |
|-----------|-------------|
| OPENROUTER_API_KEY | API Key de OpenRouter |
| MODEL_NAME | Modelo de lenguaje |
| EMBEDDING_MODEL | Modelo de embeddings |
| CHUNK_SIZE | Tamaño de los fragmentos |
| CHUNK_OVERLAP | Superposición entre fragmentos |
| TOP_K | Número de documentos recuperados |
| SIMILARITY_THRESHOLD | Umbral de similitud |

---

# API

## Estado del servidor

```
GET /health
```

Respuesta:

```json
{
  "success": true,
  "message": "BimBam Agent v2.0 funcionando correctamente."
}
```

---

## Consultar al asistente

```
POST /preguntar
```

Body:

```json
{
    "pregunta":"¿Cómo funciona una garantía?"
}
```

Respuesta:

```json
{
    "success": true,
    "data":{
        "respuesta":"..."
    }
}
```

---

# Modelos compatibles

El proyecto puede utilizar cualquier modelo disponible en OpenRouter.

Ejemplos:

- meta-llama/llama-3.3-70b-instruct
- deepseek/deepseek-chat-v3
- qwen/qwen3-235b-a22b
- openai/gpt-5
- anthropic/claude-sonnet-4

Solo es necesario modificar:

```
MODEL_NAME
```

en el archivo `.env`.

---

# Despliegue

El proyecto está preparado para ejecutarse en:

- PythonAnywhere
- Railway
- Render
- Docker

---

# Roadmap

Próximas mejoras:

- Historial de conversaciones.
- Memoria por usuario.
- Citas del documento utilizado.
- Referencia de página.
- Panel administrativo.
- Streaming de respuestas.
- OCR para documentos escaneados.
- Soporte para Word, Excel y PowerPoint.
- Estadísticas de uso.

---

# Licencia

Proyecto desarrollado para **BimBam Buy**.

---

# Autor

Desarrollado por **EditionDP** con apoyo de **ChatGPT (OpenAI)** como asistente para el diseño, desarrollo y optimización del sistema RAG.