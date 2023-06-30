from sqlalchemy.orm import sessionmaker

from user import User

class UserManager:
    """Classe para gerenciar usuários."""

    def __init__(self, session):
        """Inicializa uma instância de UserManager.

        Args:
            session: Uma instância da classe Session do SQLAlchemy.
        """
        self.session = session

    def add_user(self, user):
        """Adiciona um usuário ao banco de dados.

        Args:
            user: Um objeto User representando o usuário a ser adicionado.
        """
        self.session.add(user)
        self.session.commit()

    def get_all_users(self):
        """Obtém todos os usuários armazenados.

        Returns:
            Uma lista contendo todos os objetos User armazenados.
        """
        return self.session.query(User).all()

    def get_user_by_email(self, email):
        """Obtém um usuário com base no endereço de e-mail.

        Args:
            email: O endereço de e-mail do usuário a ser encontrado.

        Returns:
            O objeto User correspondente ao endereço de e-mail fornecido.
            Retorna None se nenhum usuário for encontrado.
        """
        return self.session.query(User).filter_by(email=email).first()

    def delete_user(self, user):
        """Exclui um usuário do banco de dados.

        Args:
            user: O objeto User a ser excluído.
        """
        self.session.delete(user)
        self.session.commit()

