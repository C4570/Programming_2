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
    
    def __str__(self):
        return f'Cargo: {self.cargo} next: {self.next}'
    
class ListaE:
    def __init__(self):
        self.head = None
    
    def insert(self, value, pos):
        if self.head == None:
            self.head = Nodo(value)
        else:
            i = self.head
            c = 0
            while c != pos-1:
                i = i.next
                c+=1
            nodo = Nodo(value)
            nodo.next = i.next
            i.next = nodo
            
    def index(self,valor):
        if (self.head == None):
            return -1
        else:
            i = self.head
            c = 0
            while (i != None):
                if (valor == i.cargo):
                    return c
                else:
                    c+=1
                    i = i.next
            return -1

    def remove(self,valor):
        if (self.head == None):
            return -1
        else:
            i = self.head
            i_ant = None
            while i.next != None:
                if (valor == i.cargo):
                    i_ant.next = i.next
                    return
                else:
                    i_ant = i
                    i = i.next
            return -1

    def __getitem__(self, index):
      if self.head == None:
        return -1
      else:
        i = self.head
        c = 0
        while (i.next != None):
          if (index == c):
            return i.cargo
          else:
            i = i.next
            c += 1
        return -1
    
    def __str__(self):
      representacion = "["
      if self.head:
        i = self.head
        while i != None:
          representacion += str(i)
          representacion +=", "
          i = i.next
      representacion += "]"
      return representacion
            
le = ListaE()
le.insert(2, 0)
le.insert(3, 1)
le.insert(4, 2)
le.insert(5, 3)
print(le)