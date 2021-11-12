import peewee

database = peewee.MySQLDatabase('db_hackaton', host='localhost', port=3306, user='root', password='root')

class usuario(peewee.Model):
    id_usuario = peewee.CharField()
    cedula = peewee.CharField(max_length=10)
    nombre = peewee.CharField(max_length=50)
    apellido = peewee.CharField(max_length=50)
    sexo = peewee.CharField(max_length=1)
    f_nacimiento = peewee.DateField()
    direccion = peewee.CharField(max_length=100)
    ciudad = peewee.CharField(max_length=50)
    acum_compras = peewee.DoubleField()
    n_bonos = peewee.IntegerField()
    username = peewee.CharField(max_length=50)
    email = peewee.CharField(max_length=50)
    password = peewee.CharField(max_length=50)
    cargo = peewee.CharField(max_length=50)
    Role = peewee.CharField(max_length=50)

    class Meta:
        database = database
        db_table = 'Usuario'

if __name__ == '__main__':
    if not usuario.table_exists():
        usuario.create_table()
    
    
# username = input("Ingrese un Nombre :")
# email = input("Ingrese un email :")
# usuario.create_table()    
# newUser = usuario.create(nombre = username, correo=email)
# newUser.save()

# import peewee

# database = peewee.MySQLDatabase('hackaton', host='localhost', port=3306, user='root', password='root')

# pip install pymysql

# class usuario(peewee.Model):
#  #  id = peewee.PrimaryKeyField()
#     nombre = peewee.CharField()
#     correo = peewee.CharField()

#     class Meta:
#         database = database
#         db_table = 'Usuario'


# username = input("Ingrese un Nombre :")
# email = input("Ingrese un email :")
# usuario.create_table()    
# newUser = usuario.create(nombre = username, correo=email)
# newUser.save()



# array = usuario.select() // seleccionar una tabla
# array = usuario.filter(nombre = "Jhon") // filtrar usuario

# for user in array:
#    print(user.id, user.nombre, user.correo)
    