import peewee

database = peewee.MySQLDatabase('hackaton', host='localhost', port=3306, user='root', password='root')

class producto_baja(peewee.Model):
    id_baja = peewee.PrimaryKeyField()
    cod_prod = peewee.CharField()
    f_baja = peewee.DateField()
    lote = peewee.CharField()
    n_bajas = peewee.IntegerField()
    razon = peewee.CharField()
    

    class Meta:
        database = database
        db_table = 'Producto_baja'

if __name__ == '__main__':
    if not producto_baja.table_exists():
        producto_baja.create_table()