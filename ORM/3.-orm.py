'''
ORM con sqlite 
'''
import datetime
import peewee

db = peewee.SqliteDatabase('orm_practise.db')

class BaseModel(peewee.Model):
    created_at = peewee.DateTimeField(default = datetime.datetime.now)
    updated_at = peewee.DateTimeField(default = datetime.datetime.now)
    
    class Meta:
        database = db
        
class Store(BaseModel):
    name = peewee.CharField(unique = True)
    
class Warehouse(BaseModel):
    store = peewee.ForeignKeyField(Store, backref='warehouses')
    

class Product(BaseModel):
    name = peewee.CharField()
    description = peewee.TextField()
    warehouse = peewee.ForeignKeyField(Warehouse, backref='products')