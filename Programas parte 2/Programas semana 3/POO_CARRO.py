def main(): # teste com a classe 

    carro1 = Carro('brasilia', 1968, 'amarela', 80) # aqui estamos criando umas intancias ou objetos
    carro2 = Carro('fuscão', 1981, 'preto', 95)

    carro1.acelere(40) # aqui estamos chamando os metodos
    carro2.acelere(50)
    carro1.acelere(80)
    carro1.pare()
    carro2.acelere(100)


class Carro: # definição da classe carro 

    def __init__(self, nome, ano, cor, velocidade): # metodo construtor sempre começa com self
        self.modelo = nome
        self.ano    = ano
        self.cor    = cor
        self.vel    = 0 # todo carro quando e criado começa com velocidade zero
        self.maxV   = velocidade # velocidade maxima


    def imprima(self): # metodo imprima 
        if self.vel == 0: # quando queremos nos referir ao objeto, usamos self
            print("%s %s %d"%(self.modelo, self.cor, self.ano)   )
            
        elif self.vel < self.maxV:
            print(" %s %s indo a %d Km/h"%(self.modelo, self.cor, self.vel)) 
        else:
            print("%s %s indo muito rapido !!!!!" %(self.modelo, self.cor))

    def acelere(self, velocidade): # metodo acerela 
        self.vel = velocidade
        if self.vel > self.maxV: # se alguém colocar uma velocidade maior que a maxima
            self.vel = self.maxV # ele iguala o valor da velocidade a maxima
        self.imprima()

    def pare(self): # metodo pare 
        self.vel = 0 # coloca zero na velocidade
        self.imprima()

main() # para executar a função main para fazer um teste com as classess
