import datetime
from models import *

with db: 
    db.create_tables([Expense, Payment])
    
print('DONE')