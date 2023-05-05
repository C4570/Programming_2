'''
TAD - Lista con nodos enlazados

__init__ : inicia una lista vacia
insert   : agrega un elemento a la lista en la posicion dada 
index    : encuentra la posicion donde se encuentra un valro dado en una lista o si no se encuentra da error 
[]       : muestra si la lista esta vacia
remuve   : elimina un valor dado de la lista

'''
class Nodo:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next
        
    def insert(self, value, pos):
        if pos == 0:
            nodo = Nodo(value)
            nodo.next = self
            return nodo
        else:
            if self.next == None:
                self.next = Nodo(value)
            else:
                self.next = self.next.insert(value, pos-1)
                return self
            
    def index(self, valor, pos=0):
        if valor == self.cargo:
            return pos
        elif self.next == None:
            return -1
        else: 
            aux = self.next.index(valor, pos+1)
            if aux == -1:
                return -1
            else: 
                return aux
    
    def __str__(self):
        return f'Cargo: {self.cargo} next: {self.next}'
            
class ListaE:
    def __init__(self):
        self.head = None
    
    def insert(self, valor, pos):
        if self.head == None:
            self.head = Nodo(valor)
        else:
            self.head.insert(valor, pos)
    
    def index(self,valor):
        if self.head == None:
            return -1
        else:
            return self.head.index(valor)
    
    def __str__(self) -> str:
        representacion = '['
        if self.head:
            i = self.head
            while i != None:
                representacion += str(i) + ','
                i = i.next
        representacion += ']'
        return representacion

le = ListaE()

le.insert(2, 0)
le.insert(3, 1)
le.insert(4, 2)
le.insert(5, 3)

print(le)

print(le.index(5))



