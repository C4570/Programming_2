def impriir_numero(n, cont= 1):
    if n < 10:
        return cont
    else:
        return impriir_numero(n/10, cont+1)
    
print(impriir_numero(0))