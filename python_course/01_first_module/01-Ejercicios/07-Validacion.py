""" 
    Validación de contraseña: Pide al usuario que cree una contraseña. 
    Asegúrate de que la contraseña tenga al menos 8 caracteres de longitud y 
    contenga al menos una letra mayúscula y un número.
"""
print("\tVALIDACIÓN DE CONTRASEÑA\n")

print("Crea una nueva contraseña que contenga al menos 8 caracteres, una letra mayuscula y un número\n")
password = input("Contraseña nueva: ")

if len(password) < 8:
    print("La contraseña es muy corta, debe contener al menos 8 caracteres")
else:
    minuscula = False
    for minus in password:
        if minus.islower() == True:
            minuscula = True
    if not minuscula:
        print("La contraseña debe tener al menos una minuscula")
    
    mayusculas = False
    for mayus in password:
        if mayus.isupper() == True:
            mayusculas = True
    if not mayusculas:
        print("La contraseña debe contener al menos una mayuscula")
        
    num = False
    for carac in password:
        if carac.isdigit() == True:
            num = True
    if not num:
        print("La contraseña debe contener al menos un número")
        
    else:
        print("La contraseña es segura")
