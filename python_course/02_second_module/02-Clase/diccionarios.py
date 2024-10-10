"""
usuario = {
    'nombre': 'pedro',
    'apellidos': 'rojas valladares',
    'edad': 22,
    'email': 'pedro@gmail.com'
}

user_name = usuario['nombre']
user_lastname = usuario['apellidos']
aye = usuario.get('edad')
email = usuario.get('email')

high = usuario.get('altura', 'no se encontro una altura')

print(usuario.keys())
print(usuario.values())
print(usuario.items())
print(usuario.clear())

usuario2 = usuario.copy()
print(usuario2)

for key, value in usuario.items():
    print(f'llave en esta iteración: {key}, valor en esta iteración: {value}')
    
usuarios = [
    {"nombre": "Daniel"},
    {"nombre": "Alex"},
    {"nombre": "Pedro"},
]

for user in usuarios:
    print(user.items())
    
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print(matriz[1][2])
"""

matriz2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
    [13, 14, 15],
    [16, 17, 18],
    [19, 20, 21]
]

for num in matriz2:
    print(num)
    
print("------------------------------------------------------")

for num in matriz2:
    print(num[0])
    print(num[1])
    print(num[2])