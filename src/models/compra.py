import peewee

import basedatos

class compra(peewee.Model):
    id_compra = peewee.PrimaryKeyField()
    cod_prod = peewee.CharField()
    id_usuario = peewee.CharField()
    f_compra = peewee.DateField()
    cantidad = peewee.IntegerField()
    precio_und = peewee.IntegerField()
    precio_total = peewee.IntegerField()

    class Meta:
        database = basedatos.obtener_database()
        db_table = 'Compra'

def crearTabla():
    if not compra.table_exists():
        compra.create_table()