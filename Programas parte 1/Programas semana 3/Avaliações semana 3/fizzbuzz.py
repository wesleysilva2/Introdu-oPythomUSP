valor_test = int(input("Digite um numero a ser testado:"))

if(valor_test % 3 == 0 and valor_test % 5 == 0):
    print("FizzBuzz")

else:
    print(valor_test)