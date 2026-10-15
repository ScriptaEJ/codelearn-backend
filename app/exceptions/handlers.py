from fastapi import Request
from fastapi.responses import JSONResponse

from app.exceptions.exceptions import CategoriaSemNomeException, CategoriaExistenteException

async def categoria_sem_nome(request: Request, exc: CategoriaSemNomeException):
    return JSONResponse(
        status_code=400,
        content={
            'detail': exc.message
        }
    )

async def categoria_ja_existe(request: Request, exc: CategoriaExistenteException):
    return JSONResponse(
        status_code=409,
        content={
            'detail': exc.message
        }
    )