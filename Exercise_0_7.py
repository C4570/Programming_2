def reversaR(list):
    if len(list) == 1:
        return list
    else:
        return list[-1:] + reversaR(list[:-1]) 
    
def reversaI(list):
    list.sort(reverse=True)
    return list

Lista_I = reversaI([1,2,3,4])
Lista_R = reversaR([1,2,3,4])

print("Lista Iteracion: {} \nLista Recursiva: {}".format(Lista_I, Lista_R))