class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.pontuacao = 0

    def aumentar_pontuacao(self):
        """Aumenta a pontuação do jogador"""
        self.pontuacao += 1
