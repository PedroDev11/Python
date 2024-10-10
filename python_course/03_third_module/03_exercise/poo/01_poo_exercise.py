""" 
Crea una clase llamada "Banco" que tenga una lista de cuentas bancarias como atributo. 
La clase debe tener métodos para agregar cuentas, realizar transferencias entre cuentas 
y calcular el saldo total del banco.
"""

class CuentaBancaria:
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

class Banco:
    def __init__(self):
        self.cuentas = []

    def agregar_cuenta(self, numero_cuenta, saldo):
        #Instanciamos la clase y le pasamos los parametros envíados en la función
        cuenta = CuentaBancaria(numero_cuenta, saldo)
        self.cuentas.append(cuenta)
        print(f"Cuenta bancaria con número: {numero_cuenta} -->> con Saldo: ${saldo} fué agregada con éxito")

    # Recibimos una cuenta de origen, destino y el saldo a transferir
    def realizar_transferencia(self, cuenta_origen, cuenta_destino, monto):
# Utilizamos la variable cuenta y buscamos las cuentas con un for dentro de self.cuentas (Recordemos 
# que self.cuentas tiene las cuentas que agregamos con la función anterior).
# después evaluamos accediendo al atributo numero_cuenta con el parametro envíado cuenta_origen
# de ser así evaluamos el saldo que tenga esta cuenta con el monto a transferir, si el saldo es mayor
# o igual al monto, procedemos a restar
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == cuenta_origen:
                if cuenta.saldo >= monto:
                    cuenta.saldo -= monto
# Utilizamos la variable cuenta_dest y buscamos las cuentas con un for dentro de self.cuentas para 
# después con esta variable podamos acceder al atributo numero_cuenta y posamos evaluar con la 
# cuenta destino que nos llega como parametro, de ser así utillizamos la variable cuenta_dest 
# y accedemos al atributo saldo para aumentarle la transferencia (monto) que fué pasado como parametro
# también 
                    for cuenta_dest in self.cuentas:
                        if cuenta_dest.numero_cuenta == cuenta_destino:
                            cuenta_dest.saldo += monto
                            print("\nTransferencia éxitosa, saldo actualizado correctamente")
                            return True               
                else:
                    print("\nSaldo insuficiente para realizar la transferencia")
                    return True
        print("\nLa cuenta de origen y/o destino no existe.")

    def calcular_saldo_total(self):
        # Accedemos al atributo saldo de la clase CuentaBancaria y se va sumando
        # y se va almacenando en el arreglo self.cuentas[] 
        saldo_total = sum(cuenta.saldo for cuenta in self.cuentas)
        return saldo_total

banco = Banco()

# Agregamos unas cuentas con su respectivo saldo
banco.agregar_cuenta("12345", 1000)
banco.agregar_cuenta("67890", 500)

# Realizamos una transferencia, pasandole como parametros la cuenta origen y la cuenta destino
# y el saldo que queremos depositar
banco.realizar_transferencia("12345", "67890", 300)

# Mostrar cuentas actualizadas
print("\nCuentas después de la transferencia:")
for cuenta in banco.cuentas:   
    print(f"Cuenta bancaria con número: {cuenta.numero_cuenta} -->> cuenta con un Saldo actualizado de: ${cuenta.saldo}")

# Calculamos el saldo total del banco entre todas (dos) las cuentas
saldo_total = banco.calcular_saldo_total()
print(f"\nSaldo total del banco: {saldo_total}")