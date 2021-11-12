import peewee

database = peewee.MySQLDatabase('hackaton', host='localhost', port=3306, user='root', password='root')

class usuario(peewee.Model):
    id_usuario = peewee.PrimaryKeyField()
    cedula = peewee.CharField()
    nombre = peewee.CharField()
    apellido = peewee.CharField()
    sexo = peewee.CharField()
    fecha_n = peewee.DateField()
    direccion = peewee.CharField()
    ciudad = peewee.CharField()
    acum_compras = peewee.CharField()
    n_bonos = peewee.IntegerField()
    username = peewee.CharField()
    email = peewee.CharField()
    password = peewee.CharField()
    cargo = peewee.CharField()
    role = peewee.IntegerField()

    class Meta:
        database = database
        db_table = 'Usuario'

if __name__ == '__main__':
    if not usuario.table_exists():
        usuario.create_table()