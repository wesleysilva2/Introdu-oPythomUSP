def encontra_impares(lista):
    
    lista_2 = []
    
    #if len(lista) <= 1: # Base da recurcao
        #if lista[0] % 2 != 0:
           # return lista[0]
    #else:
    if len(lista) > 0:
        valor = lista.pop(0)
            
        if valor % 2 != 0:
            lista_2.append(valor)
                
        lista_2 = lista_2 + encontra_impares(lista) # Recursao completa

    # Retorna a lista final:
    return lista_2
        
               
            

    
