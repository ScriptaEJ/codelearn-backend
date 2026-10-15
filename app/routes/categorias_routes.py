from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.categorias_schema import CategoriasRequest
from app.services.categorias_services import criar_categoria_service
from app.database.database import get_db

categorias_router = APIRouter(tags=['01. Categorias'], prefix='/categorias')

@categorias_router.post('/')
def criar_categoria(data: CategoriasRequest, db: Session = Depends(get_db)):

    criar_categoria_service(data, db)
    return {'message': 'Categoria criada com sucesso!'}