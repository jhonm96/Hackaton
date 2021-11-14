from src.model.Usuario import Usuario
from werkzeug.security import check_password_hash


def autenticacion_usuario(email, password):
    usuario = Usuario.filter(email = email)[0]

    if usuario:
        password_user = usuario.password
        if check_password_hash(password_user, password):
            return usuario
        else:
            return False
    else:
        return False
