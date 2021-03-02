# ele coloca o primeiro elemento numa lista, ai ele vai comparando os outros elementos
# da primeira lista com o elemento adicionado a pouco, se for maior ele bota na frente, se for 
# menor ele passa o primeiro elemento para frente e coloca o elmento menor que ele atras, assim ordenando a lista.


def insertion_sort(lista):
    tamanho_lista = len(lista)
    for x in range(1, tamanho_lista): # pega a partir da segunda posição 1, por que o primeiro vai para nova lista que so com ele ja esta ordenada 
        elemento_corrente = lista[x] # pegando o valor da vez na lista 
        j = x - 1 # para ver o elemento anterior, na primeira interação começa como 0
        
        while j >= 0 and lista[j] > elemento_corrente:
            lista[j+1] = lista[j] # se precisar avança uma posição
            j = j - 1
        lista[j+1] = elemento_corrente # precisa do j + 1 pq vc vai terminar uma posição antes de onde precisa inserir

    return lista   
