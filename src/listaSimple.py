from colorama import Fore, init


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
        aux = self.cabeza
        while aux:
            minimo = aux
            siguiente = aux.siguiente
            while siguiente:
                if float(getattr(siguiente.dato, llave)) < float(getattr(minimo.dato, llave)):
                    minimo = siguiente
                siguiente = siguiente.siguiente
            if aux != minimo:
                aux.dato, minimo.dato = minimo.dato, aux.dato
            aux = aux.siguiente
        self.imprimir10(llave)

    def imprimir10(self, llave):
        cad = llave
        cad += ':'
        aux = self.cabeza
        for i in range(1, 11):
            if aux:
                print(Fore.CYAN + str(i) + '.'+Fore.YELLOW +
                      'Codigo: '+Fore.RESET + aux.dato.codigo +
                      Fore.LIGHTRED_EX + ' - '+Fore.YELLOW + cad + Fore.RESET + str(getattr(aux.dato, llave)))
                aux = aux.siguiente

    def imprimir(self, llave):
        cad = llave
        cad += ':'
        aux = self.cabeza
        while aux is not None:
            print('Codigo: ', aux.dato.codigo)
            print(cad, str(getattr(aux.dato, llave)))
            aux = aux.siguiente

    
