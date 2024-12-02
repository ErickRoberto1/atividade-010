class Bola:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade_x = 1
        self.velocidade_y = 1

    def mover(self):
        """Move a bola de acordo com sua velocidade"""
        self.x += self.velocidade_x
        self.y += self.velocidade_y

    def checar_colisao(self, raquete):
        """Verifica a colisão da bola com a raquete"""
        if self.x == raquete.x and raquete.y <= self.y < raquete.y + 3:
            self.velocidade_x *= -1

    def checar_colisao_com_parede(self, parede):
        """Verifica a colisão da bola com as paredes"""
        if self.y <= 0 or self.y >= parede.altura - 1:
            self.velocidade_y *= -1

    def resetar(self):
        """Reseta a posição da bola"""
        self.x = 10
        self.y = 5
        self.velocidade_x *= -1
        self.velocidade_y *= -1
