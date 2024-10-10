import sqlite3
import datetime

def get_timestamp(y, m, d):
    return int(datetime.datetime.timestamp(datetime.datetime(y, m, d)))

def get_date(tmstmp):
    return datetime.datetime.fromtimestamp(tmstmp).date()

with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query = """ CREATE TABLE IF NOT EXISTS payments(
        id INTERGER,
        amount REAL,
        payment_date INTERGER,
        expense_id INTERGER
    )"""
    cursor.execute(query)
    db.commit()
    
with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query1 = """ INSERT INTO expenses (id, name) VALUES(1, 'Pepe')"""
    query2 = """ INSERT INTO expenses (name, id) VALUES('Pedro', 2)"""
    query3 = """ INSERT INTO expenses VALUES(3, 'Rojas')"""
    cursor.execute(query1)
    cursor.execute(query2)
    cursor.execute(query3)
    db.commit()
    
insert_payments = [
    (1, 120, datetime.date(2020, 9, 1), 1),
    (2, 12, datetime.date(2020, 9, 2), 3),
    (3, 20, datetime.date(2020, 9, 3), 2),
    (4, 20, datetime.date(2020, 9, 4), 2),
    (5, 20, datetime.date(2020, 9, 5), 2),
    (6, 20, datetime.date(2020, 9, 6), 2),
    (7, 20, datetime.date(2020, 9, 7), 2),
]

with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query = """INSERT INTO payments(id, amount, payment_date, expense_id)
                            VALUES(?, ?, ?, ?);"""
                            
    cursor.executemany(query, insert_payments)
    db.commit()
    print(cursor.rowcount, "Filas insertadas")
    
with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query = """SELECT * FROM payments"""
    cursor.execute(query)
    
with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query = """SELECT amount, payment_date FROM payments WHERE expense_id = 2"""
    cursor.execute(query)
    
with sqlite3.connect('db/database.db') as db:
    cursor = db.cursor()
    query = """SELECT amount, payment_date, name FROM payments JOIN expenses
                ON expenses.id = payments.expenses_id WHERE expenses_id = 2"""
    
    cursor.execute(query)
    
            
    