
class Bola:
    def __init__(self, x, y,velocidade_x,velocidade_y):
        self.x = x
        self.y = y
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
        self.jogo = Jogo

    def mover(self):
        """Move a bola de acordo com sua velocidade"""
        self.x += self.velocidade_x
        self.y += self.velocidade_y

    def resetar(self):
        """Reseta a posição da bola"""
        self.x = 10
        self.y = 5
        self.velocidade_x *= -1
        self.velocidade_y *= -1
