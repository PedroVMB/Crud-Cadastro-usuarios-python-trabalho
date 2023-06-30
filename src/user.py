from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Crie uma instância do engine do SQLAlchemy para se conectar ao banco de dados PostgreSQL
engine = create_engine('postgresql://postgres:root123@localhost/cadastro_usuarios')

# Crie uma instância da classe Session do SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Crie uma classe de modelo para a tabela de usuários
Base = declarative_base()

class User(Base):
    """Classe de modelo para a tabela de usuários."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __init__(self, name, email):
        self.name = name
        self.email = email

# Cria a tabela no banco de dados
Base.metadata.create_all(engine)

