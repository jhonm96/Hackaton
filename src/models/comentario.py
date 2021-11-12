import peewee

database = peewee.MySQLDatabase('hackaton', host='localhost', port=3306, user='root', password='root')

class comentarios(peewee.Model):
    id_coment = peewee.PrimaryKeyField()
    cod_prod = peewee.CharField()
    id_usuario = peewee.CharField()
    fecha = peewee.DateField()
    calificacion = peewee.IntegerField()
    comentario = peewee.CharField()
    

    class Meta:
        database = database
        db_table = 'Comentarios'

if __name__ == '__main__':
    if not comentarios.table_exists():
        comentarios.create_table()