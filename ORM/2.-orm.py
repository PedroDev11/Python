"""
ORM con sqllite
"""
from datetime import date
import peewee

db = peewee.SqliteDatabase('girl.db')

class Girl(peewee.Model):
    name = peewee.CharField()
    birthday = peewee.DateField()
    
    class Meta:
        database = db
        
if __name__ == '__main__':
    try:
        db.connect()
        db.create_tables([Girl])
    except:
        print("No se pudo crear la tabla ")
        
    try:
        vany = Girl(name = 'Vany', birthday = '1980-1-1')
        vany.save()
        
        # We retrieve the data
        data = Girl.get(Girl.name == 'Vany')
        print(data.name)
    except:
        print('Vany is not in the database')