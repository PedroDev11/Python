""" 
Crea un diccionario que asocie nombres de personas con sus edades 
utilizando una comprensión de diccionario.
"""
personas = [("Pedro", 22), ("Eduardo", 23), ("Lalo", 40), ("Brian", 18)]

com_dict = {name: edad for name, edad in personas}
print(com_dict)