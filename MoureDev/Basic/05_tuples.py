my_tuple = tuple()
my_other_tuple = ()

my_tuple = (21, 1.60, "Pedro", "Alberto", "Pedro")
my_other_tuple = ("Rojas", "Valladares")
print(type(my_tuple))
print(type(my_other_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Pedro"))
print(my_tuple.index("Alberto"))
print(my_tuple.index("Pedro"))

#my_tuple[5] = 1.80 No soporta agregar items
print("-------------CONCATENACION DE TUPLA---------------")
print(my_tuple + my_other_tuple)

print(my_tuple[1:4])

print("------------PASANDO EL TYPO DE TUPLA A LISTA---------------")
my_tuple = list(my_tuple)
print(type(my_tuple))

print("-------------AGREGANDO ELEMENTOS A LA TUPLA--------")
my_tuple[4] = "Pepe"
my_tuple.insert(1, "Mango")
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple))

#del my_tuple[2] NO SOPORTA ELMINAR ITEMS

del my_tuple #ELIMINA TODA LA TUPLA