import peewee

import basedatos

class lista(peewee.Model):
    id_lista = peewee.PrimaryKeyField()
    id_usuario = peewee.CharField()
    cod_prod = peewee.CharField()
    nombre_lista = peewee.CharField()
    precio_und = peewee.IntegerField()
    precio_total = peewee.IntegerField()

    class Meta:
        database = basedatos.obtener_database()
        db_table = 'Lista'


def crearTabla():
    if not lista.table_exists():
        lista.create_table()
        