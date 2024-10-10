print("Bienvenidos a la calculadora\n")
print("para salir escribe salir.\n")
print("Las operaciones son suma, resta, multiplicacion, division")

resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese un número: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("Ingresar operación: ")
    if op.lower() == "salir":
        break
    n2 = input("Ingresa siguiente número: ")
    if n2.lower() == "salir": 
        break
    n2 = int(n2)
    
    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multiplicacion":
        resultado *= n2
    elif op.lower() == "division":
        resultado /= n2
    else:
        print("Operación no válida")
        break
    
    print(f"El resultado es: {resultado}")