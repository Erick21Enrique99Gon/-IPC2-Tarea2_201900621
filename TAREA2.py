class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None
    
class lista:
    def __init__(self):
        self.inicio = None
        self.final = None
    
    def push(self,dato):
        nuevoNodo = Nodo(dato)

        if  self.inicio == None:
            self.inicio = nuevoNodo
            self.final = nuevoNodo
        else:
            nuevoNodo.anterior = self.final
            self.final.siguiente = nuevoNodo
            self.final = nuevoNodo
            self.final.siguiente = self.inicio
            self.inicio.anterior = self.final
    
    def pop(self):
        if self.inicio == None:
            return
        else:
            nodoaux = self.inicio
            self.inicio = self.inicio.siguiente
            self.inicio.anterior = self.final
            self.final.siguiente = self.inicio
            return nodoaux.dato
    
    def imprimir(self):
        aux = self.inicio
        while aux != None:
            print(aux.dato)
            if aux.siguiente == self.inicio:
                return
            aux = aux.siguiente

    def datos_numero(self,numero):
        aux = self.inicio
        print('Numero:',numero)    
        while aux != None:
            if aux.dato == numero:
                print('Numero anterior:',aux.anterior.dato)
                print('Numero porterior:',aux.siguiente.dato)
                return
            if aux.siguiente == self.inicio:
                return
            aux = aux.siguiente


l = lista()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.push(5)
print('----------')
l.imprimir()
print('----------')
l.datos_numero(5)