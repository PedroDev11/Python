signos = ['.', '_', '-']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
dominios = ['gmail', 'hotmail', 'msn', 'yahoo', 'outlook', 'live']
minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
mayusculas = []
extension = ['com', 'net', 'com.mx', 'edu.mx', 'ea', 'es', 'mx', 'org', 'gob', 'tesch.edu.mx']

for x in minusculas:
    mayusculas.append(x.upper())

email = input("Escribe tu emial para verificar: ")
problema = ""

if email.find('@') != -1:
    nuevo_email = email.split('@')
    usuario = nuevo_email[0]
    resto = nuevo_email[1]
    continuacion = resto.split('.')
    dominio = continuacion[0]
    terminacion = continuacion[1]
    
    for x in usuario:
        if x in signos or x in numeros or x in minusculas or x in mayusculas:
            if dominio in dominios:
                if terminacion in extension:
                    problema = "El email es correcto"
                else:
                    problema += "La terminación no es común pero puede ser valido\n"
            else:
                problema += "El dominio no es reconocido pero puede ser privado\n"
        else:
            problema += "El valor " + x + " no es valido para un correo\n"
else:
    problema += "El correo no tiene una arroba\n"

print(problema)