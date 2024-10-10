frutas = [
    'banana',
    'manzana',
    'pera',
    'sandia'
]

print(frutas[0])

#reasignar valores
frutas[0] = 'platano'
print(frutas)

print(len(frutas))

print(frutas.append('naranja'))

#nos indica la posición del elemento a buscar
print(frutas.index('manzana'))

for fruta in frutas:
    print(fruta)