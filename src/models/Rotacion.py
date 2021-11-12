import peewee

database = peewee.MySQLDatabase('hackaton', host='localhost', port=3306, user='root', password='root')

class rotacion(peewee.Model):
    id_rotacion = peewee.PrimaryKeyField()
    cod_prod = peewee.CharField()
    categoria = peewee.CharField()
    
    class Meta:
        database = database
        db_table = 'Rotacion'

if __name__ == '__main__':
    if not rotacion.table_exists():
        rotacion.create_table()