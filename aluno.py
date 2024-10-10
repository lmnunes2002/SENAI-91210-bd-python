import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# Criando banco de dados.
db = create_engine("sqlite:///meubanco.db")

# Conexão com banco de dados.
Session = sessionmaker(bind = db)
session = Session()

# Criando tabela.
Base = declarative_base()

class Aluno(Base):
    # Definindo nome da tabela
    __tablename__ = "alunos"

    # Definindo atributos da tabela.
    ra = Column("ra", Integer, primary_key= True, autoincrement = True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    # Definindo atributas da classe.
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha

# Criando tabela no banco de dados.
Base.metadata.create_all(bind = db)

# Salvar no banco de dados.
# Equivalente ao INSERT INTO TABLE
for i in range(3):
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    aluno = Aluno(nome= nome, email= email, senha= senha)
    session.add(aluno)
    session.commit()

# Mostrando conteúdo do banco de dados.
# Equivalente ao SELECT * FROM
# VIEWS - SELECT
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.ra} - {aluno.nome} - {aluno.email}")

# Deletando um usuário
aluno = session.query(Aluno).filter_by(email = "jose@email.com").first()
session.delete(aluno)
session.commit()
print("\nUsuário deletado com sucesso.")

# Mostrar conteúdo do banco de dados.
print("\nListando usuários no banco de dados.")
lista_alunos = session.query(Aluno).all()

for aluno in lista_alunos:
    print(f"{aluno.ra} - {aluno.nome} - {aluno.email}")