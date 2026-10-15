from pydantic import BaseModel

class CategoriasRequest(BaseModel):
    nome: str
