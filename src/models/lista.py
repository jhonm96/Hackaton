import peewee

database = peewee.MySQLDatabase('hackaton', host='localhost', port=3306, user='root', password='root')

class lista(peewee.Model):
    id_lista = peewee.PrimaryKeyField()
    id_usuario = peewee.CharField()
    cod_prod = peewee.CharField()
    nombre_lista = peewee.CharField()
    precio_und = peewee.IntegerField()
    precio_total = peewee.IntegerField()

    class Meta:
        database = database
        db_table = 'Lista'


if __name__ == '__main__':
    if not lista.table_exists():
        lista.create_table()
        