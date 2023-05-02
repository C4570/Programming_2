def imprimir_numero(n):
    
    if n == 1:
        print(1)
    else:
        print(n)
        imprimir_numero(n-1)
    
n = input("Ingrese un numero entero: ")

imprimir_numero(int(n))