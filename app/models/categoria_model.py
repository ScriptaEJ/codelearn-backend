from app.database.database import Base
from sqlalchemy import Column, Integer, String


class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(60), unique=True, nullable=False)
