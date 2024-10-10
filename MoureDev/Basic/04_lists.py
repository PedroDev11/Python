my_list = list()
my_other_list = []

my_list = [21, 22, 17, 13, 21, 15, 21]
my_other_list = [21, 1.50, "Pedro", "Rojas Valladares"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[-2])
print(my_other_list[-1])
#print(my_other_list[-5]) Error, fuera de rango
print(my_list.count(21))

print("-------------DESCOMPONIENDO LISTA---------------")
age, height, name, lastname = my_other_list
print(name)

name, height, age, lastname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(lastname)

print("-------------CONCATENANDO LISTA---------------")
print(my_list + my_other_list)

print("-------------AGREGANDO ELEMENTO A LISTA---------------")
my_other_list.append("MoureDev")
print(my_other_list)

print("-------------INSERTANDO EN UN INDICE DE LA LISTA---------------")
my_other_list.insert(1, "Manog")
print(my_other_list)

print("-------------REASIGNANDO A LA LISTA---------------")
my_other_list[1] = "Fresa"
print(my_other_list)

print("-------------REMOVIENDO DE LISTA---------------")
my_other_list.remove("Fresa")
print(my_other_list)

my_list.remove(21)
print(my_list)

print("-------------QUITA EL ULTIMO ELEMENTO DE LA LISTA---------------")
print(my_other_list.pop())
print(my_other_list)

print(my_other_list.pop(2))
print(my_other_list)

print("-------------ELIMINA ELEMENTO DE LA LISTA POR INDICE---------------")
del my_list[1]
print(my_list)

print("-------------COPIANDO LISTA---------------")
my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

print("-------------REVERSED LISTA---------------")
my_new_list.reverse()
print(my_new_list)

print("-------------ORDENAR LISTA---------------")
my_new_list.sort()
print(my_new_list)

my_list = "Hola python"
print(my_list)
print(type(my_list))