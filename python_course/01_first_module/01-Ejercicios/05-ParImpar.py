""" 
    Verificar número par o impar: Solicita al usuario que ingrese un número 
    entero y verifica si es par o impar.
"""
print("\tVERIFICANDO SI UN NÚMERO ES PAR O IMPAR\n")

num = int(input("Ingresa un número entero: "))

x = num % 2

if x == 0:
    print(num, "Es par")
else:
    print(num, "Es impar") 