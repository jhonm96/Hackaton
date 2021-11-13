import peewee

import basedatos

class producto(peewee.Model):
    cod_prod = peewee.PrimaryKeyField()
    nombre_prod = peewee.CharField()
    cantidad = peewee.IntegerField()
    presentacion = peewee.CharField()
    precio_und = peewee.IntegerField()
    desc_promo = peewee.IntegerField()
    und_vendidas = peewee.IntegerField()
    total_venta = peewee.IntegerField()
    calif_prom = peewee.IntegerField()
    desc_promo = peewee.IntegerField()
    apl_desc = peewee.CharField()
    acum_desc = peewee.IntegerField()
    id_coment = peewee.IntegerField()

    class Meta:
        database = basedatos.obtener_database()
        db_table = 'Producto'

def crearTabla():
    if not producto.table_exists():
        producto.create_table()