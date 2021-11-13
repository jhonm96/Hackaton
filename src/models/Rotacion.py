import peewee

import basedatos

class rotacion(peewee.Model):
    id_rotacion = peewee.PrimaryKeyField()
    cod_prod = peewee.CharField()
    categoria = peewee.CharField()
    
    class Meta:
        database = basedatos.obtener_database()
        db_table = 'Rotacion'

def crearTabla():
    if not rotacion.table_exists():
        rotacion.create_table()