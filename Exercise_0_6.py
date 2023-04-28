def replica(list,n):
    if n == 1 or 0:
        return list
    else:
        return list + replica(list, n-1)
    
lista = replica([1,2,3],3)
lista.sort()
print(lista)