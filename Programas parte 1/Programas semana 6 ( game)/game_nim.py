def usuario_escolhe_jogada(n,m): # 9 e 2 
    tira_u = 0
    tira_u = int(input("\nInforme quanto vai tirar:"))
    while (tira_u <= 0 or tira_u > m):
        print("\nvalor incorreto e muito alto ou menor que 0")
        tira_u = int(input("informe quanto vai tirar:"))
    
    print("\nJogador tirou essa quantidade de peças:",tira_u)
    return tira_u


def computador_escolhe_jogada(n, m):
    tira_c = 1

    while (tira_c != m):
        if ((n - tira_c) % (m + 1) == 0):
            print("\nComputador tirou essa quantidade de peças:",tira_c)
            return tira_c
        else:
            tira_c = tira_c + 1
    
    print("\nComputador tirou essa quantidade de peças:",tira_c)
    return tira_c


def partida():
    n = int(input("\nDigite o numero de peças inicial:"))

    m = int(input("\nDigite o numero maxino de peças que vai poder tirar em uma rodada:"))

    jogador = True
    user = 0 
    cpu = 0

    if (n % (m + 1) == 0):
        print("\nVoce começa")
        user = usuario_escolhe_jogada(n,m)
        n = n - user
        print("\nAgora restam",n,"no tabuleiro")
    
    else:
        print("\nComputador começa")
        cpu = computador_escolhe_jogada(n,m)
        n = n - cpu
        print("\nAgora restam",n,"no tabuleiro")
        jogador = False
    
    
    while (n != 0):
        if (jogador == True):
            cpu = computador_escolhe_jogada(n,m)
            n = n - cpu
            print("\nAgora restam",n,"no tabuleiro")
            if (n == 0):
                print("\nO computador ganhou")
            jogador = False
        else:
            user = usuario_escolhe_jogada(n,m)
            n = n - user
            print("\nAgora restam",n,"no tabuleiro")
            if(n == 0):
                print("\nVoce ganhou")
            else:
                cpu = computador_escolhe_jogada(n,m)
                n = n - cpu
                print("\nAgora restam",n,"no tabuleiro")
                if(n == 0):
                    print("\nO computador ganhou")
                else:
                    jogador = False

def campeonato():
    cont = 1 
    while (cont <= 3):
        print("\n**** Rodada",cont,"****")
        partida()
        cont = cont + 1

    print("\n**** Final do campeonato! ****")
    print("\nPlacar: Você 0 X 3 Computador")    

def jogo():
    valor = int(input("\nBem vindo ao jogo NIM, digite 1 para partida unica e 2 para campeonato:")) 
    if (valor == 1):
        print("\nVoce escolheu partida unica!!!")
        partida()
    if (valor == 2):
        print("\nVoce escolheu campeonato!!!")
        campeonato()
    else:
        print("\nValor incorreto")
            
        



jogo()
