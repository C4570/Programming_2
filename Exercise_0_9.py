def contar_AE(cadena):
        return contar_AE_aux(cadena, 0, 0)
    
def contar_AE_aux(cadena, cont_a, cont_b):
    if len(cadena) == 0:
        return cont_a, cont_b
    else:
        if cadena[0] == "a" or cadena[0] == "A":
            return contar_AE_aux(cadena[1:], cont_a +1, cont_b)
        elif cadena[0] == "e" or cadena[0] == "E":
            return contar_AE_aux(cadena[1:], cont_a, cont_b +1)
        else:
            return contar_AE_aux(cadena[1:], cont_a, cont_b)        


cadena1 = ""
cadena2 = "Lorem ipsum dolor sit amet"
cadena3 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus at mollis massa, ac tristique sem. Nullam tempus gravida blandit. Donec pellentesque vulputate tellus, non venenatis magna. Cras rutrum, quam a volutpat tempus, enim justo tincidunt velit, ac aliquet neque augue ac lorem. Interdum et malesuada fames ac ante ipsum primis in faucibus. Vivamus in aliquet urna. Morbi eget nibh sit amet turpis aliquam varius ut sed ex."

print(contar_AE(cadena3))
