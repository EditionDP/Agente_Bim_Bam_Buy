"""
=========================================================
BimBam Agent v2.0
Archivo de configuración central
=========================================================
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# -------------------------------------------------------
# Cargar variables de entorno
# -------------------------------------------------------

load_dotenv()

# -------------------------------------------------------
# Directorios principales
# -------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

PDF_DIR = DATA_DIR / "documentos_pdf"

VECTORSTORE_DIR = DATA_DIR / "vectorstore"

LOG_DIR = DATA_DIR / "logs"

UPLOAD_DIR = DATA_DIR / "uploads"

# Crear carpetas automáticamente
for carpeta in [
    DATA_DIR,
    PDF_DIR,
    VECTORSTORE_DIR,
    LOG_DIR,
    UPLOAD_DIR,
]:
    carpeta.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------
# OpenRouter
# -------------------------------------------------------

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

# Modelo principal
MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "meta-llama/llama-3.3-70b-instruct"
)

# -------------------------------------------------------
# Embeddings
# -------------------------------------------------------

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)

# -------------------------------------------------------
# FAISS
# -------------------------------------------------------

FAISS_INDEX_FILE = VECTORSTORE_DIR / "index.faiss"

FAISS_METADATA_FILE = VECTORSTORE_DIR / "index.pkl"

BASE_DIR = Path(__file__).resolve().parent


# -------------------------------------------------------
# Chunking
# -------------------------------------------------------

CHUNK_SIZE = 500

CHUNK_OVERLAP = 80

# -------------------------------------------------------
# Retrieval
# -------------------------------------------------------

TOP_K = 5

SIMILARITY_THRESHOLD = 0.35

# -------------------------------------------------------
# Flask
# -------------------------------------------------------

HOST = "0.0.0.0"

PORT = int(os.getenv("PORT", 5000))

DEBUG = os.getenv("DEBUG", "False").lower() == "true"

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "bimbam-agent-v2"
)

# -------------------------------------------------------
# Chat
# -------------------------------------------------------

MAX_HISTORY = 8

TEMPERATURE = 0

MAX_TOKENS = 1200

# -------------------------------------------------------
# Administrador
# -------------------------------------------------------

ADMIN_USER = os.getenv("ADMIN_USER", "admin")

ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD", "admin123")

# -------------------------------------------------------
# Empresa
# -------------------------------------------------------

COMPANY_NAME = "BimBam Buy"

BOT_NAME = "BimBam Agent"

BOT_DESCRIPTION = (
    "Asistente Inteligente de BimBam"
)

# -------------------------------------------------------
# Prompt del sistema
# -------------------------------------------------------

SYSTEM_PROMPT = """
Eres BimBam Agent.

Eres el asistente inteligente oficial de BimBam Buy.

Tu conocimiento proviene exclusivamente de la base documental de la empresa.

Responde únicamente utilizando la información encontrada en los documentos cargados.

Si la información proviene de varios documentos, intégrala en una sola respuesta coherente.

Si la respuesta no existe en la base documental responde exactamente:

"No lo sé. Intenta otra pregunta."

No inventes información.

Siempre responde en español, de manera clara, profesional y amable.
"""