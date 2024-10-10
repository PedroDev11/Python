""" 
Crea una clase "Zoológico" que tenga una lista de animales como atributo. Cada 
animal debe tener nombre, especie y edad. La clase debe tener métodos para agregar 
animales, mostrar todos los animales de una especie específica y calcular la edad promedio 
de los animales en el zoológico.
"""

class Animal:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

class Zoologico:
    def __init__(self):
        self.animales = []

# Agregamos un método para guardar animales
    def agregar_animal(self, nombre, especie, edad):
        animal = Animal(nombre, especie, edad)
        self.animales.append(animal)
        print(f"El animal: {nombre}, de la Especie: {especie}, con Edad: {edad} fué agregado correctamente")

    def mostrar_animales_especie(self, especie):
# Creamos una list_comprenhencion donde creamos una variable animal y esta recorrerá self.animales
# y esta tiene los atributos de nombre, especie y edad, y agregamos una condición donde si el 
# atributo especie de la variable animal es igual al parametro que nos estan pasando, los almacene
# solo unicamente cuando esta condicional se cumple se guarda 
        animales_list = [animal for animal in self.animales if animal.especie == especie]
# Evaluamos si es que tenemos animales en nuestra lista de animales y sí es así procedemos a imprimir
# los animales recorriendo con un ciclo for esta lista de animales con la ayuda de una variable 
        if animales_list:
            print(f"\nAnimales de la especie {especie}:")
            for animal in animales_list:
                print(f"Los animales de la especie {animal.especie} son los siguientes: {animal.nombre} y tienen una edad de: {animal.edad}")
        else:
            print(f"No hay animales de la especie {especie} en el zoológico.")

    def calcular_edad_promedio(self):
# Ocupamos la funcion sum() y le pasamos como parametros una list_comprenhencion con una variable 
# animal que recorra a self.animales ya que esta tiene todos los atributos de los animales agregados
# y una vez con esto, accedemos al atributo edad de la variable animal ya que cuenta con todos los 
# datos de los animales, una vez teniendo esta suma, procedemos a sacar el promedio haciendo 
# la operación de la edad total de los animales entre y aquí ocupamos la función len() para contar 
# cuantos animales son los que se tiene y así poder obtener el promedio. 
        edad_total = sum(animal.edad for animal in self.animales)
        edad_promedio = edad_total / len(self.animales)
        print(f"\nEdad promedio de todos los animales en el zoológico es de: {edad_promedio}")

zoo = Zoologico()

print("Agregando algunos animalitos:")
zoo.agregar_animal("León", "Felino", 5)
zoo.agregar_animal("Tigre", "Felino", 7)
zoo.agregar_animal("Ballena", "Mamifero", 10)
zoo.agregar_animal("Gorila", "Primate", 8)
zoo.agregar_animal("Gato", "Felino", 10)

zoo.mostrar_animales_especie("Felino")

zoo.calcular_edad_promedio()