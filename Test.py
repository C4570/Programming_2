
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
                self.next = self.next.insert(value,pos-1)
                return self
                
    def index(self, valor):
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
    
    def __str__(self):
        return f'Cargo: {self.cargo} next: {self.next}'
    
class ListaE:
    def __init__(self):
        self.head = None
    
    def insert(self, value, pos):
        if self.head is None:
            self.head = Nodo(value)
        else:
            self.head.insert(value, pos)
            
    def index(self,valor):
        pass

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