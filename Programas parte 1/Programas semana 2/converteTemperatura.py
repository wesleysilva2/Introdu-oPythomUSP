Fahrenheit = input("Digite uma temperatura em Fahrenheit: ")

auxiliar = float(Fahrenheit) # Converte o valor digitado pelo usuario em float, para poder entrar na formular

Celsius = (auxiliar - 32) * 5 / 9 # formula de conversão de Fahrenheit para Celsius

print("A temperatura em celsius é ",Celsius)