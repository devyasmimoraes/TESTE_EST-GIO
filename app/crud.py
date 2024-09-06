from sqlalchemy.orm import Session
from app.models import Noticia

def listar_noticias(db: Session, pular: int = 0, limite: int = 10):
    return db.query(Noticia).offset(pular).limit(limite).all()

def obter_noticia_por_id(db: Session, noticia_id: int):
    return db.query(Noticia).filter(Noticia.id == noticia_id).first()

def criar_noticia(db: Session, titulo: str, conteudo: str, autor: str, publicado: bool):
    noticia = Noticia(titulo=titulo, conteudo=conteudo, autor=autor, publicado=publicado)
    db.add(noticia)
    db.commit()
    db.refresh(noticia)
    return noticia

def atualizar_noticia(db: Session, noticia_id: int, titulo: str, conteudo: str, autor: str, publicado: bool):
    noticia = db.query(Noticia).filter(Noticia.id == noticia_id).first()
    if noticia:
        noticia.titulo = titulo
        noticia.conteudo = conteudo
        noticia.autor = autor
        noticia.publicado = publicado
        db.commit()
        db.refresh(noticia)
    return noticia

def deletar_noticia(db: Session, noticia_id: int):
    noticia = db.query(Noticia).filter(Noticia.id == noticia_id).first()
    if noticia:
        db.delete(noticia)
        db.commit()
    return noticia
