def divisora(a, b):
    try:
        resultado = a / b
    except ZeroDivisionError as e:
        print("Exception type zero division")
        return False
    except TypeError as e:
        print("Exception of type error")
        return False
    else:
         print("Se ejecuta cuando no hay exceptions")
    finally:
        print("Esto se ejecuta siempre")
    return resultado

print(divisora(100, 5))