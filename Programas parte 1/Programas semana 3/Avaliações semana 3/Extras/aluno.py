aluno = int(input("Digite o numero de alunos:"))
cont = 0 

while cont < aluno: 
    nota = float(input("Digite a nota:"))
                 
    if (nota >=3 and nota <=5):
        print("Esta em recuperação")
        cont = cont + 1
    else:
        if(nota < 3):
            print("Esta Reprovado")
            cont = cont + 1
        else:
            print("Aluno esta Aprovado")
            cont = cont + 1
        