""" 
    Conversor de unidades de longitud: Pide al usuario una distancia en metros y 
    conviértela a centímetros y pulgadas. Muestra los tres valores.
"""
print("\tCONVERSOR DE UNIDADES DE LONGITUD\n")

metros = int(input("Ingresa una distancia en metros: "))

def centimetros(metros):
    cm = metros * 100
    return cm

def pulgadas(metros):
    pg = metros * 39.3701
    return pg

cm = centimetros(metros)
pg = pulgadas(metros)

msg = f"""
Valores de respuesta\n
Mestros: {metros}
Centimetros: {cm} 
Pulgadas: {pg}
"""

print(msg)