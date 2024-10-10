""" 
Escribe una comprensión de lista que tome una lista de temperaturas en grados 
Celsius y las convierta a grados Fahrenheit utilizando la fórmula F = (C * 9/5) + 32.
"""
celsius_list = [30, 34, 29, 42, 40]

fahrenheit = [(grados * 9/5) + 32 for grados in celsius_list]
print(fahrenheit)