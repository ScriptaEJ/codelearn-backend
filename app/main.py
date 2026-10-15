from fastapi import FastAPI
from app.routes.categorias_routes import categorias_router
from app.exceptions.exceptions import CategoriaSemNomeException, CategoriaExistenteException
from app.exceptions.handlers import categoria_sem_nome, categoria_ja_existe
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# ---------------- CORS ----------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

origins = [
    "http://localhost:5173",
    "*", 
]

# ------------------ HANDLERS ------------------

app.add_exception_handler(
    CategoriaSemNomeException,
    categoria_sem_nome
)

app.add_exception_handler(
    CategoriaExistenteException,
    categoria_ja_existe
)

# ------------------ HANDLERS ------------------

app.include_router(categorias_router, prefix='/api')


@app.get('/')
def root():
    return {'status_api': 'active'}

