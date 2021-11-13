
from src.models import Carrito, Producto, Usuario, Comentario, Compra, Lista, ProductoBaja, ProductoLote, Roles, Rotacion

def crear_tablas():
    Carrito.crearTabla()
    Producto.crearTabla()
    Usuario.crearTabla()
    Comentario.crearTabla()
    Compra.crearTabla()
    Lista.crearTabla()
    ProductoBaja.crearTabla()
    ProductoLote.crearTabla()
    Roles.crearTabla()
    Rotacion.crearTabla()




