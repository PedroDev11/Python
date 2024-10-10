""" 
Crear una función que devuelva una lista ordenada de menor a mayor.
Nota --> no se pueden utilizar ni sorted() ni librerías 
"""

def bubbleSort(arrayNums):
    change = True
    while change:
        change = False
        # nos trae el tamaño del arreglo pero este arreglo nos devuelve el valor 5 sin contar el índice 0, 
        # así que por eso se le resta uno
        for num in range(len(arrayNums) - 1):
            # le indicamos que sí, en arrayNums en el índice del 0 al 4, por ejemplo vamos a comparar, 
            # aquí al principio va a valer 0 la primer iteración, por lo tanto vamos a comparar si el 7 
            # es mayor al 5 (arrayNums[num + 1]) posición 1
            if arrayNums[num] > arrayNums[num + 1]:
                # Como si se cumple la condición, entonces toma la posición 0 del número 7
                temp = arrayNums[num]
                
                # ahora le indicamos que la posición 0 que le pertenece al 7, tome la siguiente posición
                arrayNums[num] = arrayNums[num + 1]
                
                # ahora donde estaba el 7 va estar el 5 y donde estaba el 5 va estar el 7
                arrayNums[num + 1] = temp
                change = True
    return arrayNums
arrayNums = [7, 5, 4, 9, 2]

result = bubbleSort(arrayNums)
print(result)