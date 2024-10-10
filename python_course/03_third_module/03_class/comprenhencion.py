"""# list comprenhencion
my_list = [number for number in range(1, 11)]
print(my_list)

my_other_list = [char.upper() for char in "Pedro"]
print(my_other_list)

par = [number for number in range(1, 11) if number % 2 == 0]
print(par)

def filter_number(number_filter):
    com_list = [number for number in range(1, 11) if number % number_filter == 0]
    return com_list

print(filter_number(5))

#dict comprenhencion

my_dict = {
    "name": "pedro",
    "age": 22,
    "hobbie": "Programming"
}

com_dict = {x: x*2 for x in range(1, 11)}
print(com_dict)

com_dict_two = {x*2: x for x in range(1, 11)}
print(com_dict_two)

# Exercises LIST COMPRENHENCION
# list comprenhencions que apartir de una lista de numeros enteros a partir 1 al 1000
# y que añada los valores pares

# List comprenhencion que apartir de una lista de contraseñas(str), solamente añada las que tengan
# una longitud mayor o igual a 8

# list comprenhencion anidado que apartir de una lista de listas, que solamente añada el primer 
# valor de la lista de las listas anidadas

print("----------------EXERCISE ONE--------------------")
list_par = [number for number in range(1, 1001) if number % 2 == 0]
print(list_par)

print("----------------EXERCISE TWO--------------------")
my_list = ["password123", "pass", "pp", "pedroalberto"]
list_password = [con for con in my_list if len(con) >= 8]
print(list_password)

print("----------------EXERCISE THREE--------------------")
list_anidada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

my_other_list = [value[0] for value in list_anidada]
print(my_other_list)

for i in list_anidada:
    print(i[0])
"""
# EXCERCISES DICT COMPRENHENCION
# dict comprenhencion que a partir de una lista de nombres, crea un nuevo diccionario
# que tenga como llave cada nombre y como valores la longitud de ese nombre

# dict comprenhencion que a partir de una lista de enteros crea un nuevo dict que como llave tenga 
# el entero y como valor el entero elevado a si mismo 
name_list = ["Daniel", "Adolf", "Alex", "Pedro"]
com_dict = {x: len(x) for x in name_list}
print(com_dict)

num_list = [2, 3, 4, 5, 1, 6, 7, 8]
com_dict = {x: x**x for x in num_list}
print(com_dict)