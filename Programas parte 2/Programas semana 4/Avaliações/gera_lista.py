def lista_grande(tamanho_da_lista):

        lista = []
        valores_aleatorios_lista = tamanho_da_lista + 100
        cont = tamanho_da_lista

        while cont != 0:
            if valores_aleatorios_lista % 2 == 0 or valores_aleatorios_lista % 3 == 0:
               valores_aleatorios_lista = valores_aleatorios_lista - 3
               lista.append(valores_aleatorios_lista)
            else:
               valores_aleatorios_lista = valores_aleatorios_lista + 11 
               lista.append(valores_aleatorios_lista)
            cont = cont - 1
        
        return lista
