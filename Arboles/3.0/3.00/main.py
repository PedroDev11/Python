from arbol3 import Node, BinarySearchTree, InPreOrder

# Función para probar las clases
def testBinarySearchTree():
    '''
    Ejemplo
                  8
                 / \
                3   10
               / \    \
              1   6    14
                       /
                      13 
          
    '''

    '''
    Ejemplo luego del borrado
                  7
                 / \
                1   4

    '''
    # Instancia del árbol binario de búsqueda
    t = BinarySearchTree()
    #Insertamos los elementos
    t.insert(8)
    t.insert(3)
    t.insert(6)
    t.insert(1)
    t.insert(10)
    t.insert(14)
    t.insert(13)
    n1 = int(input("Ingresa un número: "))
    t.insert(n1)
    
    #t.insert(4)
    #t.insert(7)

    print(t.__str__())

    # if(t.getNode(6) is not None):
    #     print("El elemento 6 existe")
    # else:
    #     print("El elemento 6 no existe")

    # if(t.getNode(-1) is not None):
    #     print("El elemento -1 existe")
    # else:
    #     print("El elemento -1 no existe")
    
    # if(not t.empty()):
    #     print(("Valor Max: ", t.getMax().getLabel()))
    #     print(("Valor Min: ", t.getMin().getLabel()))
    
    # t.delete(13)
    # t.delete(10)
    # t.delete(8)
    # t.delete(3)
    # t.delete(6)
    # t.delete(14)

    # Obtenemos todos los elementos del árbol en preorden
    list = t.traversalTree(InPreOrder, t.root)
    for x in list:
        print(x)

if __name__ == "__main__":
    testBinarySearchTree()
