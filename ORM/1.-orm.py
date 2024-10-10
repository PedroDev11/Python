'''
Un ORM (OBJECT RELATIONAL MAPPER) una pieza de software que nos permite interactuar con nuestra base de datos 
sin utilizar sql solo con programación orientada a objetos

py -m pip install peewee
'''
import peewee
import datetime

database = peewee.MySQLDatabase("peewee_test", host="localhost", port=3306, user="root", password="pedro20761867")

class User(peewee.Model):
    username = peewee.CharField()
    email = peewee.CharField()
    created_date = peewee.DateTimeField(default = datetime.datetime.now)
    
    class Meta:
        database = database 
        db_table = 'Users'
        
if __name__ == '__main__':
    if not User.table_exists():
        User.create_table()
    
    username = input("Ingrese un nombre: ")
    email = input("Ingrese un email: ")
    
    new_user = User.create(username = username, email = email)
    new_user.save()