class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo
    
    def __str__(self):
        return f"{self.valor} de {self.palo}"
    
    def __eq__(self, other):
        return self.valor == other.valor and self.palo == other.palo
    
as_espadas = Carta("1", "espada")
tres_copas = Carta("3", "copas")

print(as_espadas == tres_copas)
print(tres_copas == tres_copas)