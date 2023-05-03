'''
TAD - Inmutable

__init__

'''

class Nodo:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next
        
    def __str__(self) -> str:
        return f'Cargo: {self.cargo}'
