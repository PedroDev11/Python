""" 
Realiza un programa que extraiga los dígitos de la siguiente cadena de texto, que los ordene de menor a mayor
y los devuelve en una cadena de texto, que sume todos los dígitos y devuelve el resultado de la suma total.
Todoo estos resultados deben ser mostrados por consola de manera simultánea.
"""
def extractDigits(text):
    digits = ''
    
    for char in text:
        if char.isdigit():
            digits += char
    return digits

def sortDigits(digits):
    sortedDigits = sorted(digits)
    sortedStringDigits = ''.join(sortedDigits)
    return sortedStringDigits

def sumDigits(digits):
    total = sum(int(number) for number in digits)
    return total

def showResult(digits, sortedDigits, total):
    msg = f'''
Los dígitos extraidos son: {digits},
Los dígitos ordenados de menor a mayor son: {sortedDigits},
La suma de todos los dígitos es: {total}
'''
    print(msg)

text = '3ha4sa2df3as5f3ad5a4sdf8df6'
digits = extractDigits(text)
sortedDigits = sortDigits(digits)
total = sumDigits(digits)

showResult(digits, sortedDigits, total)