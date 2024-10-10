from models import *

User(
    vk_id = 20,
    name = 'pepe',
    mode = 'start',
    money = 2000
).save()

cust = User.get(id = 1)
exe = User.get(id = 2)

Order(
    price = 400,
    comment = "Text align, text center",
    customer = cust,
    executor = exe
).save()

user = User.get(id = 1)
print(user.name)

users = [x for x in User.select().where(User.money > 100)]
for user in users:
    print(f'{user.vk_id} | {user.name}')
    
executor = User.get(name = 'Maxim')
orders = [x for x in Order.select().where(Order.executor_id == executor.id)]
print(orders)