from app.database.database import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, UniqueConstraint
from app.utils.horario import horario_br

class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    curso_id = Column(Integer, ForeignKey("cursos.id"), nullable=False)
    matriculado_em = Column(DateTime(timezone=True), default=horario_br, nullable=False)

    __table_args__ = (
        UniqueConstraint("user_id", "curso_id"),
    )
