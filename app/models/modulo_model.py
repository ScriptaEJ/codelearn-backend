from app.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint


class Modulo(Base):
    __tablename__ = "modulos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    curso_id = Column(Integer, ForeignKey("cursos.id", ondelete="CASCADE"), nullable=False)
    titulo = Column(String(100), nullable=False)
    ordem = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint("curso_id", "ordem"),
    )
