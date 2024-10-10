""" 
    Promedio de calificaciones: Pide al usuario que ingrese cinco calificaciones y 
    luego calcula y muestra el promedio de estas calificaciones.
"""
print("\tPROMEDIO DE CALIFICACIONES\n")
print("Ingresa tus calificaciones de tus cinco materias\n")

n1 = int(input("Ingresa tu primer calificación: "))
n2 = int(input("Ingresa tu segunda calificación: "))
n3 = int(input("Ingresa tu tercera calificación: "))
n4 = int(input("Ingresa tu cuarta calificación: "))
n5 = int(input("Ingresa tu quinta calificación: "))

promedio = (n1 + n2 + n3 + n4 + n5) / 5

print("\nDebido a tus calificaciones tu promedio es el siguiente:", promedio)