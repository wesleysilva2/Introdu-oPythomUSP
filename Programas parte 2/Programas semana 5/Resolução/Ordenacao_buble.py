def bubble_sort(lista):
    fim = len(lista)
        #Esse for começa na ultima posição do vetor, vai percorrer até a primeira posição, a zero, e o passo é de menos 1 a menos 1. 

    for i in range(fim-1, 0, -1):
        for j in range(i):# for para percorrer o vetor fazendo as trocas dos mais leves pelos mais pesados, o range i e por que eu quero desde a posição do j ate a posição do i-1, ou seja a posição atual
            if lista[j] > lista[j + 1]: # se for verdade quer dizer que esta na ordem inversa 
                lista[j], lista[j+1] = lista[j+1], lista[j] # Trocando os elementos para ordenar
                print(lista)
    return lista