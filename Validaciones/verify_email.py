import re

#simplemente evalua si tiene la estructura, no valida si la direccion email es verdadera o falsa
def validate_email(arg_email):
    is_valid = True
    
    #A esta regla primero se le debe pasar la 'r' para evaluar lo que se le este pasando
    EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
    
    #Hace un match positivo de arg_email
    is_valid = False if not EMAIL_REGEX.match(arg_email) else True
    
    print("Email is valid" if is_valid else "Invalid email address")
    
validate_email("alvison.hunter@outlook.com")
validate_email("pedro2076r@gmail.com")
validate_email("pedro2076r@gmail.com")
validate_email("pedro2076r@outlook.com")