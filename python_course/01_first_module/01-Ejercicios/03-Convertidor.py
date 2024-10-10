""" 
    Conversor de temperatura: Pide al usuario que ingrese una temperatura en grados Celsius
    y conviértela a grados Fahrenheit utilizando la fórmula (F = (C * 9/5) + 32).
"""
print("\tCONVERTIDOR DE GRADOS CELSIUS A FAHRENHEIT\n")

celsius = int(input("Ingresa los grados celsius: "))

def convertidor(c):
    f = (c * 9/5) + 32
    return f

f = convertidor(celsius)

print("\nLa conversión de grados celsius a grados fahrenheit es de:", f)