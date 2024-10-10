"""
# EXAMPLES

print("----------------PERSON CLASS-----------------\n")
class Persona:
    def __init__(self, nombre, apellidos, edad, sexo):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.sexo = sexo
        
    def saludar(self):
        print(f'Hola, mi nombre es: {self.nombre} {self.apellidos}, tengo {self.edad} años y mi sexo es {self.sexo}')

persona1 = Persona("Pedro", "RV", 22, "M")

print(persona1.nombre)
persona1.saludar()
print("----------------CAR CLASS-----------------\n")

class Carro:
    def __init__(self, color, velocidad_maxima, marca, velocidad_actual = 0):
        self.color = color
        self.velocidad_maxima = velocidad_maxima
        self.marca = marca
        self.velocidad_actual = velocidad_actual
        
    def acelerar(self, velocidad):
        print(f"Avanzando hasta {velocidad}")
        self.velocidad_actual = velocidad
    
    def avanzar_hasta_maximo(self):
        print(f'Avanzando hasta: {self.velocidad_maxima} km/h')
        self.velocidad_actual = self.velocidad_maxima
    
    def frenar(self, velocidad):
        print(f"Frenando hasta: {velocidad}")
        if velocidad >= self.velocidad_actual:
            raise Exception("No puedes frenar a una velocidad mayor a la actual")
        self.velocidad_actual = velocidad
    
    def obtener_velocidad_actual(self):
        print(self.velocidad_actual)
        
        
carro1 = Carro("Rojo", 200, "Honda")

carro1.acelerar(10)
carro1.obtener_velocidad_actual()
carro1.frenar(5)
carro1.obtener_velocidad_actual()
carro1.avanzar_hasta_maximo()
carro1.obtener_velocidad_actual()"""

# EXCERCIES

print("----------------RECTANGÚLO CLASS-----------------\n")
# Crear una clase rectangulo que tenga los siguientes atributos, ancho, alto 
# y que tenga un metodo para calcular su area

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def area(self):
        return (self.base * self.altura) / 2

area1 = Rectangulo(4, 4)

print("La área del rectangúlo es la siguiente: ", area1.area())

print("----------------ANIMALS CLASS-----------------\n")

# Crear una clase animal con atributos nombre de animal, peso, color, dieta, abitad, sonido 
# y que tenga un método que se llame hacer sonido y que obtenga el peso

class Animal:
    def __init__(self, nombre, peso, color, dieta, abitad, sonido):
        self.nombre = nombre
        self.peso = peso
        self.color = color
        self.dieta = dieta
        self.abitad = abitad
        self.sonido = sonido
        
    def hacer_sonido(self):
        print(f'El sonido del animal {self.nombre} es el siguiente: {self.sonido}')
        
    def obtener_peso(self):
        print(f'El peso del animal es el siguiente: {self.peso} kg')
        
animal1 = Animal("Leon", 190, "Anaranjado bonito", "Carne/Carniboro", "Selva", "Rugido")
animal1.hacer_sonido()
animal1.obtener_peso()

print("----------------ESTUDENT CLASS-----------------\n")
# Crear clase estudiante con atributos nombre, edad, lista de materias y que tenga como método 
# que imprima cada una de las materias y que diga cuantas tiene 

materias = ["Español", "Matemáticas", "Fílosofia", "Física"]

class Estudiante:
    def __init__(self, nombre, edad, materias):
        self.nombre = nombre
        self.edad = edad
        self.materias = materias
        
    def list_materias(self):
        msg = f"""
        Las materias del alumno: {self.nombre},
        son las siguientes: {self.materias},
        total de materias: {len(self.materias)}
        """
        print(msg)

estudiante1 = Estudiante("Pedro", 22, materias)

estudiante1.list_materias()

print("----------------BOOK CLASS-----------------\n")

# Clase llamada libro con atributos como el titulo del libreo, autor, feha de publicacion, 
# genero y que tenga un método que devuelva un diccionario con los atributos 

class Libro:
    def __init__(self, titulo, autor, date, genero):
        self.titulo = titulo
        self.autor = autor
        self.date = date
        self.genero = genero
    
    def make_dict(self):
        diccionarie = {
            "Título": self.titulo,
            "Autor": self.autor,
            "Fecha de publicación": self.date,
            "Genero": self.genero
        }
        for key, item in diccionarie.items():
            print(f'{key}: {item}')
    
libro1 = Libro("Si hubiera espinas", "Virginia Andrews", "12/02/2006", "Suspenso")
libro1.make_dict()
