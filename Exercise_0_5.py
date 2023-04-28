def es_potencia(n, b):
    if n == b:
        return True
    elif n < b:
        return False
    else:
        return es_potencia(n/b, b)
    
print(es_potencia(16,2))