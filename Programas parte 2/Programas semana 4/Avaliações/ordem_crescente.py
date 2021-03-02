def ordena(lista):
        fim = len(lista) 

        for i in range(fim - 1): # ele vai buscando o menor valor
            # Inicialmente, o menor elemento ja visto é o i-esimo
            posicao_do_minimo = i

            for j in range(i+1, fim): # nesse for, depois de pegar o primeiro valor vamos ver se os proximos são menores, por isso i+1 tipo a proxima posição, depois do i
                if lista[j] < lista[posicao_do_minimo]: # Comparando valores o atual e o proximo
                    posicao_do_minimo = j # se ele achar um menor ele substitui

            # Coloca o menor elemento encontrado no inicio da sub-lista
            # Para isso, troca de luga os elementos nas posições i e posicao_do_m   

            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]        

            # se fosse em outras linguagens, ia ter que usar uma variavel auxiliar para trocar os valores
            # em Phyton basta fazer a operação acima para trocar um valor por outro

        return lista
 