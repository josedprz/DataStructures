

class Elemento:
    """ Creates an instance of Elemento. """
    def __init__(self, valor):
        """ Sets Element Value and Reference to next Element.

            Reference needs to be None. 
        """
        self.valor = valor
        self.siguiente = None

class Pila:

    def __init__(self):
        """ Creates a new Stack with size 0. """
        self.primero = None
        self.tamanio = 0

    def agregar_elemento(self, valor):
        """ Adds new element to the top of the Stack. """
        Nuevo = Elemento(valor)

        if self.tamanio == 0:
            self.primero = Nuevo
        else:
            actual = self.primero

            while actual.siguiente != None:
                actual = actual.siguiente

            actual.siguiente = Nuevo
        self.tamanio += 1

    def eliminar(self):
        """ Deletes top element of the Stack. """
        actual = self.primero
        anterior = None
        if self.tamanio != 0:
            while actual.siguiente != None:
                anterior = actual
                actual = actual.siguiente
            
            if anterior == None:
                self.primero = None
            else:
                anterior.siguiente = None
            self.tamanio -= 1

    
    def ver_pila(self):
        """ Shows the Stack
        
            Stores values inside list just for aesthetics
        """
        actual = self.primero
        lista = []
        while actual != None:
            lista.append(actual.valor)
            actual = actual.siguiente
            
        return print(lista)

nueva_pila = Pila()
nueva_pila.agregar_elemento(1) #
nueva_pila.agregar_elemento(2) #  Add 3 elements
nueva_pila.agregar_elemento(3) #
nueva_pila.ver_pila()          # Show Stack
nueva_pila.eliminar()          # Delete 1 element 
nueva_pila.ver_pila()          # Show Stack -1 element
nueva_pila.eliminar()          # Deleting remaining elements
nueva_pila.eliminar()          # 
nueva_pila.ver_pila()          # Show
