import peewee

import basedatos

class producto_baja(peewee.Model):
    id_baja = peewee.PrimaryKeyField()
    cod_prod = peewee.CharField()
    f_baja = peewee.DateField()
    lote = peewee.CharField()
    n_bajas = peewee.IntegerField()
    razon = peewee.CharField()
    

    class Meta:
        database = basedatos.obtener_database()
        db_table = 'Producto_baja'

def crearTabla():
    if not producto_baja.table_exists():
        producto_baja.create_table()