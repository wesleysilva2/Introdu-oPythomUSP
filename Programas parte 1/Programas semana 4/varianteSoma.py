
parada = int(input("Digite quantos numeros vc vai digitar:"))
cont = 1
soma = 0

valor = 1

while cont <= parada:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor
    cont = cont + 1

print("soma dos valores e:",soma)