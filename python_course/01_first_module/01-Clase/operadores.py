""" 
    Operadores
    
+, -, *, /, //, %, **

    Operador y asignación 
+=, -=, *=, /=

    EJERCICIO
Crear una calculadora de descuentos
"""
print("BIENVENIDO A LA TIENDITAA\n")
product1 = int(input("Introduce el costo de tu producto 1: "))
product2 = int(input("Introduce el costo de tu producto 2: "))
product3 = int(input("Introduce el costo de tu producto 3: "))
x = product1 + product2 + product3

def descuento(x):
    x -= x*0.30
    return x

resultado = descuento(x)
print(f'\nFelicidades por tu compra de ${x} usted obtuvo un descuento y ahora paga ${resultado}')

