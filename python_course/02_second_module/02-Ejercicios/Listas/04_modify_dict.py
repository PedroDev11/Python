personas = [
    {
        "Nombre": "Pedro",
        "Edad": 22,
        "Ciudad": "Valle de Chalco",
        "Profesión": "Estudiante de ingeniería en sistemas computacionales"
    },
    {
        "Nombre": "Eduardo",
        "Edad": 23,
        "Ciudad": "Valle de Chalco",
        "Profesión": "Estudiante de ingeniería en sistemas automotrices"
    },
    {
        "Nombre": "Brian",
        "Edad": 18,
        "Ciudad": "Valle de Chalco",
        "Profesión": "Estudiante de soporte y mantenimiento al equipo de computo"
    }
]

user = personas[0]
user["Edad"] = 30

for users in personas:
    print("\n")
    for key, valor in users.items():
        print(f'{key}: {valor}')
        