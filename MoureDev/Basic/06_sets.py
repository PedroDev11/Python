my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #inicialmente el tipo es un diccionario

my_other_set = {"Pedro", "RV", 21}
print(type(my_other_set))

print("-------------AGREGAMOS UN ELEMENTO AL SET--------")
my_other_set.add("Pepe")
print(my_other_set) #Los sets no es una estructura ordenada y no acepta elementos repetidos

print("-------------EVALUAMOS IS EXISTEN ESTOS ELEMENTOS EN EL SET--------")
print("Pedro" in my_other_set)
print("Pedrito" in my_other_set)

print("-------------REMOVEMOS UN ELEMENTO DEL SET--------")
my_other_set.remove("Pepe")
print(my_other_set)

print("-------------CAMBIAMOS EL TIPO DE SET A LISTA--------")
my_set = {"pepe", 21, "Rojas"}
my_list = list(my_set) 
#se puede cambiar el tipo a una lista pero esto es arriesgado ya que siempre el set esta desordenado y la lista no toma un orden concreto
print(my_list)
print(type(my_list))

print("-----------OPERACIÓN LÓGICA UNIÓN--------")
my_other_set = {"Kotlin", "Python", "Java", 21, "pepe"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"JavaScript", "C++", "C#"}))

print("------------OPERACIÓN LÓGICA DIFERENCIA--------")
print(my_new_set.difference(my_set))

print("------------LIMPIAMOS EL SET--------")
my_other_set.clear() #simplemente la deja vacía
print(my_other_set)
print(len(my_other_set))

print("------------ELIMINAMOS POR COMPLETO EL SET--------")
del my_other_set #elimina toda la variable