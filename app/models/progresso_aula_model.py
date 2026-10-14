from app.database.database import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, UniqueConstraint

class ProgressoAula(Base):
    __tablename__ = "progresso_aulas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    matricula_id = Column(Integer, ForeignKey("matriculas.id"), nullable=False)
    aula_id = Column(Integer, ForeignKey("aulas.id"), nullable=False)
    concluida_em = Column(DateTime(timezone=True), nullable=False)

    __table_args__ = (
        UniqueConstraint("matricula_id", "aula_id"),
    )
