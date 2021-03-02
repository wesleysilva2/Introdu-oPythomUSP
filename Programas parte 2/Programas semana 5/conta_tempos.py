import Ordenador_bublesoft # para usar os algoritimos de ordenação criados antes 
import random # para randomizar a lista com valores numericos 
import time # para contar o tempo de ordenação das listas


class ContaTempos:
    def lista_aleatoria(self, n):
        #lista = [0 for x in range(n)] Esse comando gerar uma lista de n elementos com 0 em todas as posições do vetor

        lista = [random.randrange(1000) for x in range(n)] # Vai gerar numeros aleatorios entra 0 e 999 na lista
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara (self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:] # estamos clonando a primeira lista, para a segunda lista

        o = Ordenador_bublesoft.Ordenador()

        print("Comparando com listas aleatorias\n") 
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print("bolha curta demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecão direta demorou ", depois - antes)


        print("\nComparando com listas quarse ordenadas") 
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]

        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print("bolha curta demorou ", depois - antes)

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print("Selecão direta demorou ", depois - antes)
