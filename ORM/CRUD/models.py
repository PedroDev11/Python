import peewee

db = peewee.SqliteDatabase('db/database.db')

class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(unique = True)

    class Meta:
        database = db
        order_by = 'id'

class Expense(BaseModel):
    name = peewee.CharField()
    
    class Meta:
        db_table = 'expenses'

    
class Payment(BaseModel):
    amount = peewee.FloatField()
    payment_date = peewee.DateField()
    expense_id = peewee.ForeignKeyField(Expense)
    
    class Meta:
        db_table = 'payments'