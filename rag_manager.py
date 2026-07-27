import os
import logging
from pathlib import Path
from config import FAISS_INDEX_FILE

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import *

logging.basicConfig(level=logging.INFO)


class RAGManager:

    def __init__(self):

        self.llm = self._cargar_llm()

        self.embeddings = self._cargar_embeddings()

        self.vectorstore = None

        self.retriever = None

        # Cargar índice automáticamente
        if Path(FAISS_INDEX_FILE).exists():

            logging.info("Cargando índice FAISS...")

            self.cargar_indice()

        else:

            logging.warning("No existe un índice FAISS.")
    
    # ==========================================
    # Cargar el modelo LLM
    # ==========================================
    def _cargar_llm(self):

        logging.info("Cargando modelo LLM...")
        

        return ChatOpenAI(
            model=MODEL_NAME,
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_BASE_URL,
            temperature=TEMPERATURE
        )
   
    # ==========================================
    # Cargar modelo de Embeddings
    # ==========================================
    ef _cargar_embeddings(self):

    logging.info("Cargando modelo de Embeddings...")

    return HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL,
        model_kwargs={
            "device": "cpu"
        },
        encode_kwargs={
            "normalize_embeddings": True,
            "batch_size": 8
        }
    )
    
    # ==========================================
    # Crear índice FAISS
    # ==========================================
    def crear_indice(self):

        logging.info("Creando índice FAISS...")
        print("PDF_DIR =", PDF_DIR)
        print("Ruta absoluta =", Path(PDF_DIR).resolve())
        print("Existe =", Path(PDF_DIR).exists())

        documentos = []
        print(list(Path(PDF_DIR).glob("*.pdf")))

        for archivo in Path(PDF_DIR).glob("*.pdf"):

            logging.info(f"Leyendo: {archivo.name}")

            loader = PyMuPDFLoader(str(archivo))

            documentos.extend(loader.load())

        if not documentos:
            raise Exception("No se encontraron documentos PDF.")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

        chunks = splitter.split_documents(documentos)

        self.vectorstore = FAISS.from_documents(
            chunks,
            self.embeddings
        )

        self.guardar_indice()

        self.retriever = self.vectorstore.as_retriever(
            search_kwargs={"k": 4}
        )

        logging.info("Índice creado correctamente.")


    # ==========================================
    # Guardar índice
    # ==========================================
    def guardar_indice(self):
        Path(VECTORSTORE_DIR).mkdir(
            parents=True,
            exist_ok=True
            )
        self.vectorstore.save_local(
            str(VECTORSTORE_DIR)
            )
        logging.info("Índice guardado correctamente.")
    # ==========================================
    # Cargar índice existente
    # ==========================================
    def cargar_indice(self):
        if not (Path(VECTORSTORE_DIR) / "index.faiss").exists():
            logging.warning("No existe un índice FAISS.")
            return False

        self.vectorstore = FAISS.load_local(
            
            str(VECTORSTORE_DIR),

            self.embeddings,

            allow_dangerous_deserialization=True

            )
        
        self.retriever = self.vectorstore.as_retriever(

            search_kwargs={"k": 4}

            )

        logging.info("Índice cargado correctamente.")

        return True   

    # ==========================================
    # Realizar una consulta al RAG
    # ==========================================
    def preguntar(self, pregunta):

        if self.retriever is None:

            if not self.cargar_indice():
                return "No existe un índice FAISS. Ejecute crear_indice.py primero."

        try:
            import gc
            
            gc.collect()

            documentos = self.retriever.invoke(pregunta)

            if not documentos:
                return "No encontré información relacionada con tu consulta."

            contexto = "\n\n".join(
                doc.page_content for doc in documentos
            )

            prompt = f"""
Eres BimBam Agent.

Eres el asistente inteligente oficial de BimBam Buy.

Tu conocimiento proviene exclusivamente de la base documental de la empresa.

Responde únicamente utilizando la información encontrada en los documentos cargados.

Si la información proviene de varios documentos, intégrala en una sola respuesta coherente.

Si la respuesta no existe en la base documental responde exactamente:

"No lo sé. Intenta otra pregunta."

No inventes información.

Siempre responde en español, de manera clara, profesional y amable.

Contexto:
{contexto}

Pregunta:
{pregunta}
"""

            respuesta = self.llm.invoke(prompt)

            return respuesta.content

        except Exception as e:

            logging.error(e)

            return "Ocurrió un error al procesar la consulta."


    # ==========================================
    # Estado del sistema
    # ==========================================
    def estado(self):

        return {
            "modelo": MODEL_NAME,
            "embeddings": EMBEDDING_MODEL,
            "indice_cargado": self.vectorstore is not None,
            "carpeta_pdf": PDF_DIR,
            "carpeta_faiss": VECTORSTORE_DIR,
        }


    # ==========================================
    # Listar documentos PDF
    # ==========================================
    def listar_documentos(self):

        archivos = []

        for archivo in Path(PDF_DIR).glob("*.pdf"):

            archivos.append(archivo.name)

        return archivos
    # ==========================================
    # Información del índice
    # ==========================================
    def info_indice(self):
        total_pdfs = len(list(Path(PDF_DIR).glob("*.pdf")))
        total_chunks = 0
        if self.vectorstore is not None:
            try:
                total_chunks = self.vectorstore.index.ntotal
            except Exception:
                pass

        return {
            "empresa": COMPANY_NAME,
            "bot": BOT_NAME,
            "modelo": MODEL_NAME,
            "embeddings": EMBEDDING_MODEL,
            "pdfs": total_pdfs,
            "vectores": total_chunks,
            "vectorstore": str(VECTORSTORE_DIR)
            }


