import peewee

import basedatos

class role(peewee.Model):
    id_roles = peewee.PrimaryKeyField()
    rol = peewee.CharField()
    
    class Meta:
        database = basedatos.obtener_database()
        db_table = 'Roles'

def crearTabla():
    if not role.table_exists():
        role.create_table()