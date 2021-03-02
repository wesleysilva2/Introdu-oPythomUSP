def fibonacci(n):
    if n < 2: # seria a base da recurção, onde o problema e pequeno
        return n
    else: # aqui ja cai fora da base da recurção

        return fibonacci(n-1) + fibonacci(n-2)