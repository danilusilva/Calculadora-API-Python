from fastapi import APIRouter, HTTPException
from ..models import Usuario, UsuarioLogin
from ..auth import get_usuario, gerar_hash
router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.get("/teste")
def testar():
    return {"Mensagem: ":"Rota de usuários funcionando!"}


@router.post("/registro")
def registrar(usuario: Usuario):
    if get_usuario(usuario.username):
        raise HTTPException(status_code=400, detail="Usuário já existe!")
    
    hash_senha = gerar_hash(usuario.password)
    return {"Mensagem: ":f"Seja bem vindo {usuario.username} {hash_senha}!"}

@router.post("/login")
def login(usuario: UsuarioLogin):
    return {"Mensagem: ":f"Usuário {usuario.username} logado com sucesso!"}