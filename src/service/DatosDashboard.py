from src.model.Compra import Compra
from src.model.Usuario import Usuario
from datetime import datetime

def total_ventas():
    compras = Compra.select()
    return len(compras)

def ventas_hoy():
    compras = Compra.filter( fecha_compra = datetime.today().strftime('%Y-%m-%d'))
    return len(compras)

def total_usuario():
    usuarios = Usuario.select()
    return len(usuarios)

def usuario_nuevos():
    usuarios = Usuario.filter( fecha_creacion = datetime.today().strftime('%Y-%m-%d'))
    return len(usuarios)

def obtener_usuario_nuevos():
    usuarios = Usuario.filter( fecha_creacion = datetime.today().strftime('%Y-%m-%d'))
    return usuarios