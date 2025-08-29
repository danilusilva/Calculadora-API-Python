from fastapi import APIRouter, HTTPException
from ..models import Usuario, UsuarioLogin
from ..auth import get_usuario, gerar_hash, autenticar_usuario, criar_token
from ..database import usuarios
from datetime import timedelta
from ..config import ACCESS_TOKEN_EXPIRE_MINUTES
router = APIRouter(prefix="/usuarios", tags=["Usuários"])

@router.get("/teste")
def testar():
    return {"Mensagem: ":"Rota de usuários funcionando!"}


@router.post("/registro")
def registrar(usuario: Usuario):
    if get_usuario(usuario.username):
        raise HTTPException(status_code=400, detail="Usuário já existe!")   
    hash_senha = gerar_hash(usuario.password)
    usuarios.insert_one({"username": usuario.username, "password": hash_senha})
    return {"Mensagem: ":f"Seja bem vindo {usuario.username} {hash_senha}!"}

@router.post("/login")
def logar(usuario: UsuarioLogin):
    autenticado = autenticar_usuario(usuario.username, usuario.password)
    if not autenticado:
        raise HTTPException(status_code=400, detail="Usuário ou senha inválidos!")

    access_token = criar_token(
        data={"sub": autenticado["username"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        )
    return {"access_token": access_token, "token_type": "bearer"}