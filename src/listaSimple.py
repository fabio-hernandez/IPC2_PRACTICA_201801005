class Nodo:

    def __init__(self, dato=None, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente


class listaSimple:

    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tamanio = 0

    def insertar(self, dato):
        if self.cabeza is None:
            nuevo = Nodo(dato)
            self.cabeza = nuevo
            self.ultimo = nuevo
            self.tamanio += 1
        else:
            nuevo = Nodo(dato)
            self.ultimo.siguiente = nuevo
            self.ultimo = self.ultimo.siguiente
            self.tamanio += 1

    def ordenar(self, llave):
        if not self.cabeza or not self.cabeza.siguiente:
            return
        aux = self.cabeza
        while aux:
            min_node = aux  
            siguiente = aux.siguiente
            while siguiente:
                if siguiente.dato[llave] < min_node.dato[llave]:
                    min_node = siguiente
                siguiente = siguiente.siguiente
            if aux != min_node:
                aux.dato, min_node.dato = min_node.dato, aux.dato
            aux = aux.siguiente

    def get_top_10(self):
        top_10 = []
        aux = self.cabeza
        for i in range(10):
            if aux:
                top_10.append(aux.dato)
                aux = aux.siguiente
        return top_10

    def imprimir(self):
        aux = self.cabeza
        while aux is not None:
            print('Code: ', aux.dato.codigo)
            aux = aux.siguiente
