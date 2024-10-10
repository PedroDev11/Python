class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def moverse(self):
        return "Moviendose hacía adelante"

""" 
El polimorfismo nos permite trabajar con diferentes clases de manera uniforme, nos permite escribir código
flexible y reutilizable. Método comúnes que comparten diferentes clases llamadas polimorficas 
"""

class Pez(Animal):
    def moverse(self):
        return f"{self.nombre} nada a 20 km/h"
    
class Ave(Animal):
    def moverse(self):
        return f"{self.nombre} volando a 40 km/h"
    
class Perro(Animal):
    def moverse(self):
        return f"{self.nombre} corriendo a 15 km/h"
    
class Caja:
    def __init__(self):
        pass
    
    def almacenarObjeto(self):
        return "Almacenando objeto"
    
pez = Pez("Willy")
ave = Ave("Canario")
perro = Perro("Max")

objetos = [pez, ave, perro]

# Esta es una función genérica y se convierte en código reutilizable y flexible para una variedad 
# de objetos diferentes
def moverObjetos(objetos: list): 
    for obj in objetos:
        print(obj.moverse()) # Ejemplo de llamada polimorfica
        
moverObjetos(objetos=objetos)

caja = Caja()
cajas = [caja]

# Función específica para objetos caja o para un solo objeto
def almacenar(objetos: list):
    for obj in objetos:
        print(obj.almacenarObjeto())
        
almacenar(cajas)

class Figura():
    def __init__(self):
        pass
    
class Cuadrado(Figura):
    def __init__(self, lado):
        self.tipo = "Cuadrado"
        self.lado = lado
    
    def calcularArea(self):
        return self.lado ** 2
    
class Circulo(Figura):
    def __init__(self, radio):
        self.tipo = "Circulo"
        self.radio = radio
        self.PI = 3.14159
        
    def calcularArea(self):
        return self.PI * self.radio ** 2
    
class Triangulo(Figura):
    def __init__(self, base, altura):
        self.tipo = "Triangulo"
        self.base = base
        self.altura = altura
        
    def calcularArea(self):
        return (self.base * self.altura) / 2
    
class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.tipo = "Rectangulo"
        self.base = base
        self.altura = altura
        
    def calcularArea(self):
        return self.base * self.altura
    
class Rombo(Figura):
    def __init__(self, diagonalMayor, diagonalMenor):
        self.tipo = "Rombo"
        self.diagonalMayor = diagonalMayor
        self.diagonalMenor = diagonalMenor
        
    def calcularArea(self):
        return (self.diagonalMayor * self.diagonalMenor) / 2
    
cuadrado = Cuadrado(5)
circulo = Circulo(5)
triangulo = Triangulo(6, 5)
rectangulo = Rectangulo(5, 5)
rombo = Rombo(16, 12)


listaFiguras = [cuadrado, circulo, triangulo, rectangulo, rombo]


def calcularAreas(figuras):
    for figura in figuras:
        print(f"Esto es un {figura.tipo}, y su área es {figura.calcularArea()}\n")
        
calcularAreas(listaFiguras)