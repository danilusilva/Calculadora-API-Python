from fastapi import APIRouter, HTTPException
from ..models import OperacaoDoisNumeros


router = APIRouter(prefix="/calc", tags=["Calculadora"])

@router.post("/somar")
def somar(dados: OperacaoDoisNumeros):
    return {"Resultado: ":dados.a + dados.b}

@router.post("/subtrair")
def subtrair(dados: OperacaoDoisNumeros):
    return {"Resultado: ":dados.a - dados.b}

@router.post("/multiplicar")
def multiplicar(dados: OperacaoDoisNumeros):
    return {"Resultado: ":dados.a * dados.b}


@router.post("/dividir")
def dividir(dados: OperacaoDoisNumeros):
    if dados.b == 0:
        raise HTTPException(status_code=400, detail= "Não é possível divir por zero")
    return {"Resultado: ":dados.a / dados.b}


@router.post("/potenciacao")
def potenciacao(dados: OperacaoDoisNumeros):
    return {"Resultado: ":dados.a ** dados.b}

@router.post("/raiz")
def raiz(dados: OperacaoDoisNumeros):
    resultado =  dados.a ** (1/dados.b)
    return {"Resultado: ":resultado}

