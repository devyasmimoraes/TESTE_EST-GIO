from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal, Base, engine
from app.models import Noticia
from app.crud import criar_noticia, listar_noticias, obter_noticia_por_id, atualizar_noticia, deletar_noticia
from app.schemas import NoticiaCriar, NoticiaAtualizar

app = FastAPI()

# Criar as tabelas no banco
Base.metadata.create_all(bind=engine)

# Dependência para obter a sessão do banco de dados
def obter_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def ler_raiz():
    return {"mensagem": "API de Notícias"}

@app.get("/noticias/")
def listar_noticias_endpoint(pular: int = 0, limite: int = 10, db: Session = Depends(obter_db)):
    return listar_noticias(db, pular=pular, limite=limite)

@app.get("/noticias/{noticia_id}")
def ler_noticia(noticia_id: int, db: Session = Depends(obter_db)):
    noticia = obter_noticia_por_id(db, noticia_id)
    if noticia is None:
        raise HTTPException(status_code=404, detail="Notícia não encontrada")
    return noticia

@app.post("/noticias/")
def criar_noticia_endpoint(noticia: NoticiaCriar, db: Session = Depends(obter_db)):
    return criar_noticia(db, noticia.titulo, noticia.conteudo, noticia.autor, noticia.publicado)

@app.put("/noticias/{noticia_id}")
def atualizar_noticia_endpoint(noticia_id: int, noticia: NoticiaAtualizar, db: Session = Depends(obter_db)):
    noticia_atualizada = atualizar_noticia(db, noticia_id, noticia.titulo, noticia.conteudo, noticia.autor, noticia.publicado)
    if noticia_atualizada is None:
        raise HTTPException(status_code=404, detail="Notícia não encontrada")
    return noticia_atualizada

@app.delete("/noticias/{noticia_id}")
def deletar_noticia_endpoint(noticia_id: int, db: Session = Depends(obter_db)):
    noticia = deletar_noticia(db, noticia_id)
    if noticia is None:
        raise HTTPException(status_code=404, detail="Notícia não encontrada")
    return {"mensagem": "Notícia removida com sucesso"}
