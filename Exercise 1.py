def mi_funcion(n):
    
    if n == 1:
        return print(n)
    
    print(n)
    n = n - 1
       
    mi_funcion(n)
    return n

n = input("Ingrese un numero entero: ")

mi_funcion(int(n))