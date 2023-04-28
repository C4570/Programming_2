def posicion_de(a,b):
    def helper(a, b, index):
        if a.startswith(b):
            return index
        elif len(a) == 0:
            return -1
        else:
            return helper(a[1:], b, index + 1)
    return helper(a, b, 0)
    
   
x = posicion_de("Un tete a tete con Tete","te")

print(x)