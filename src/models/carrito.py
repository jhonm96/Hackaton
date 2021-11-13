import peewee
import Usuario
import basedatos


class Carrito(peewee.Model):
    id_carrito = peewee.PrimaryKeyField()
    # id_usuario = peewee.ForeignKeyField(Usuario, backref='id_usuarios')
    id_usuario = peewee.CharField()
    cod_prod = peewee.CharField()
    precio_und = peewee.IntegerField()
    precio_total = peewee.IntegerField()

    class Meta:
        database = basedatos.obtener_database()
        db_table = 'carrito'

def crearTabla():
    if not Carrito.table_exists():
        Carrito.create_table()