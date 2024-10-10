my_condition = False

if my_condition == False:
    print("Se ejecuta la condicional if")

my_condition = 67

if my_condition >= 20 and my_condition <= 30:
    print("El número introducido es mayor o igual que 20 o menor o igual que 30")

elif my_condition >= 50 and my_condition <=80:
    print("El número introduccido es:", my_condition)

else:
    print("El número esta fuera del rango de 20 a 30")
    print("El número introduccido puede que sea menor que 20 o mayor que 30")

print("La ejecución continua")

my_string = "Pepe"

if my_string:
    print("La cadena de texto no es vacía")
else:
    print("Es necesario que rellene los campos solicitados")

my_string = ""

if not my_string:
    print("La cadena de texto esta vacía")
else:
    print("Es necesario que rellene los campos solicitados")