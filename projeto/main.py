import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# Conexão com banco de dados.
Session = sessionmaker(bind = db)
session = Session()

# Criado tabela.
Base = declarative_base()

class Usuario(Base):
    # Definindo nome da tabela.
    __tablename__ = "usuarios"

    # Definindo atributos da tabela.
    id = Column("id", Integer, primary_key = True, autoincrement= True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributos da classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind = db)

# Salvar no banco de dados.
# usuario = Usuario("Marta", "marta@gmail.com", "123")
# Equivalente ao INSERT INTO TABLE
usuario = Usuario(nome= "Marta", email= "marta@gmail.com", senha= "123")
session.add(usuario)
session.commit()

# Mostrando conteúdo do banco de dados.
# Equivalente ao SELECT * FROM
# VIEWS - SELECT 
lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id} - {usuario.nome} - {usuario.email}")