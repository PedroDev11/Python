productos = {
    "Leche": 12.30,
    "Mermelada": 15.69,
    "Mayonesa": 19.99,
    "Yogurt": 10.02,
    "Helado": 25.45,
    "Carne": 30.55,
    "Chetos": 5.99
}

name = input("Ingrese el nombre del producto a buscar: ")
product = productos.get(f"{name}", 'No se encontró el producto ingresado')

if product == 'No se encontró el producto ingresado':
    print(product)
else:
    print(f'El producto: {name}, tiene un precio de: {product}')