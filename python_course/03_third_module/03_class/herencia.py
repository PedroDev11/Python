"""class Animal():
    def __init__(self, edad, especie):
        self.edad = edad
        self.especie = especie
        
    def comer(self):
        print("Comiendo")
        
    def dormir(self):
        print("Durmiendo")
        
class Perro(Animal):
    def __init__(self, edad, especie, raza, nombre):
        super().__init__(edad, especie)
        self.raza = raza
        self.nombre = nombre
        
    def hacer_ruido(self):
        print("Woff")
        
    def obtener_detalles(self):
        return {"nombre": self.nombre, "especie": self.especie, "raza": self.raza}
    
class Gato(Animal):
    def __init__(self, edad, especie, dieta):
        super().__init__(edad, especie)
        self.dieta = dieta
    
    def hacer_sonido(self):
        print("Miauu")
        
    def desventaja(self):
        print("Tira mucho pelo")
        
gato1 = Gato(2, "Felino", "Croquetas")

print(gato1.edad)
print(gato1.especie)
gato1.dormir() # Mandamos a llamar un método de la clase padre

perro1 = Perro(10, "perrito", "pitbull", "scooby")
print(perro1.edad)"""

""" 
Generar una clase padre llamada Vehiculo que tenga los atributos: marca y modelo, definir un método
obtener detalles que regrese un diccionario con los atributos de la clase, definir 3 clases hijas 
llamadas Carro, Bicibleta y Motocicleta, que tengan características propias de cada una y que 
hereden los atributos de la clase padre Vehiculo, cada clase hija debe tener un método propio
según el tipo de vehículo, llamado 
"""

class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def obtener_detalles(self):
        return {"Marca:": self.marca, "Modelo:": self.modelo}

class Carro(Vehiculo):
    def __init__(self, marca, modelo, placas, velocidad_actual = 0):
        super().__init__(marca, modelo)
        self.placas = placas
        self.velocidad_actual = velocidad_actual
        
    def acelerando(self, acelerar):
        print(f"Velocidad actual: {self.velocidad_actual} km")
        print(f"acelerando hasta {acelerar} km")
        self.velocidad_actual = acelerar
        print(f"Velocidad actual: {self.velocidad_actual} km")
        

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, color, rodada):
        super().__init__(marca, modelo)
        self.color = color
        self.rodada = rodada
        
    def cambio_de_color(self, color_nuevo):
        print(f"Actualmente tu bicibleta tiene el color {self.color}")
        self.color = color_nuevo
        print(f"Se ha cambiado el color de tu bicileta por el color: {self.color}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, cilindros, gasolina):
        super().__init__(marca, modelo)
        self.cilindros = cilindros
        self.gasolina = gasolina
        
    def agregar_gasolina(self, gasolina_agregada):
        print(f"Gasolina actual: {self.gasolina} litros")
        self.gasolina += gasolina_agregada
        print("Gasolina agregada con éxito")
        print(f"Gasolina actual: {self.gasolina} litros")
        
        
vehiculo1 = Vehiculo("Chevrolet", "RAPTOR")
print(vehiculo1.obtener_detalles())
print("\n")

carro1 = Carro("Honda", "HSBO", "HG123P")
carro1.acelerando(10)
print("\n")

bicicleta1 = Bicicleta("Skate", "HSB132", "Gris", 22)
bicicleta1.cambio_de_color("verde")
print("\n")

moto1 = Motocicleta("Yamaha", "150", 2, 10)
moto1.agregar_gasolina(12)