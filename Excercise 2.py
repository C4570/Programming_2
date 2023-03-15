def numero_triangular(n):
    
    if n == 1:
        return 1
    else:
        return n + numero_triangular(n-1)

n = input("Ingrese un numero entero: ")

print(numero_triangular(int(n)))