import random

x = random.randrange(1, 10)
y = random.uniform(1, 10)
z = random.randrange(0, 10, 2)

print(f"1.-{x}, 2.-{y}, 3.-{z}")

personas = ["pedro", "alberto", "rojas", "valladares"]
winner = random.choice(personas)
print(winner)

personas = ["pedro", "alberto", "rojas", "valladares"]
winner = random.choice(personas)
print(winner, 2)

# CONTRASEÑAS

letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = ".!#$%&/()=?¡¿}+*]-_"

unir = f"{letras}{numeros}{simbolos}"
extension = random.sample(unir, 10)
password = "".join(extension)
print(f"contraseña generada: {password}")