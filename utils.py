"""
=========================================================
BimBam Agent v2.0
Funciones auxiliares
=========================================================
"""

from pathlib import Path
from datetime import datetime
import logging
import os

from utils import banner
from utils import configurar_logger
from utils import listar_pdfs
from utils import tiempo_legible


# =====================================================
# Crear carpeta si no existe
# =====================================================

def crear_directorio(ruta):

    ruta = Path(ruta)

    ruta.mkdir(parents=True, exist_ok=True)

    return ruta


# =====================================================
# Fecha y hora actual
# =====================================================

def ahora():

    return datetime.now()


# =====================================================
# Fecha en formato legible
# =====================================================

def fecha_hora():

    return ahora().strftime("%Y-%m-%d %H:%M:%S")


# =====================================================
# Crear logger
# =====================================================

def configurar_logger(nombre, carpeta_logs="logs"):

    crear_directorio(carpeta_logs)

    logger = logging.getLogger(nombre)

    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    archivo_log = Path(carpeta_logs) / f"{nombre}.log"

    formatter = logging.Formatter(

        "%(asctime)s | %(levelname)s | %(message)s"

    )

    file_handler = logging.FileHandler(

        archivo_log,

        encoding="utf-8"

    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger


# =====================================================
# Obtener tamaño archivo
# =====================================================

def tamaño_archivo(path):

    archivo = Path(path)

    if not archivo.exists():

        return 0

    return round(

        archivo.stat().st_size / 1024,

        2

    )


# =====================================================
# Validar PDF
# =====================================================

def es_pdf(path):

    archivo = Path(path)

    return (

        archivo.exists()

        and

        archivo.suffix.lower() == ".pdf"

    )


# =====================================================
# Listar PDFs
# =====================================================

def listar_pdfs(carpeta):

    carpeta = Path(carpeta)

    return sorted(

        carpeta.glob("*.pdf")

    )


# =====================================================
# Contar PDFs
# =====================================================

def contar_pdfs(carpeta):

    return len(

        listar_pdfs(carpeta)

    )


# =====================================================
# Formatear segundos
# =====================================================

def tiempo_legible(segundos):

    if segundos < 60:

        return f"{round(segundos,2)} segundos"

    minutos = int(segundos // 60)

    segundos = int(segundos % 60)

    return f"{minutos} min {segundos} seg"


# =====================================================
# Banner
# =====================================================

def banner():

    print()

    print("=" * 60)

    print("        BimBam Agent v2.0")

    print("=" * 60)

    print()


# =====================================================
# Línea separadora
# =====================================================

def linea():

    print("-" * 60)


# =====================================================
# Verificar archivos
# =====================================================

def existe(path):

    return Path(path).exists()


# =====================================================
# Obtener extensión
# =====================================================

def extension(path):

    return Path(path).suffix.lower()


# =====================================================
# Nombre sin extensión
# =====================================================

def nombre_archivo(path):

    return Path(path).stem


# =====================================================
# Tamaño de carpeta
# =====================================================

def tamaño_directorio(carpeta):

    total = 0

    carpeta = Path(carpeta)

    for archivo in carpeta.rglob("*"):

        if archivo.is_file():

            total += archivo.stat().st_size

    return round(total / 1024 / 1024, 2)


# =====================================================
# Limpiar consola
# =====================================================

def limpiar_consola():

    os.system("cls" if os.name == "nt" else "clear")