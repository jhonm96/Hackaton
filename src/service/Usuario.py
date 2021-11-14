from src.model.Usuario import Usuario
from src.service.Mailer import enviar_correo

def crear_usuario(cedula, nombre, sexo, fecha_nac, direccion, ciudad, email, password):

    usuario = Usuario( cedula = cedula, nombre = nombre, sexo = sexo, fecha_nac = fecha_nac, direccion = direccion, ciudad = ciudad, username = email, email = email, password = password)

    usuario.save()

    asunto = 'Bienvenido'
    mesnaje = 'Hola {},\n Te damos la bienvenida a nuestra constelación.'
    enviar_correo(asunto, mesnaje.encode(), email)


def crear_usuario_registro(cedula, nombre, sexo, fecha_nac, direccion, ciudad, email, password, cargo):

    usuario = Usuario( cedula = cedula, nombre = nombre, sexo = sexo, fecha_nac = fecha_nac, direccion = direccion, ciudad = ciudad, username = email, email = email, password = password, role = cargo)

    usuario.save()

    asunto = 'Bienvenido'
    mesnaje = 'Hola {},\n Te damos la bienvenida a nuestra constelación.'
    enviar_correo(asunto, mesnaje.encode(), email)


def obtener_usuario(email):
    usuario = Usuario.filter(email = email)[0]

    if usuario:
        return usuario
    else:
        return False

def obtener_usuario_cedula(cedula):
    usuario = Usuario.filter(cedula = cedula)[0]

    if usuario:
        return usuario
    else:
        return False


def actualizar_usuario(usuario, data):
    usuario.nombre = data['nombre']
    usuario.cedula = data['cedula']
    usuario.sexo = data['sexo']
    usuario.fecha_nac = data['fecha_nac']
    usuario.direccion = data['direccion']
    usuario.ciudad = data['ciudad']
    usuario.role = data['role']

    usuario.save()
