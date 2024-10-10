"""
Dada una lista de números, crea una nueva lista que contenga solo los números pares
"""
number_list = [100, 2, 5, 7, 8, 9, 12, 18, 16]

par = [number for number in number_list if number % 2 == 0]
print(par)