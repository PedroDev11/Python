"""
nombre_global = "pepe rojas"

def saludar(nombre, apellidos, edad, email, direccion = "ote 44a"):
    print(f'nombre: {nombre}')
    print(f'apellidos: {apellidos}')
    print(f'edad: {edad}')
    print(f'emial: {email}')
    print(f'direccion: {direccion}')
    print(f'nombre global: {nombre_global}')
    
saludar("pedro", "rojas valladares", 22, "pedrogmail.com")
"""

#definir una funcion para sacar el area de un triangulo, cuadrado, rectangulo, circulo, 
trg_base = 4
trg_altura = 4

def trg_area(base, altura):
    x = (base * altura) / 2
    return x

triangulo = trg_area(trg_base, trg_altura)
print(f"Área del triangulo: {triangulo}")

print("------------------------------------------------")

cua_lado = 5

def cua_area(lado):
    x = lado**2
    return x

cuadrado = cua_area(cua_lado)
print(f"Área del cuadrado: {cuadrado}")

print("------------------------------------------------")

rec_base = 10
rec_altura = 5

def rec_area(base, altura):
    x = base * altura
    return x

rectangulo = rec_area(rec_base, rec_altura)
print(f"Área del rectangulo: {rectangulo}")

print("------------------------------------------------")

rom_diagonal_ma = 16
rom_diagonal_me = 12

def rom_area(diagonal_ma, diagonal_me):
    x = (diagonal_ma * diagonal_me) / 2 
    return x

rombo = rom_area(rom_diagonal_ma, rom_diagonal_me)
print(f"Área del rombo: {rombo}")

print("------------------------------------------------")

cir_radio = 5
pi = 3.1416

def cir_area(radio, pi):
    x = pi * (radio**2) 
    return x

circulo = cir_area(cir_radio, pi)
print(f"Área del circulo: {circulo}")

print("------------------------------------------------")

tra_base_ma = 9.5
tra_base_me = 3.5

def tra_area(base_ma, base_me):
    x = ((base_ma + base_me) * 4 ) / 2 
    return x

trapecio = tra_area(tra_base_ma, tra_base_me)
print(f"Área del trapecio: {trapecio}")

print("-----------------------PARAMETROS ARBITRARIOS-------------------------")

def saludar2(*args):
    for name in args:
        print(f'Nombre: {name}')
        
saludar2("Daniel", "Alex", "Pedro", "Brian", "Fernando")

tres_nums = [1, 2, 3]

def suma(num1, num2, num3):
    print(num1 + num2 + num3)
    
suma(*tres_nums)

print("---------------------EJERCICIO DE MULTIPLICACIÓN CON ARGUMENTOS ARBITRARIOS--------------------")
print("---------------------EMPAQUETADO--------------------")

def multiplicacion(*args):
    resultado = 1
    for num in args:
        resultado *= num
    print(f'La multiplicación es: {resultado}')
        
multiplicacion(3, 2, 1, 5, 6, 7, 9, 10)

print("---------------------DESEMPAQUETADO--------------------")

multi_num = [3, 2, 2, 2, 2]

def rev_multiplicacion(*args):
    res = 1
    for n in args:
        res *= n
    print(res)
    
rev_multiplicacion(*multi_num)