#Exception Handling
x = 5
y = 5
y = "110"

#try except 
try:
  print(x + y)
  print("No se ha producido algún error")
except: #se ejecuta si se produce una excepción
  print('An exception occurred\n')

#try expet else finally
try:
  print(x + y)
except:
  print('An exception occurred')
else: #se ejecuta si no se produce una excepción 
    print("La ejecución continúa correctamente")
finally: #se ejecuta siempre
    print("La ejecución continúa\n")

#Captura de excepciones por tipo
try:
  print(x + y)
  print("No se ha producido algún error")
except TypeError:
  print("Se ha prducido un TypeError\n")
except ValueError:
  print("Se ha prducido un ValueError")
  
#captura de la información de la excepción
try:
  print(x + y)
  print("No se ha producido algún error")
except ValueError as e:
  print("Se ha prducido un TypeError")
  print(e)
except Exception as e: 
#Excepción genérica, en el caso de que el error que se produce no es ValueError, se nos va por el bloque de Exception
    print(e)