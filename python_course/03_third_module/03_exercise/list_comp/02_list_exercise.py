""" 
Dada una lista de palabras, crea una nueva lista que contenga solo las palabras 
que tengan más de 5 letras.
"""

words = ["PalabraUno", "Pizarron", "Computadora", "Hola", "Pepe"]
new_list = [i for i in words if len(i) > 5]
print(new_list)