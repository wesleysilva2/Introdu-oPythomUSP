def fatorial(n):
    if n < 1: # seria a base da recurção, onde o problema e pequeno
        return 1
    else: # aqui ja cai fora da base da recurção

        return n * fatorial(n-1)