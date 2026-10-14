from app.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint


class Aula(Base):
    __tablename__ = "aulas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    modulo_id = Column(Integer, ForeignKey("modulos.id"), nullable=False)
    titulo = Column(String(100), nullable=False)
    duracao_minutos = Column(Integer, default=0, nullable=False)
    ordem = Column(Integer, nullable=False)
    url_video = Column(String(255))

    __table_args__ = (
        UniqueConstraint("modulo_id", "ordem"),
    )
