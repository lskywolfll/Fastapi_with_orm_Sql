from peewee import *

database = MySQLDatabase(
    'fastapi2',
    user='TESTING',
    password='TESTING123',
    host='localhost',
    port=3306
)

class User(Model):
    username = CharField(max_length=50, unique=True)
    email = CharField(max_length=50)

    def __str__(self):
        return self.username
    
    class Meta:
        database = database
        table_name = 'users'