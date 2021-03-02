# Numero de Fibonacci



def fibonacci(numero): # Escreve a serie fibonacci até numero

    primario = 0
    secundario = 1

    while secundario < numero:
        print(secundario, end=" ")
        primario = secundario
        secundario = primario + secundario
    print()


def fib2(n): # retorna a serie fibonacci até numero

    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


if __name__ == "__main__": # se ele for igual a main ele esta sendo executado como escript pelo cmd

    import sys
    fib2(int(sys.argv[1])) # aqui é para pegar o valor que o usuario vai digitar no cmd, tem que transformar em inteiro
    

    # você poderia ter uma inicialização para esse caso especifico caso desejarse.
