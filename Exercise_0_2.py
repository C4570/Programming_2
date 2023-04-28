def numero_triangular(n):
    if n == 1:
        return 1
    else:
        return n + numero_triangular(n-1)

print(numero_triangular(5))