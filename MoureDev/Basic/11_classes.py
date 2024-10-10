class MyPerson: 
    pass

class Person:
    def __init__(self, name, lastname): 
#Constructor de clase y que sea capas de guardar valores, el contructor sirve para crear la instancia
        self.namee = name #creamos propiedades dentro de persona y las igualamos a las variables del contructor
        self.lastname = lastname #Las definimos con self y le asignamos el valor de la variable
    
my_person = Person("Pedro", "Rojas")
print(my_person.namee)
print(f"{my_person.namee} {my_person.lastname}")
print("--------------------------------------------------")

class Person2: #Clase con valores predefinidos
    def __init__(self): 
        self.name = "Pepe"
        self.lastname = "Rojas Valladares" 
    
my_person2 = Person2()
print(f"{my_person2.name} {my_person2.lastname}")

print("--------------------------------------------------")

class Person3: #Clase dandole formato desde dentro
    def __init__(self, name, lastname): #Ya no se almacena el valor de name y lastname
        self.full_name = f"{name} {lastname}" #se crea una propiedad almacenada que es full_name
    
my_person3 = Person3("pepe", "rojas v.")
print(my_person3.full_name)

class Person4: 
    def __init__(self, name, lastname, alias = "Sin alias"): 
        self.full_name = f"{name} {lastname} ({alias})" #propiedad pública
        self.__name = name #creamos propiedades privadas para que no se puedan acceder a ellas
        self.__lastname = lastname
    
    def get_name(self):
        return self.__name #retornamos el valor de name pero solo como escritura
    
    def walk(self):
        print(f"{self.full_name} Esta caminando")

print("--------------------------PASANDOLE PARAMETROS SIN ALIAS------------------------")
my_person4 = Person4("pepe", "rojas v.")
print(my_person4.full_name)
my_person4.walk()

print("--------------------------ALIAS------------------------")
#definiendole un alias
my_other_person = Person4("pepe", "rojas", "Pedro") #definimos una variable que acceda a la clase person
print(my_other_person.full_name)
my_other_person.walk()

print("--------------------------CAMBIAMOS EL VALOR DE FULL_NAME------------------------")
#cambiamos el valor de full name, por que no esta fuertemente typado
my_other_person.full_name = "Hector (El loco de los perros)"
print(my_other_person.full_name)
my_other_person.walk()

print("--------------------------ACCDEMEMOS A LA PROPIEDAD PRIVADA------------------------")
print(my_person4.get_name())