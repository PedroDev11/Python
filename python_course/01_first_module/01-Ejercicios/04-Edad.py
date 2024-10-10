""" 
    Edad en días: Pregunta al usuario su edad en años y muestra la edad 
    equivalente en días (suponiendo que un año tiene 365 días).
"""
print("\tCALCULANDO TÚ EDAD EN DÍAS\n")

edad = int(input("Ingresa tu edad en años: "))

def dias(edad):
    x = edad * 365
    return x

x = dias(edad)

print("Tú edad en días equivale a:", x)