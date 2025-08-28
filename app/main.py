from fastapi import FastAPI
from .routers import calculadora, usuarios

app = FastAPI(titlle="Calculadora Modularizada", description= "Minha Calculadora", version="0.0.2")

app.include_router(calculadora.router)
app.include_router(usuarios.router)