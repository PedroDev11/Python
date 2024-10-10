my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre": "Pedro", "Apellidos": "Rojas Valladares", "Edad": 21, 1: "id"}
my_dict = {
    "Nombre": "Alberto",
    "Apellidos": "Rojas Valladares",
    "Edad": 21,
    "Lenguajes": {"Python", "SQL", "Java"},
    "Listado": ["MoureDev", "Platzi", "Profe"],
    2: "id"
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Listado"])

print("------------REASIGNAMOS EL VALOR NOMBRE--------")
my_dict["Nombre"] = "Pepe"
print(my_dict["Nombre"])

print("------------AGREGAMOS UN VALOR AL DICCIONARIO--------\n")
my_dict["Calle"] = "Oriente44a"
print(my_dict)

print("------------ELIMINAMOS UN ELEMENTO DEL DICCIONARIO--------\n")
del my_dict["Calle"]
print(my_dict)

print("Apellidos" in my_dict)
print("Pepe" in my_dict)

print(my_dict.items())
print(my_dict.keys()) #retorna todas las claves
print(my_dict.values()) #retorna todos los valores

print("------------FROMKEYS DE UN DICCIONARIO--------\n")
my_new_dict = dict.fromkeys(("nombre", "apellidos"))
print(my_new_dict)
my_new_dict = dict.fromkeys((my_dict)) #conserva todas las claves de un diccionario
print(my_new_dict)
print("-----------------------------------------------------------\n")
my_new_dict = dict.fromkeys(my_dict, "Pedroooo")
print(my_new_dict)

print("-----------------------------------------------------------\n")
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(set(my_new_dict))