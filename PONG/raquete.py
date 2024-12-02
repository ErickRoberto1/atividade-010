class Raquete:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, direcao):
        if direcao == 'w' and self.y > 0:
            self.y -= 1
        elif direcao == 's' and self.y < 7:
            self.y += 1

