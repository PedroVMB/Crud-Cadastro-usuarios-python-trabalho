from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from user import User
from services import UserManager


engine = create_engine('postgresql://postgres:root123@localhost/cadastro_usuarios')

Session = sessionmaker(bind=engine)
session = Session()

user_manager = UserManager(session)

# Obter o usuário que deseja excluir (por exemplo, pelo email)
user_to_delete = user_manager.get_user_by_email("teste@example.com")

# Verificar se o usuário existe
if user_to_delete is not None:
    # Excluir o usuário do banco de dados
    user_manager.delete_user(user_to_delete)
else:
    print("Usuário não encontrado.")
