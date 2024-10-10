import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# Conexão com banco de dados.
Session = sessionmaker(bin = db)
session = Session()

# I/O
# I = input (Entrada)
# O = output (Saída)

# Abrindo uma conexão.

Base = declarative_base()

# Criado tabela.
class Usuario(Base):
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha