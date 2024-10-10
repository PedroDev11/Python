#from datetime import datetime
import datetime

now = datetime.datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

print("----------------------------")

timestamp = now.timestamp()
print(timestamp)

print("-------FUNCIÓN CON VALORES DEL SISTEMA---------------------")

def print_date(date):
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)

print_date(now)

print("----------------------------")

year_2023 = datetime.datetime(2023, 4, 1, 12)
print_date(year_2023)

print("--------TIME PASANDOLE VALORES--------------------")

from datetime import time
current_time = time(21, 6, 20)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

print("--------DATE CON VALORES DEL SISTEMA--------------------")

from datetime import date
current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)

print("--------DATE PASANDOLE VALORES--------------------")

current_date = date(2023, 10, 6)

print(current_date.year)
print(current_date.month)
print(current_date.day)

print("---------OPERACIONES CON FECHAS-------------------")

current_date = date(current_date.year, current_date.month + 1, current_date.day)

print(current_date.month)

diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

print("---------TIMEDELTA-------------------")

from datetime import timedelta
#sirve para trabajar con frangas de tiempo
start_timedelta = timedelta(200, 100, 100, weeks = 10)
end_timedelta = timedelta(300, 100, 100, weeks = 13)

print(end_timedelta + start_timedelta)
print(end_timedelta - start_timedelta)