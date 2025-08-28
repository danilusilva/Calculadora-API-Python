from pydantic import BaseModel
from typing import Optional
class OperacaoDoisNumeros(BaseModel):
    a:float
    b:float

class Operacao(BaseModel):
    radicando:float
    indice:float = 2

class Usuario(BaseModel):
    username:str
    password:str
    nome: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[float] = None

class UsuarioLogin(BaseModel):
    username:str
    password:str