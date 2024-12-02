class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0

    def aumentar_pontuacao(self):
        self.pontuacao += 1
