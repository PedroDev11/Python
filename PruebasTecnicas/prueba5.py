""" 
Se le debe dar la vuelta al texto entregado, el ejercicio se realizará sin utilizar las librerías 
y/o utilidades de Python
print(''.join(reversed(text)))
"""

def reversedText(text):
    result = ""
    
    for letter in text:
        result = letter + result
    return result

text = "Bienvenidos a Pedro"

reversed = reversedText(text)
print(reversed)