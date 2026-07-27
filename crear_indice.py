"""
=========================================================
BimBam Agent v2.0
Crear índice FAISS
=========================================================

Uso:

python crear_indice.py
"""

import time
from pathlib import Path

from rag_manager import RAGManager
import config


def banner():

    print("=" * 60)
    print("      BimBam Agent v2.0")
    print("      Constructor de Índice FAISS")
    print("=" * 60)
    print()


def verificar_pdf():

    pdfs = list(config.PDF_DIR.glob("*.pdf"))

    if len(pdfs) == 0:

        print("❌ No se encontraron archivos PDF.")
        print()
        print(f"Carpeta esperada:")
        print(config.PDF_DIR)
        return False

    print(f"📄 PDFs encontrados: {len(pdfs)}")

    for pdf in pdfs:

        tamaño = round(pdf.stat().st_size / 1024, 2)

        print(f"   • {pdf.name} ({tamaño} KB)")

    print()

    return True


def crear():

    banner()

    if not verificar_pdf():

        return

    inicio = time.time()

    rag = RAGManager()

    print()

    print("🚀 Construyendo índice...")

    rag.crear_indice()

    fin = time.time()

    segundos = round(fin - inicio, 2)

    print()

    print("=" * 60)

    print("✅ Índice generado correctamente")

    print("=" * 60)

    print()

    print("Resumen")

    print("---------------------------")

    print(f"Empresa : {config.COMPANY_NAME}")

    print(f"Bot     : {config.BOT_NAME}")

    print(f"Modelo  : {config.MODEL_NAME}")

    print(f"Embeds  : {config.EMBEDDING_MODEL}")

    print()

    info = rag.info_indice()

    print(f"Vectores : {info['vectores']}")

    print(f"Top K    : {config.TOP_K}")

    print()

    print("Archivos generados")

    print("---------------------------")

    print(config.FAISS_INDEX_FILE)

    print(config.FAISS_METADATA_FILE)

    print()

    print(f"Tiempo total: {segundos} segundos")

    print()

    print("Proceso finalizado correctamente.")


if __name__ == "__main__":

    crear()
    