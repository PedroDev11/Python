""" 
    Calculadora de área de un triángulo: Pide al usuario que ingrese la base y 
    la altura de un triángulo y calcula su área utilizando la fórmula (Área = (Base * Altura) / 2).
"""
print("\tCALCULANDO EL ÁREA DE UN TRIÁNGULO\n")

base = int(input("Ingresa la base del triángulo: "))
altura = int(input("Ingresa la altura del triángulo: "))

def area(base, altura):
    x = (base * altura) / 2
    return x

res = area(base, altura)
print("El área del triangulo es la siguiente:", res)