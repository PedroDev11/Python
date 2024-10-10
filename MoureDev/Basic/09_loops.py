my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("Mi condición es mayor que 10")
    
print("La ejecución continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continua")

print("------------Ciclo for de una lista--------\n")
my_list = [21, 40, 35, 80, 54, 45]

for element in my_list:
    print(element)

print("------------Ciclo for de una tupla--------\n")
my_tuple = (21, 1.60, "Pedro", "Alberto", "Pedro")

for element in my_tuple:
    print(element)

print("------------Ciclo for de un set--------\n")
my_set = {"pepe", 21, "Rojas"}

for element in my_set:
    print(element)

print("------------Ciclo for de un diccionario--------\n")
my_dict = {
    "Nombre": "Alberto",
    "Apellidos": "Rojas Valladares",
    "Edad": 21,
    "Lenguajes": {"Python", "SQL", "Java"},
    "Listado": ["MoureDev", "Platzi", "Profe"],
    2: "id"
}

#for element in my_dict.values():
#    print(element)
    
for element in my_dict:
    print(element)
    if element == "Edad":
        break
        #continue detiene la ejecución y empieza de nuevo desde el for
else:
    print("El bucle for para diccionario ha finalizado")