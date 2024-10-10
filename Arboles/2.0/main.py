from nodo import ArbolBin, Nodo

n1 = int(input("Ingresa un número: "))

arbol = ArbolBin()
nodo1 = Nodo(5); arbol.raiz = nodo1
nodo2 = Nodo(n1); nodo1.hijo_izq = nodo2; nodo2.padre = nodo1
nodo3 = Nodo(3); nodo3.padre = nodo1; nodo1.hijo_der = nodo3
nodo4 = Nodo(20); nodo4.padre = nodo2; nodo2.hijo_izq = nodo4
nodo5 = Nodo(10); nodo5.padre = nodo2; nodo2.hijo_der = nodo5
nodo6 = Nodo(7); nodo6.padre = nodo4; nodo4.hijo_izq = nodo6
nodo7 = Nodo(4); nodo7.padre = nodo4; nodo4.hijo_der = nodo7

arbol.mostrarArbolBin()

