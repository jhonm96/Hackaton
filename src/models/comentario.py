import peewee

import basedatos

class comentarios(peewee.Model):
    id_coment = peewee.PrimaryKeyField()
    cod_prod = peewee.CharField()
    id_usuario = peewee.CharField()
    fecha = peewee.DateField()
    calificacion = peewee.IntegerField()
    comentario = peewee.CharField()
    

    class Meta:
        database = basedatos.obtener_database()
        db_table = 'Comentarios'

def crearTabla():
    if not comentarios.table_exists():
        comentarios.create_table()