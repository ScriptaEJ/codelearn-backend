from app.database.database import Base
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum
from app.utils.horario import horario_br

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(200), unique=True, nullable=False)
    senha_hash = Column(String(255), nullable=False)
    perfil = Column(Enum("user", "admin", name="perfil_usuario"), default="user", nullable=False)
    ativo = Column(Boolean, default=True, nullable=False)
    criado_em = Column(DateTime(timezone=True), default=horario_br, nullable=False)
    token_verificacao = Column(String(255))
    tentativas_login = Column(Integer, default=0, nullable=False)
    bloqueado_ate = Column(DateTime)
    vezes_bloqueado = Column(Integer, default=0, nullable=False)
