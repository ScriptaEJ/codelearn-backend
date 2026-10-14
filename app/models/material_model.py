from app.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from app.utils.horario import horario_br

class Material(Base):
    __tablename__ = "materiais"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    aula_id = Column(Integer, ForeignKey("aulas.id"), nullable=False)
    nome = Column(String(150), nullable=False)
    url = Column(String(255), nullable=False)
    criado_em = Column(DateTime(timezone=True), default=horario_br, nullable=False)
