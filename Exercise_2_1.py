'''
TAD - Celda

__init__ : Inicia una celda vacia 
insert   : Agrega un nuevo elemento a la celda y si habia uno lo pisa
__str__  : Muestra la celda

'''

class Nodo:
    def __init__(self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next
    
    def __str__(self):
        return f'Cargo: {self.cargo}'
    

class Celda:
    def __init__(self):
        self.head = None
        
    def insert(self, valor):
        self.head = Nodo(valor)
        
    def __str__(self):
        representacion = "["
        representacion += str(self.head)
        representacion += "]"
        return representacion
    
celda = Celda()
celda.insert(1)
print(celda)

celda.insert(2)
print(celda)

celda.insert(3)
print(celda)