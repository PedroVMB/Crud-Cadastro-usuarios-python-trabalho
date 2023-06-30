from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import User
from services import UserManager


engine = create_engine('postgresql://postgres:root123@localhost/cadastro_usuarios')

Session = sessionmaker(bind=engine)
session = Session()

user_manager = UserManager(session)

user = User("Teste", "teste@example.com")
user_manager.add_user(user)
