""" 
    Calculadora de descuento: Pide al usuario el precio de un producto y 
    el porcentaje de descuento. Luego, calcula y muestra el precio final después del descuento.
"""
print("\tCALCULA TÚ DESCUENTO\n")

producto = int(input("Introduce el costo de tú producto: "))
descuento = int(input("Introduce el porcentaje de descuento: "))

descuento = descuento / 100

def des(producto, descuento):
    producto -= producto * descuento
    return producto

resultado = des(producto, descuento)
print(f'\nFelicidades por tu compra de ${producto} usted obtuvo un descuento y ahora paga ${resultado}')

