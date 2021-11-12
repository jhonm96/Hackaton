import peewee

database = peewee.MySQLDatabase('hackaton', host='localhost', port=3306, user='root', password='root')

class producto_lote(peewee.Model):
    id_lote = peewee.PrimaryKeyField()
    cod_prod = peewee.CharField()
    lote = peewee.CharField()
    cantidad = peewee.IntegerField()
    desc_promo = peewee.IntegerField()
    f_entrad = peewee.DateField()
    f_ult_salid = peewee.DateField()
    

    class Meta:
        database = database
        db_table = 'Producto_lote'

if __name__ == '__main__':
    if not producto_lote.table_exists():
        producto_lote.create_table()