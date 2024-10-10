""" 
Dada una lista de nombres de frutas, crea un diccionario que cuente cuántas 
veces aparece cada fruta en la lista utilizando una comprensión de diccionario.
"""

frutas = ["mango", "sandia", "platano", "durazno", "mango", "mandarina", "naranja", "mango"]
#print(frutas.count("mango")) -> 3

com_dict = {name: frutas.count(name) for name in frutas}
print(com_dict)