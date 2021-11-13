from peewee import *
import datetime

db = MySQLDatabase('my_database', host='localhost', port=3306, user='root', passwd='root')

class Producto(Model):
    cod_prod = PrimaryKeyField()
    nombre_prod = CharField()
    inventario = IntegerField()
    presentacion = CharField()
    precio_und = IntegerField()
    desc_promo = IntegerField(default = 0)
    und_vendidas = IntegerField()
    total_venta = IntegerField()
    calif_prom = DoubleField()
    desc_promo = IntegerField()
    apl_desc = CharField()
    acum_desc = IntegerField()
    id_coment = IntegerField()
    activo = BooleanField(default = True)

    class Meta:
        database = db
        db_table = 'productos'

    def crearTabla():
        if not Producto.table_exists():
            return Producto.create_table()

class Lote(Model):
    id_lote = PrimaryKeyField()
    cod_prod = ForeignKeyField(Producto, related_name='cod_prod')
    cant_lote = IntegerField()

    class Meta:
        database = db
        db_table = 'lotes'

    def crearTabla():
        if not Lote.table_exists():
            return Lote.create_table()

class ProductoLote(Model):
    id_prodLote = PrimaryKeyField()
    cod_prod = ForeignKeyField(Producto, related_name='cod_prod')
    id_lote = ForeignKeyField(Lote, related_name='id_lote')
    cant_act_lote = IntegerField()
    # fecha_ingreso = DateTimeField(defaul = datetime.datetime.now())
    fecha_ultima_venta = DateField()

    class Meta:
        database = db
        db_table = 'producto_lote'

    def crearTabla():
        if not ProductoLote.table_exists():
            return ProductoLote.create_table()

class ProductosBaja(Model):
    id_prodBaja = PrimaryKeyField()
    cod_prod = ForeignKeyField(Producto, related_name='cod_prod')
    lote = ForeignKeyField(Lote, related_name='id_lote')
    fecha_baja = DateTimeField()
    num_ventas = IntegerField()
    valor_total_ventas = DoubleField()
    razon = CharField()

    class Meta:
        database = db
        db_table = 'productos_baja'

    def crearTabla():
        if not ProductosBaja.table_exists():
            return ProductosBaja.create_table()

class RotacionProducto(Model):
    id_rotacion = PrimaryKeyField()
    cod_prod = ForeignKeyField(Producto, related_name='cod_prod')
    categoria = CharField()

    class Meta:
        database = db
        db_table = 'rotacion_producto'

    def crearTabla():
        if not RotacionProducto.table_exists():
            return RotacionProducto.create_table()

class Usuario(Model):
    id_usuario = PrimaryKeyField()
    cedula = CharField(max_length=50, unique=True)
    nombre = CharField(max_length=50)
    apellido = CharField(max_length=50)
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

    class Meta:
        database = db
        db_table = 'usuarios'

    def crearTabla():
        if not Usuario.table_exists():
            Usuario.create_table()

class Compra(Model):
    id_compra = PrimaryKeyField()
    id_usuario = ForeignKeyField(Usuario, related_name='id_usuario')
    fecha_compra = DateField()
    total_compra = DoubleField()
    bonos_usados = IntegerField()

    class Meta:
        database = db
        db_table = 'compras'

    def crearTabla():
        if not Compra.table_exists():
            return Compra.create_table()

class ComprasUsuario(Model):
    id_compra_usuario = PrimaryKeyField()
    id_usuario = ForeignKeyField(Usuario, related_name='id_usuario')
    fecha_compra = DateField()
    total_compra = DoubleField()

    class Meta:
        database = db
        db_table = 'compras_usuario'

    def crearTabla():
        if not ComprasUsuario.table_exists():
            return ComprasUsuario.create_table()

class Carrito(Model):
    id_carrito = PrimaryKeyField()
    id_usuario = ForeignKeyField(Usuario, related_name='id_usuarios')
    id_usuario = CharField()
    cod_prod = CharField()
    precio_und = IntegerField()
    precio_total = IntegerField()

    class Meta:
        database = db
        db_table = 'carrito'

    def crearTabla():
        if not Carrito.table_exists():
            Carrito.create_table()

def crearTablas():
    Producto.crearTabla()
    Lote.crearTabla()
    ProductoLote.crearTabla()
    ProductosBaja.crearTabla()
    RotacionProducto.crearTabla()
    Usuario.crearTabla()
    Compra.crearTabla()
    ComprasUsuario.crearTabla()
    Carrito.crearTabla()
    
def registrar(usuario, contrraseña, email, nombre, apellido, cedula, sexo, fecha_nac, direccion, ciudad):
        Usuario.create(
            username = usuario,
            password = contrraseña,
            email = email,
            nombre = nombre,
            apellido = apellido,
            cedula = cedula,
            sexo = sexo,
            fecha_nac = fecha_nac,
            direccion = direccion,
            ciudad = ciudad)
        Usuario.save()


    

print(registrar('juan', '123', 'juan@123', 'Juan', 'Perez', '123456789', 'M', '1990-01-01', 'Calle 123', 'Bogota')
)

    
    
