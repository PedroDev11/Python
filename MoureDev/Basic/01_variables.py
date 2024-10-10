#Variables
firstname = 'Pedro'
lastname = 'Rojas Valladares'
nickname = 'pepe'
age = 21

print('Que tal, soy', firstname)
print('my last name is', lastname)
print('i like they call me', nickname)
print('I am', age)
print(type(age))

#cambiando variable de int a str
my_int_to_str = str(age)
print(my_int_to_str)
print(type(my_int_to_str))

#Variables en una sola línea
country, skills, alias, random = 'Latam', 'programer', 'apex', 3.1416
print('Desafortunadamente vivo en:', country, 'I am', skills, alias, random)

#Formulario
firstname = input('What is your name: ')
age = input('How old are you: ')
print(firstname)
print(age)

address: str = 'pp'
print(type(address))