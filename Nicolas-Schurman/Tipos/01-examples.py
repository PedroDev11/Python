print("-----------Secuencias de escape---------------")
#Secuencias de escape \", \', \\

curso = "Ultimate \"Python\""
print(curso)

print("-----------Números---------------")
#números 
# 2 + 2i -> I means, la raíz cuadrada de -1 porque no existe ningún número que multiplicado por 
# si mismo nos de -1, la i es de imaginario
imaginario = 2 + 2j # 2 + 2i
numero = 2

numero += 2

print(f"numero: {numero}")
print(1 / 3) 
print(1 // 3) # sin decimales
print(8 % 3) # cuantas veces cabe el 3 en el 8
print(2 ** 3) # potencia

print("-----------Funciones nativas---------------")
#Funciones nativas 
print(round(1.3)) # Devuelve el número al que se encuentre mas cercano, osea el 1
# Devuelve el valor absoluto del número que nosotros le pasemos a esta función, lo que hace el valor 
# absoluto es que saca el signo sea positivo o negativo de la ecuación, siempre nos entrega un positivo
print(abs(-11))

import math
print(math.ceil(1.1)) # Toma el número y va a llevarlo al número superior más cercano
print(math.floor(1.99999)) # Toma el número y lo va a llevar al número entero más cercano hacía abajo
# Si el valor que le estamos pasando corresponde a que no es un número, solo acepta números reales ("23") 
print(math.isnan(23))
print(math.pow(10, 3)) # Eleva un número a la potencia
print(math.sqrt(9)) # Sacará la raíz cuadrada del número que nosotros le pasemos


print("-----------Conversión de tipos---------------")
# int()
# str()
# float()
# bool()
print(bool("")) # True
print(bool(0)) # False