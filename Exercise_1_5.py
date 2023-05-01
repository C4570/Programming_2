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
    
    def contar_cartas(self):
        return len(self.cartas)

mazo = Mazo()
numero_de_cartas = mazo.contar_cartas()

print(f"El mazo tiene {numero_de_cartas} cartas.")