import os
import time
from raquete import Raquete
from bola import Bola
from parede import Parede
from jogador import Jogador

class Jogo:
    def __init__(self):
        self.largura = 20
        self.altura = 10
        self.vel_x_bola = 5
        self.vel_y_bola = 5

        # Objetos principais
        self.raquete1 = Raquete(0, self.altura // 2 - 1)
        self.bola = Bola(self.largura // 2, self.altura // 2,self.vel_x_bola,self.vel_y_bola)
        self.parede = Parede(0, 0, self.largura, self.altura)

        # Jogadores
        self.jogador1 = Jogador("Jogador 1")

        # Blocos para o Breakout
        self.blocos = []



    def criar_blocos(self):
        """Cria blocos para o modo Breakout"""
        for i in range(5):
            for j in range(2):
                bloco = Parede(i + 5, j + 2, 1, 1)
                self.blocos.append(bloco)

    def checar_colisao(self, raquete):
        """Verifica a colisão da bola com a raquete"""
        if self.bola.x == self.raquete1.x and self.bola.y == self.raquete1.y :
            self.vel_x_bola *= -1

    def checar_colisao_com_parede(self, parede):
        """Verifica a colisão da bola com as paredes"""
        if self.y <= 0 or self.y >= parede.altura - 1:
            self.velocidade_y *= -1
        else:
            vel_x_bola = 5
            vel_y_bola = 5

    def atualizar(self):
        """Atualiza as posições e verifica as colisões"""
        # Movimenta a bola
        self.bola.mover()

        # Verifica colisões com as raquetes
        self.checar_colisao(self.raquete1)

        # Verifica colisões com as paredes
        self.checar_colisao_com_parede(self.parede)

        # Se estiver no modo Breakout, verificar colisões com os blocos
        self.checar_colisao_com_blocos()


    def checar_colisao_com_blocos(self):
        """Verifica a colisão da bola com os blocos"""
        for bloco in self.blocos:
            if self.bola.x == bloco.x and self.bola.y == bloco.y:
                self.bola.velocidade_x *= -1
                self.bola.velocidade_y *= -1
                self.blocos.remove(bloco)
                break

    def desenhar(self) :
        """Atualiza apenas os valores no terminal"""
        # Limpa a tela novamente para atualizar a interface
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela

        # Desenha a estrutura fixa
        print("###########################################################")
        print("# Jogo de Pong (em modo console)                 #")
        print("###########################################################")

        # Atualiza as coordenadas da bola
        print(f"Bola - Posição: (x = {self.bola.x}, y = {self.bola.y})")

        # Atualiza as posições das raquetes
        print(f"Raquete 1 - Posição: (x = {self.raquete1.x}, y = {self.raquete1.y})")

        # Exibe a pontuação
        print(f"Pontuação: {self.jogador1.pontuacao}")

        print("###########################################################")


    def rodar(self) :
        """Loop principal do jogo"""
        while True :
            self.criar_blocos()
            self.atualizar()
            self.desenhar()
            time.sleep(1.5)  # Delay para visualização do movimento


