class Nodo:
    """
        Node class.

        Attributes:
            valor = Node value.
            ref = Reference to next Node.
    """
    def __init__(self, Valor):
        self.valor = Valor
        self.ref = None


class ListaEnlazada:

    def __init__(self):
        """ Creates a new Linked List.
        
            Starts with size = 0 and has no First Node.
        """
        self.primero = None
        self.tamanio = 0

    def agregar_nodo(self, Valor):
        """ Adds new Node at end of List. """
        Nuevo = Nodo(Valor)

        if self.tamanio == 0 :
            self.primero = Nuevo
        else:
            actual = self.primero

            while actual.ref != None:
                actual = actual.ref

            actual.ref = Nuevo
        self.tamanio = self.tamanio + 1

    
    def agregar_inicio(self, valor):
        """ Adds new Node at the beginning of the List. """
        Nuevo = Nodo(valor)

        if self.tamanio == 0:
            self.primero = Nuevo
        else:
            temp = self.primero
            self.primero = Nuevo
            self.primero.ref = temp
        self.tamanio += 1
        


    def quitar_nodo(self, Valor):
        """ Removes a Node matching the value. """
        actual = self.primero
        if self.tamanio != 0:
            while actual.valor != Valor:
                if actual.ref == None:
                    break
                else:
                    anterior = actual
                    actual = actual.ref

            if actual != None:
                if actual == self.primero:
                    self.primero = actual.ref
                else:
                    anterior.ref = actual.ref
            self.tamanio -= 1


    
    def verlista(self):
        """ Shows the List. """
        actual = self.primero
        lista = []
        while actual!= None:
            lista.append(actual.valor)
            actual = actual.ref
        return print(lista)


NuevaLista = ListaEnlazada()
NuevaLista.agregar_nodo(1)      #
NuevaLista.agregar_nodo(2)      # 
NuevaLista.agregar_nodo(3)      # Adds 3 Nodes.
NuevaLista.agregar_inicio(4)    # Adds Node at Start.
NuevaLista.agregar_inicio(7)    # Adds Node at Start.
NuevaLista.verlista()           # Shows List.
NuevaLista.quitar_nodo(7)       # Removes Node.
NuevaLista.quitar_nodo(1)       # Removes Node.
NuevaLista.verlista()           # Shows.

