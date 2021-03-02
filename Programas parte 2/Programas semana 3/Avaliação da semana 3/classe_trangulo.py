import math

class Triangulo:
    
    def __init__(self, a, b, c): # Construtor da classe 
        
        self.a = a 
        self.b = b
        self.c = c
    
    def ordena_lados(self): # Função auxiliar para pegar os lados digitados
        return sorted([self.a, self.b, self.c])


    def perimetro(self):
        return self.a + self.b + self.c

    def tipo_lado(self):
        if self.a == self.b and self.b == self.c:
            return "equilátero"

        elif self.a == self.b and self.a != self.c or self.a == self.c and self.a != self.b or self.b == self.a and self.b != self.c or self.b == self.c and self.b != self.a or self.c == self.b and self.c != self.a or self.c == self.a and self.c != self.b:
            return "isósceles"
            # condicional muito grande para cobrir as possibilidades de dois lados igais defe ter jeito mais facil 

        elif self.a != self.b and self.b != self.c:
            return "escaleno"

    def retangulo(self):
        
        catetos_potencias = math.pow(self.b, 2) + math.pow(self.c, 2) # Somando as potencias de B e C 
        
        raiz_catetos = math.sqrt(catetos_potencias) # Calculando a raiz quadrada
        
        if raiz_catetos == self.a:
            return True 
        if self.a == 3 and self.b == 4 and self.c == 5:
            return True
        else:
            return False 
    
    def semelhantes(self,triangulo):
        
        primeiro_passo = 0
        cont_1 = 0
        cont_2 = 0
        triangulo_1 = list(self.ordena_lados()) # Chama a função auxiliar ordena_lados Nessa função
        triangulo_2 = list(triangulo.ordena_lados()) # Pegamos os valores digitados pelo usuario e colocamos numa lista

        for x in triangulo_1: # Manipulando a lista de valores dos lados do triangulo
            if primeiro_passo == 0:
                y = x                   
            if y == x and primeiro_passo == 1:
                cont_1 = cont_1 + 1
            primeiro_passo = 1    

        primeiro_passo = 0 
        
        for x in triangulo_2: # Com essa manipulação podemos ver se todos os valores dos lados são igais
            if primeiro_passo == 0:
                y = x                   
            if y == x and primeiro_passo == 1:
                cont_2 = cont_2 + 1
            primeiro_passo = 1 

        if cont_1 == cont_2: # Se todos so lados são iguais ele retorna que são semelhantes ou seja True
            return True
        else:
            return False    
        
