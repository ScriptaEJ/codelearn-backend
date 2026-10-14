from app.database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime, Text, Enum
from app.utils.horario import horario_br

class Curso(Base):
    __tablename__ = "cursos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    categoria_id = Column(Integer, ForeignKey("categorias.id"), nullable=False)
    titulo = Column(String(150), nullable=False)
    descricao = Column(Text)
    professor = Column(String(100), nullable=False)
    nivel = Column(Enum("iniciante", "intermediario", "avancado", name="nivel_curso"), nullable=False)
    ativo = Column(Boolean, default=True, nullable=False)
    criado_em = Column(DateTime(timezone=True), default=horario_br, nullable=False)
