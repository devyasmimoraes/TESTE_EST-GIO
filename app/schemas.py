from pydantic import BaseModel
from typing import Optional

class NoticiaCriar(BaseModel):
    titulo: str
    conteudo: str
    autor: str
    publicado: Optional[bool] = False

class NoticiaAtualizar(BaseModel):
    titulo: str
    conteudo: str
    autor: str
    publicado: Optional[bool] = False
