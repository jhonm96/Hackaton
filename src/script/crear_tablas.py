from src.model.Usuario import Usuario
from src.model.Producto import Producto
from src.model.Lote import Lote
from src.model.Compra import Compra

def crear_tablas():
    if not Usuario.table_exists():
        Usuario.create_table()

    if not Producto.table_exists():
        Producto.create_table()

    if not Lote.table_exists():
        Lote.create_table()

    if not Compra.table_exists():
        Compra.create_table()