"""
    Calculadora de IMC: Pide al usuario su peso en kilogramos y su altura en metros. 
    Luego, calcula e imprime su índice de masa corporal (IMC).
"""
print("\tCALCULADORA DE IMC\n")

altura = float(input("Ingresa tu altura: "))
peso = int(input("Ingresa tu peso en kilogramos: "))

def imc(peso, altura):
    imc = peso / (altura**2)
    return imc

x = imc(peso, altura)
print("Su indice de masa corporal es:", x)