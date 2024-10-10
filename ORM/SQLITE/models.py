'''
ORM con sqlite 
'''
import datetime
import peewee

db = peewee.SqliteDatabase('data.db')

class BaseModel(peewee.Model):
    
    class Meta:
        database = db
        
class User(BaseModel):
    class Meta:
        db_table = 'User'
    
    vk_id = peewee.IntegerField()
    name = peewee.CharField(max_length=150)
    mode = peewee.CharField(max_length=50)
    money = peewee.FloatField()
    
class Order(BaseModel):
    class Meta:
        db_table = 'Order'
    
    customer = peewee.ForeignKeyField(User)
    executor = peewee.ForeignKeyField(User)
    price = peewee.FloatField()
    comment = peewee.TextField()
    
if __name__ == '__main__':
    db.create_tables([User, Order])