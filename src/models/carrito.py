import peewee

database = peewee.MySQLDatabase('hackaton', host='localhost', port=3306, user='root', password='root')

class carrito(peewee.Model):
    id_carrito = peewee.PrimaryKeyField()
    id_usuario = peewee.CharField()
    cod_prod = peewee.CharField()
    precio_und = peewee.IntegerField()
    precio_total = peewee.IntegerField()

    class Meta:
        database = database
        db_table = 'Carrito'

if __name__ == '__main__':
    if not carrito.table_exists():
        carrito.create_table()