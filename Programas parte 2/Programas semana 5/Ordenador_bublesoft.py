class Ordenador: # classe 
    def selecao_direta(self,lista): # metodo que recebe lista como parametro
        #lista = self.cria_lista()
        fim = len(lista) # guardo o comprimento da lista, quantos valores tem

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

            

        
    def bolha(self,lista):
        fim = len(lista)
        #Esse for começa na ultima posição do vetor, vai percorrer até a primeira posição, a zero, e o passo é de menos 1 a menos 1. 

        for i in range(fim-1, 0, -1):
            for j in range(i):# for para percorrer o vetor fazendo as trocas dos mais leves pelos mais pesados, o range i e por que eu quero desde a posição do j ate a posição do i-1, ou seja a posição atual
                if lista[j] > lista[j + 1]: # se for verdade quer dizer que esta na ordem inversa 
                    lista[j], lista[j+1] = lista[j+1], lista[j] # Trocando os elementos para ordenar


    def bolha_curta(self,lista):
        fim = len(lista)
        
        for i in range(fim-1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j + 1]: # se for verdade quer dizer que esta na ordem inversa 
                    lista[j], lista[j+1] = lista[j+1], lista[j] # Trocando o                
                    trocou = True

        if trocou == False: # Se não trocou quer dizer que a lista ja esta ordenada, isso deixa o algoritmo mais eficiente
            return
            
