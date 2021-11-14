from peewee import *
from src.model.basedatos import db
from src.model.Producto import Producto

class Lote(Model):
    id = PrimaryKeyField()
    cod_prod = ForeignKeyField(Producto, related_name='cod_prod')
    cant_lote = IntegerField()

    class Meta:
        database = db
        db_table = 'lote'
        