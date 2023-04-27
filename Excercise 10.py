def potencia(b,n):
    if n == 0:
        return 1
    elif n > 0:
        return b * potencia(b, n-1)
    else:
        return float(1 / b * potencia(b, n+1))

def potencia_aux(b,n):
    if b == 1 or b == 0 or n == 1:
        return b
    else:
        potencia(b,n)

print(potencia(2,-4))
