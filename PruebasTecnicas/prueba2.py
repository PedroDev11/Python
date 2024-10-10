""" 
Realiza una función 'multiplicar' que no utilice el símbolo de multiplicación
"""

def multipliar(n1, n2):
    result = 0
    
    for rep in range(n1):
        result += n2
    return result

total = multipliar(5, 7)
print(f"Resultado de la multiplicación: {total}")