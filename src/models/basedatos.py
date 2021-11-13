import peewee

database = peewee.MySQLDatabase('temp', host='localhost', port=3306, user='root', password='root')

def obtener_database():
    return database

