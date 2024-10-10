from .LogBack import logging

def validarContraseñas(password):
    if len(password) < 8:
        logging.warning("La contraseña es muy corta, debe contener al menos 8 caracteres.")
        return "La contraseña es muy corta, debe contener al menos 8 caracteres."
    else:
        minuscula = False
        for minus in password:
            if minus.islower() == True:
                minuscula = True
        if not minuscula:
            logging.warning("La contraseña debe tener al menos una minuscula.")
            return "La contraseña debe tener al menos una minuscula."
        
        mayusculas = False
        for mayus in password:
            if mayus.isupper() == True:
                mayusculas = True
        if not mayusculas:
            logging.warning("La contraseña debe contener al menos una mayuscula.")
            return "La contraseña debe contener al menos una mayuscula."
            
        num = False
        for carac in password:
            if carac.isdigit() == True:
                num = True
        if not num:
            logging.warning("La contraseña debe contener al menos un número.")
            return "La contraseña debe contener al menos un número."
        else:
            logging.info("La contraseña es segura.")
            return "La contraseña es segura."
            
""" 

def validarContraseñas(password):
    if len(password) < 8:
        print()
        return "La contraseña es muy corta, debe contener al menos 8 caracteres"
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
"""