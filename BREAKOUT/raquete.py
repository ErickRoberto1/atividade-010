class Raquete:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mover(self, direcao):
        """Move a raquete para cima ou para baixo"""
        if direcao == 'up' and self.y > 0:
            self.y -= 1
        elif direcao == 'down' and self.y < 7:
            self.y += 1

    def desenhar(self, tela):
        """Desenha a raquete"""
        for i in range(3):
            tela[self.y + i][self.x] = '|'
