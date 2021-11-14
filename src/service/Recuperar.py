from src.model.Usuario import Usuario
from src.service.Mailer import enviar_correo

def recuperar_datos(email):
    usuario = Usuario.filter(email = email)[0]

    if usuario:
        asunto = 'Recuperacion de datos'
        mensaje = 'Hola, tus datos son:\n\n Nombre: {}\n Sexo:{}\n Fecha de nacimiento: {}\n Direccion: {}\n Ciudad: {}\n Nombre de usuario: {}\n Correo: {}\n Hash contrasena: {}'.format(usuario.nombre, usuario.sexo, usuario.fecha_nac, usuario.direccion, usuario.ciudad, usuario.username, usuario.email, usuario.password)

        enviar_correo(asunto, mensaje, email)
    else:
        return False


