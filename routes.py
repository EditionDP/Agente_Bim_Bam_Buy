"""
=========================================================
BimBam Agent v2.0
API REST
=========================================================
"""

from datetime import datetime

from flask import (
    Blueprint,
    jsonify,
    request
)

from rag_manager import RAGManager


# --------------------------------------------------------
# Blueprint
# --------------------------------------------------------

api = Blueprint("api", __name__)


# --------------------------------------------------------
# Inicializar el motor RAG una sola vez
# --------------------------------------------------------

#rag = RAGManager()
rag = None
rag.cargar_indice()


# --------------------------------------------------------
# Función auxiliar para respuestas JSON
# --------------------------------------------------------

def respuesta(success, message="", data=None, status=200):

    return jsonify({

        "success": success,

        "message": message,

        "timestamp": datetime.utcnow().isoformat(),

        "data": data

    }), status


# --------------------------------------------------------
# Ruta principal
# --------------------------------------------------------

@api.route("/", methods=["GET"])
def home():

    return respuesta(

        True,

        "BimBam Agent v2.0 funcionando correctamente.",

        {

            "version": "2.0",

            "status": "online"

        }

    )


# --------------------------------------------------------
# Estado del servidor
# --------------------------------------------------------

@api.route("/health", methods=["GET"])
def health():

    return respuesta(

        True,

        "Servidor activo.",

        rag.health()

    )


# --------------------------------------------------------
# Estado del índice
# --------------------------------------------------------

@api.route("/status", methods=["GET"])
def status():

    return respuesta(

        True,

        "Estado del sistema.",

        rag.status()

    )


# --------------------------------------------------------
# Chat
# --------------------------------------------------------

@api.route("/preguntar", methods=["POST"])
def preguntar():

    global rag
    
    if rag is None:
        rag = RAGManager()

    datos = request.get_json()

    if not datos:

        return respuesta(

            False,

            "No se recibieron datos.",

            status=400

        )

    pregunta = datos.get("pregunta", "").strip()

    if pregunta == "":

        return respuesta(

            False,

            "Debe escribir una pregunta.",

            status=400

        )

    try:

        resultado = rag.preguntar(pregunta)

        return respuesta(

            True,

            "Consulta realizada correctamente.",

            {

                "respuesta": resultado

            }

        )

    except Exception as e:

        return respuesta(

            False,

            str(e),

            status=500

        )


# --------------------------------------------------------
# Lista de documentos
# --------------------------------------------------------

@api.route("/documentos", methods=["GET"])
def documentos():

    try:

        archivos = rag.listar_documentos()

        return respuesta(

            True,

            "Lista de documentos.",

            {

                "total": len(archivos),

                "documentos": archivos

            }

        )

    except Exception as e:

        return respuesta(

            False,

            str(e),

            status=500

        )


# --------------------------------------------------------
# Reconstrucción del índice
# --------------------------------------------------------

@api.route("/reconstruir", methods=["POST"])
def reconstruir():

    try:

        rag.reconstruir_indice()

        return respuesta(

            True,

            "Índice reconstruido correctamente."

        )

    except Exception as e:

        return respuesta(

            False,

            str(e),

            status=500

        )

@api.route("/estadisticas", methods=["GET"])
def estadisticas():

    return respuesta(

        True,

        "Estadísticas.",

        rag.estadisticas()

    )

@api.route("/indice", methods=["GET"])
def indice():

    return respuesta(

        True,

        "Información del índice.",

        rag.info_indice()

    )

@api.route("/recargar", methods=["POST"])
def recargar():

    rag.recargar_indice()

    return respuesta(

        True,

        "Índice recargado."

    )
