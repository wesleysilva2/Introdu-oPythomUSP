class Musica:
    def __init__(self, titulo, interprete, compositor, ano): # Metodo q vai gerar um objeto
        self.titulo = titulo
        self.interprete = interprete
        self.compositor = compositor
        self.ano = ano


class Buscador: # Classe 
    def busca_por_titulo(self, playlist, titulo):
        for i in range(len(playlist)):
            if playlist[i].titulo == titulo: # se o titulo da musica que esta no indice i for igual a x, que e o que foi passado como parametro
                return i
        return -1

    def vamos_buscar(self): # metodo 

        playlist = [ Musica("Ponta de areia", "Milton Nacimento", "Milton Nacimento", 1975), # Objetos sendo criados
                     Musica("Sozinho", "Caetano Veloso", "Caetano Veloso", 1984), # e esses são seus atributos
                     Musica("is this love", "Bob Marley", "Bob Marley", 1992),
                     Musica("Le Festin", "Caroline Dion", "Caroline Dion", 2005)]
        onde_achou = self.busca_por_titulo(playlist, "Le festin")

        if onde_achou == -1:
            print("Minha musica preferida não esta na playlist")
        else:
            preferida = playlist[onde_achou]
            print(preferida.titulo, preferida.interprete, preferida.compositor, preferida.ano,
            sep = ', ');      
