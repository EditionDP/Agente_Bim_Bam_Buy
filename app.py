"""
=========================================================
BimBam Agent v2.0
Aplicación principal
=========================================================
"""

from flask import Flask
from flask_cors import CORS

# Configuración
import config

# Rutas
from routes import api


def create_app():
    """
    Crea e inicializa la aplicación Flask.
    """

    app = Flask(
        __name__,
        static_folder="static",
        template_folder="templates"
    )

    # -----------------------------
    # Configuración Flask
    # -----------------------------

    app.config["SECRET_KEY"] = config.SECRET_KEY

    # -----------------------------
    # CORS
    # -----------------------------

    CORS(
        app,
        
        resources={
            r"/*": {
                "origins": [
                    "https://agentebimbam.netlify.app/",
                    "http://localhost:3000",
                    "http://127.0.0.1:3000",
                ]
            }
        }
    )

    # -----------------------------
    # Registrar Blueprint
    # -----------------------------

    app.register_blueprint(api)
    
    return app


# =====================================================
# Crear aplicación
# =====================================================

app = create_app()


# =====================================================
# Inicio
# =====================================================

if __name__ == "__main__":

    app.run(

        host=config.HOST,

        port=config.PORT,

        debug=config.DEBUG

    )

@app.route("/")
def home():
    return {
        "success": True,
        "message": "BimBam Agent v2.0 funcionando correctamente."
    }
