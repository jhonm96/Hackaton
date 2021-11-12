import peewee

database = peewee.MySQLDatabase('hackaton', host='localhost', port=3306, user='root', password='root')

class role(peewee.Model):
    id_roles = peewee.PrimaryKeyField()
    rol = peewee.CharField()
    
    class Meta:
        database = database
        db_table = 'Roles'

if __name__ == '__main__':
    if not role.table_exists():
        role.create_table()

if __name__ == '__main__':
    if not role.table_exists():
        role.create_table()