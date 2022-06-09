class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
    
class lista:
    def __init__(self):
        self.inicio = None
        self.final = None
    
    def encolar(self,dato):
        nuevoNodo = Nodo(dato)

        if  self.inicio == None:
            self.inicio = nuevoNodo
            self.final = nuevoNodo
        else:
            nuevoNodo.anterior = self.final
            self.final.siguiente = nuevoNodo
            self.final = nuevoNodo
    
    def desencolar(self):
        if self.inicio == None:
            return
        else:
            nodoaux = self.inicio
            self.inicio = self.inicio.siguiente
            self.inicio.anterior = None
            return nodoaux.dato
    
    def imprimir(self):
        aux = self.inicio
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente
