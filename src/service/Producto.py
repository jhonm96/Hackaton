from src.model.Producto import Producto

def crear_producto(nombre, codigo, tipo_unidad, fecha_ingreso, bono, precio_unitario, aplica_bono, cantidad_estandar):

    producto = Producto( codigo = codigo, nombre_prod = nombre,
    inventario = cantidad_estandar, presentacion = tipo_unidad, precio_und = precio_unitario, fecha_ingreso = fecha_ingreso, calif_prom  = aplica_bono, apl_desc = aplica_bono, acum_desc = bono )

    producto.save()



    