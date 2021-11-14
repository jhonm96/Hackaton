from peewee import *
from src.model.basedatos import db
from datetime import datetime

class Usuario(Model):
    id = PrimaryKeyField()
    cedula = CharField(max_length=50, unique=True)
    nombre = CharField(max_length=50)
    sexo = CharField(max_length=1)
    fecha_nac = DateField()
    direccion = CharField(max_length=250)
    ciudad = CharField(max_length=250)
    acum_compras = DoubleField(default=0)
    n_bonos = IntegerField(default=0)
    username = CharField(max_length=50)
    email = CharField(max_length=250, unique=True)
    password = CharField(max_length=250)
    role = CharField(max_length=50, default='usuario externo')
    fecha_creacion = DateField(default=datetime.today().strftime('%Y-%m-%d'))

    class Meta:
        database = db
        db_table = 'usuario'
        