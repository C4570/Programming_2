def mayor_numero(n):
    if len(n) == 1:
        return n[0]
    else:
        m = mayor_numero(n[1:]) 
        return m if m > n[0] else n[0]
        
print(mayor_numero([1,3,9,2,4570]))

