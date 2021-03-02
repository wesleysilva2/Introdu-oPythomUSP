# Se eu pegar 6532 para pegar o ultimo digito x % 10 e para tirar esse numero x //10 

valores_somados = int(input("Digite um numero inteiro:"))

guarda = 0
soma = 0

while valores_somados >= 1: 
    guarda = valores_somados % 10
    valores_somados = valores_somados // 10 
    soma = soma + guarda
    guarda = 0 

print(soma)