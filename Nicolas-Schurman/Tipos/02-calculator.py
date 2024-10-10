#Recibímos el número en string
n1 = input("Ingresa un número: ")
n2 = input("ngresa otro número: ")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2
division = n1 / n2

msg = f"""
Para los números {n1} y {n2},
La suma es: {suma},
La resta es: {resta},
La multiplicación es: {multiplicacion},
La división es: {division}
"""

print(msg)