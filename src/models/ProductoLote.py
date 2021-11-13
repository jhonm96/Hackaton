import peewee

import basedatos

class producto_lote(peewee.Model):
    id_lote = peewee.PrimaryKeyField()
    cod_prod = peewee.CharField()
    lote = peewee.CharField()
    cantidad = peewee.IntegerField()
    desc_promo = peewee.IntegerField()
    f_entrad = peewee.DateField()
    f_ult_salid = peewee.DateField()
    

    class Meta:
        database = basedatos.obtener_database()
        db_table = 'Producto_lote'

def crearTabla():
    if not producto_lote.table_exists():
        producto_lote.create_table()