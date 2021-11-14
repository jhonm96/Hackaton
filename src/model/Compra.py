from peewee import *
from src.model.basedatos import db
from src.model.Usuario import Usuario
from datetime import datetime


class Compra(Model):
    id_compra = PrimaryKeyField()
    id_usuario = ForeignKeyField(Usuario, related_name='id_usuario')
    fecha_compra = DateField(default=datetime.today().strftime('%Y-%m-%d'))
    total_compra = DoubleField()
    bonos_usados = IntegerField()

    class Meta:
        database = db
        db_table = 'compra'