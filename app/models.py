from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base

class Noticia(Base):
    __tablename__ = "noticias"
    
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    conteudo = Column(String)
    autor = Column(String)
    publicado = Column(Boolean, default=False)
    data_criacao = Column(DateTime, default=func.now())
