import peewee

import basedatos

class Usuario(peewee.Model):
    id_usuario = peewee.PrimaryKeyField()
    cedula = peewee.CharField(max_length=50, unique=True)
    nombre = peewee.CharField(max_length=50)
    apellido = peewee.CharField(max_length=50)
    sexo = peewee.CharField(max_length=1)
    fecha_n = peewee.DateField()
    direccion = peewee.CharField(max_length=250)
    ciudad = peewee.CharField(max_length=250)
    acum_compras = peewee.DoubleField()
    n_bonos = peewee.IntegerField()
    username = peewee.CharField(max_length=50)
    email = peewee.CharField(max_length=250)
    password = peewee.CharField(max_length=250)
    cargo = peewee.CharField(max_length=250)
    role = peewee.IntegerField()

    class Meta:
        database = basedatos.obtener_database()
        db_table = 'usuario'

def crearTabla():
    if not Usuario.table_exists():
        Usuario.create_table()