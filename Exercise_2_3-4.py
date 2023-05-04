'''
TAD - Inmutable

__init__ : inicia un conjunto inmutable
index    : Muestra si el elemento esta o no en el conjunto

'''

class Conjunto:
    def __init__(self):
        self.conjunto = [1,2,3,4,5,6,7,8,9, "Hola mundo"]
    
    def index(self, valor):
        return valor in self.conjunto


valor1 = Conjunto()
print(valor1.index(1))