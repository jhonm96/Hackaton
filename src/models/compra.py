import peewee

database = peewee.MySQLDatabase('hackaton', host='localhost', port=3306, user='root', password='root')

class compra(peewee.Model):
    id_compra = peewee.PrimaryKeyField()
    cod_prod = peewee.CharField()
    id_usuario = peewee.CharField()
    f_compra = peewee.DateField()
    cantidad = peewee.IntegerField()
    precio_und = peewee.IntegerField()
    precio_total = peewee.IntegerField()

    class Meta:
        database = database
        db_table = 'Compra'

# if __name__ == '__main__':
#     if not compra.table_exists():
#         compra.create_table()