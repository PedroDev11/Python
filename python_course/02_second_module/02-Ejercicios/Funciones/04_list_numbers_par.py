def numeros_pares(n):
    if n < 1:
        return []
    else:
        return [i for i in range(2, n + 1, 2)]

numero = int(input("Ingresa un numero par: "))  
lista_pares = numeros_pares(numero)
print(lista_pares)