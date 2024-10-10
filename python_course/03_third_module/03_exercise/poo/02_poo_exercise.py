""" 
Define una clase "Tienda" que tenga una lista de productos como atributo. Los productos deben 
tener nombre, precio y cantidad en stock. La clase debe tener métodos para 
agregar productos, vender productos y calcular el valor total del inventario.
"""

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        producto = Producto(nombre, precio, cantidad)
        self.productos.append(producto)
        print(f"{nombre} -> Precio: ${precio} -> Stock: {cantidad}")

    def vender_producto(self, nombre, cantidad):
# Se crea una variable producto que recorre los productos agregados de self.productos, después 
# con esta variable accedemos al atributo nombre para después evaluar con el parametro que nos llega 
# para verificar si existe dicho producto, una vez haya pasado este primer filtro, procedemos a aceder 
# al atributo cantidad para evaluar con el parametro cantidad que nos estan pasando, y verificar que si 
# tengamos suficiente stock para proceder a hacer dicha venta, de ser verdadero osea después de haber 
# pasado este segundo filtro procedemos a restar la cantidad que se tiene en stock y así hacer 
# dicha venta
        for producto in self.productos:
            if producto.nombre == nombre:
                if producto.cantidad >= cantidad:
                    producto.cantidad -= cantidad
                    print(f"Producto: {nombre} vendido exitosamente, se vendieron: {cantidad} piezas")
                else:
                    print("No hay suficiente stock para vender.")
                return True
        print(f"El producto: {nombre} no se encuentra en la lista, favor de agregarlo")

    def calcular_valor_inventario(self):
# Utilizamos una variable externa que nos ayudará a guardar valores, despues procedemos a recorrer
# los productos de self.productos con una variable producto, dentro de este ciclo for procedemos 
# a utilizar la variable de apoyo para usar el operador y asignación para asignarle el resultado 
# del precio del producto por la cantidad y así obtener el valor total del inventario  
        valor_total = 0
        for producto in self.productos:
            valor_total += producto.precio * producto.cantidad
        return valor_total

tienda = Tienda()

print("Inventario:")
tienda.agregar_producto("Leche", 25, 25)
tienda.agregar_producto("Mermelada", 22, 30)
tienda.agregar_producto("Cheetos", 12, 32)

print("\nProcedemos a vender un producto:\n")
tienda.vender_producto("Leche", 400)
tienda.vender_producto("Platano", 20)

# Mostrar inventario actualizado
print("\nInventario después de vender productos:")
for producto in tienda.productos:
    print(f"Producto: {producto.nombre} -> Precio: {producto.precio} -> Stock: {producto.cantidad}")

valor_total = tienda.calcular_valor_inventario()
print(f"\nEl valor total del inventario es de: ${valor_total}")
