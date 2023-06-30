from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import User
from services import UserManager


engine = create_engine('postgresql://postgres:root123@localhost/cadastro_usuarios')

Session = sessionmaker(bind=engine)
session = Session()

user_manager = UserManager(session)

user = User("Pedro", "Pedro@example.com")
#user_manager.add_user(user)

user_manager.get_all_users()
users = user_manager.get_all_users()  # Atribui o resultado a uma variável
for user in users:
    print("Nome:", user.name)
    print("ID:", user.id)
    print("Email:", user.email)
    print("--------------------")
