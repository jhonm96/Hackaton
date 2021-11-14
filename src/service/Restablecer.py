from src.model.Usuario import Usuario
from src.service.Mailer import enviar_correo
from werkzeug.security import generate_password_hash

def restablecer_password(password_anterior, password, ver_password):
    usuario = Usuario.filter(password = password_anterior)[0]

    if usuario:
        asunto = 'Contrasena Restablecida'
        mensaje = 'Hola, tu contrasena ha sido cambiada'

        usuario.password = generate_password_hash(password)
        usuario.save()

        enviar_correo(asunto, mensaje, usuario.email)
    else:
        return False
