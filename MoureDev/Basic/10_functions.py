def my_function():
    print("Esta es mi función")

my_function()

def sum_two_values(first_number, second_number):
    print(first_number + second_number)
    
sum_two_values(5, 7)

def sum_two_values(num_one, num_two):
    my_multi = num_one * num_two
    #return num_one * num_two
    return my_multi

print(sum_two_values(5, 3))

my_value = sum_two_values(5, 2)
print(my_value)

print("------------Función de nombre--------\n")

def my_name(name, lastname):
    print(f"{name} {lastname}")
    print("Mi nombre es: {} {} con otro tipo de formateo".format(name, lastname))
    
my_name("Pedro", "Rojas Valladares")
my_name(lastname = "Valladares", name = "Alberto")

print("------------Función con valores por defecto--------\n")

def my_name_default(name, lastname, nickname = "Sin alias"):
    name = (f"{name} {lastname} {nickname}")
    #print(name)
    return name

print(my_name_default("Alberto", "RV"))
print(my_name_default("Alberto", "RV", "PEPE"))

print("------------Función para pasarle mas de un elemento--------\n")

def print_texts(*text):
    print(text)
    
print_texts("Hola", "Python", "Pepe", 5, 10)
print_texts("Holaaaa", "Que tal")

print("------------Función con un for--------\n")

def print_texts(*texts):
    for text in texts:
        print(text.upper())
    
print_texts("Hola", "Python", "Pepe")
print_texts("Holaaaa", "Que tal")

print("------------Función que imprime una lista--------\n")

def print_my_list(*list):
    print(type(list))
    for element in list:
        print(element)

my_list = [21, 22, 17, 13, 21, 15, 21]
print_my_list(my_list)