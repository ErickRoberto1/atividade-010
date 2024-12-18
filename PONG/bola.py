class Bola:
    def __init__(self, x, y, velocidade_x, velocidade_y):
        self.x = x
        self.y = y
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y

    def mover(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y

    def checar_colisao(self, raquete):
        if self.x == raquete.x and raquete.y <= self.y < raquete.y + 3:
            self.velocidade_x *= -1

    def checar_colisao_com_parede(self, parede):
        if self.y <= 0 or self.y >= parede.altura - 1:
            self.velocidade_y *= -1

    def resetar(self):
        self.x = 10
        self.y = 5
        self.velocidade_x *= -1
        self.velocidade_y *= -1
