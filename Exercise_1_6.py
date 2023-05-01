import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
    
    def __str__(self):
        return f"{self.valor} de {self.palo}"
    
    def __eq__(self, other):
        return self.valor == other.valor and self.palo == other.palo
    
class Mazo:
    def __init__(self):
        self.cartas = []
        
        palos = ["oros", "copas", "bastos", "espadas"]
        valores = ["as", "1", "2", "3", "4", "5", "6", "7", "8", "9", "sota", "caballo", "rey"]
        
        for palo in palos:
            for valor in valores:
                self.cartas.append(Carta(valor, palo))
        
        comodin1 = Carta("j", "comodin")
        comodin2 = Carta("j", "comodin")

        self.cartas.append(comodin1)
        self.cartas.append(comodin2)
    
    def contar_cartas(self):
        return len(self.cartas)

    def mezclar(self):
        random.shuffle(self.cartas)
    
    def __str__(self):
        print("Las cartas del mazo son:")
        for carta in self.cartas:
            print(carta)

mazo = Mazo()

mazo.__str__()

print("\n--------------------")
mazo. mezclar()
print("--------------------\n")

mazo.__str__()