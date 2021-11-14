from peewee import *
from src.model.basedatos import db
from datetime import datetime


class Producto(Model):
    cod = PrimaryKeyField()
    nombre_prod = CharField()
    inventario = IntegerField()
    presentacion = CharField()
    precio_und = IntegerField()
    desc_promo = IntegerField(default = 0)
    und_vendidas = IntegerField(default = 0)
    total_venta = IntegerField(default = 0)
    calif_prom = DoubleField()
    apl_desc = CharField()
    acum_desc = IntegerField()
    activo = BooleanField(default = True)
    fecha_ingreso = DateField(default=datetime.today().strftime('%Y-%m-%d'))

    class Meta:
        database = db
        db_table = 'producto'