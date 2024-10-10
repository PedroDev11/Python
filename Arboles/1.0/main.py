from arboles import Arbol

# #Arbol definido por nombres
# arbol = Arbol("Luis") #root
# arbol.agregar("María José")
# arbol.agregar("Andres")

# #Agregando un nuevo nombre
# nombre = input("Ingresa un nombre para agregar al árbol: ")
# arbol.agregar(nombre)

# print("----------------------------\n")
# arbol.inorden() #left, root, rigth
# print("----------------------------\n")
# arbol.preorden() #root, left, rigth
# print("----------------------------\n")
# arbol.postorden() #left, rigth, root
# print("----------------------------\n")

# # Búsqueda por nombre
# busqueda = input("Busca algo en el árbol: ")
# nodo = arbol.buscar(busqueda)
# if nodo is None:
#     print(f"{busqueda} no existe")
# else:
#     print(f"{busqueda} sí existe")
# # Aquí tienes en "nodo" toda la información del nodo. Tanto su izquierda, derecha, dato y otros atributos que le hayas agregado

'''
    Ejemplo
                  6
                 / \
                4    8
               / \    \
              1   5    9
              
inorder: 1, 4, 5, 6, 8, 9
preorder: 6, 4, 1, 5, 8, 9
postorder: 1, 5, 4, 9, 8, 6
'''

#Arbol definido por numeros
arbol_numeros = Arbol(6) #root
arbol_numeros.agregar(1)
arbol_numeros.agregar(4)
arbol_numeros.agregar(5)
arbol_numeros.agregar(8)
arbol_numeros.agregar(9)

#Agregando un nuevo nombre
# number = int(input("Ingresa un número: "))
# arbol_numeros.agregar(number)

print("----------------------------\n")
arbol_numeros.inorden() #left, root, rigth
print("----------------------------\n")
arbol_numeros.preorden() #root, left, rigth
print("----------------------------\n")
arbol_numeros.postorden() #left, rigth, root
print("----------------------------\n")

#Busqueda mediante un numero
busqueda = int(input("Ingresa un número para buscar en el árbol: "))
n = arbol_numeros.buscar(busqueda)
if n is None:
    print(f"{busqueda} no existe")
else:
    print(f"{busqueda} sí existe")