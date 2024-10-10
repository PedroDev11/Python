notas = {
    "Daniel": 95,
    "Alex": 92,
    "Alberto": 88,
    "Pedro": 89,
    "Fernando": 91
}
x = 0

for num in notas.values():
    x += num
    
promedio = x / 5
print(f'El promedio es: {promedio}')


print("El alumno con mayor calificación es:", max(notas, key=notas.get))