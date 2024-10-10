""" 
1. Comprueba que los números de la lista sean pares
2. Encuentra los números pares únicos de la lista
3. Suma estos números pares únicos de la lista y muestralo por consola
"""

def is_even_number(number):
    return number % 2 == 0

def find_unique_even_number(numbers):
    unique_even_number = set()
    for number in numbers:
        # nos dice si es par 
        if is_even_number(number):
            # si es par lo añadimos al set
            unique_even_number.add(number)
    return unique_even_number

def sum_numbers(numbers):
    return sum(numbers)

numbers = [1, 2, 3, 4, 5, 6, 12, 9, 8, 25, 32, 2, 4, 6]

unique_even_numbers = find_unique_even_number(numbers)
result = sum_numbers(unique_even_numbers)
print(f"La suma de los números pares y únicos de la lista es: {result}")