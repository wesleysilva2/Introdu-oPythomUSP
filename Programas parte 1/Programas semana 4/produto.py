
parada = int(input("Digite quantos numeros vc vai digitar:"))
i = 0
produto = 1

valor = 1

while i < parada:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    i = i + 1

print("O produto dos valores e:",produto)