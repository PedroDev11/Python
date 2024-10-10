#Commparadores lógicos
print("\n-----------Comparadores lógicos----------------")

print(1 > 3) # False
print(1 <= 2)
print(2 == 2)
print(2 != 2) # Not equal, no es igual o es diferente

print("\n-----------If, Else, Elif----------------")

edad = 22

if edad > 54:
    print("Puede ver la película con descuento")
elif edad > 18:
    print("Puedes ver la película")
else:
    print("No puedes entrar")
    
print("\n-----------Operador ternario----------------")

mensaje = "Es mayor" if edad > 17 else "Es menor"

#if edad > 17:
#    mensaje = "Es mayor"
#else:
#    mensaje = "Es menor"
    
print(mensaje)

print("\n-----------Operadores lógicos----------------")
# and, or, not

gas = True
encendido = True

if gas and encendido:
    print("(True) Puedes avanzar")
    
if gas or encendido:
    print("(True) Puedes avanzar")

if not gas and encendido: # gas is False
    print("(True) Puedes avanzar")

if gas and (encendido or edad > 17):
    print("(True) Puedes avanzar")
    
if not gas and (encendido or edad > 17):
    print("(True) Puedes avanzar")
    
print("\n-----------Operador de corto circuito----------------")

if not gas or (encendido or edad > 17):
    print("(True) Puedes avanzar")
    
print("\n-----------Cadena de comparadores----------------")
edad = 25

#if edad >= 15 and edad <= 65:
#    print("Puedes entar a la piscina")

if 15 <= edad <= 65:
    print("Puedes entar a la piscina")
    
print("\n-----------For----------------")

buscar = 3

for numero in range(5): # Termina en el número que le indicamos -1 osea 4
    print(numero)

print("\n-----------For Else----------------")

for numero in range(5):
    print(numero)
    
    if numero == buscar:
        print(f"Encontrado {numero}")
        break
else:
    print(f"No se pudo encontrar el número: {numero}")
    
print("\n-----------For Else----------------")
