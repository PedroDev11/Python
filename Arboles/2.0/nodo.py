class Nodo:
    def __init__(self, x):
        self.padre = None
        self.hijo_izq = None
        self.hijo_der = None
        self.clave = x
        
        #__str__ sería la representación en string (cadena) del objeto de la clase Nodo
        def __str__(self):
            cadena = "Nodo " + str(self.clave) + " ---> "
            
            if self.padre != None:
                cadena += "\tpadre: " + str(self.padre.clave)
            else:
                cadena += "\tpadre: Ninguno"
            if self.hijo_izq != None:
                cadena += "\th_izq: " + str(self.hijo_izq.clave)
            else:
                cadena += "\th_izq: Ninguno"
            if self.hijo_der != None:
                cadena += "\th_der: " + str(self.hijo_der.clave)
            else:
                cadena += "\th_der: Ninguno"
            cadena += "\n"
            return cadena
        
class ArbolBin:
    def __init__(self):
        self.raiz = None
        
    def mostrarArbolBin(self, sangria = 4):
        if self.raiz == None:
            print("El arbol esta vacío")
            return
        
        print("El arbol es: ")
        def mostrarArbolBinRec(nodo, cadena):
            print(str(nodo.clave))
            
            #Para el hijo izquierdo
            if nodo.hijo_izq != None:
                if nodo.hijo_der != None: #para colocar el caracter | o no en la impresion
                    print(cadena + "|" + "-" * sangria, end="")
                else:
                    print(cadena + "->" + "-" * sangria, end="")
                mostrarArbolBinRec(nodo.hijo_izq, cadena + "|" + " " * sangria)
            
            #para el hijo derecho
            if nodo.hijo_der != None:
                print(cadena + "->" + "-" * sangria, end="")
                mostrarArbolBinRec(nodo.hijo_der, cadena + "|" + " " *sangria)
                
        mostrarArbolBinRec(self.raiz, "")
        
        