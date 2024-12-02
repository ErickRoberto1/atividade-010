import os
import time
from raquete import Raquete
from bola import Bola
from parede import Parede
from jogador import Jogador

class Jogo:
    def __init__(self, modo="pong"):
        self.largura = 20
        self.altura = 10
        self.modo = modo  # Pode ser 'pong' ou 'breakout'
        
        # Objetos principais
        self.raquete1 = Raquete(0, self.altura // 2 - 1)
        self.raquete2 = Raquete(self.largura - 1, self.altura // 2 - 1)
        self.bola = Bola(self.largura // 2, self.altura // 2)
        self.parede = Parede(0, 0, self.largura, self.altura)

        # Jogadores
        self.jogador1 = Jogador("Jogador 1")
        self.jogador2 = Jogador("Jogador 2")

        # Blocos para o Breakout
        if self.modo == "breakout":
            self.criar_blocos()

    def criar_blocos(self):
        """Cria blocos para o modo Breakout"""
        self.blocos = []
        for i in range(5):
            for j in range(2):
                bloco = Parede(i + 5, j + 2, 1, 1)
                self.blocos.append(bloco)

    def atualizar(self):
        """Atualiza as posições e verifica as colisões"""
        # Movimenta a bola
        self.bola.mover()

        # Verifica colisões com as raquetes
        self.bola.checar_colisao(self.raquete1)
        self.bola.checar_colisao(self.raquete2)

        # Verifica colisões com as paredes
        self.bola.checar_colisao_com_parede(self.parede)

        # Se estiver no modo Breakout, verificar colisões com os blocos
        if self.modo == "breakout":
            self.checar_colisao_com_blocos()

        # Verifica se a bola saiu da tela
        if self.bola.x < 0:
            self.jogador2.aumentar_pontuacao()
            self.bola.resetar()
        elif self.bola.x >= self.largura:
            self.jogador1.aumentar_pontuacao()
            self.bola.resetar()

    def checar_colisao_com_blocos(self):
        """Verifica a colisão da bola com os blocos"""
        for bloco in self.blocos:
            if self.bola.x == bloco.x and self.bola.y == bloco.y:
                self.bola.velocidade_x *= -1
                self.bola.velocidade_y *= -1
                self.blocos.remove(bloco)
                break

    def desenhar(self):
        """Desenha todos os elementos no console"""
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela do console
        
        # Cria uma matriz para representar a tela
        tela = [[' ' for _ in range(self.largura)] for _ in range(self.altura)]

        # Desenha as raquetes
        for y in range(self.raquete1.y, self.raquete1.y + 3):
            if 0 <= y < self.altura:
                tela[y][self.raquete1.x] = '|'
        for y in range(self.raquete2.y, self.raquete2.y + 3):
            if 0 <= y < self.altura:
                tela[y][self.raquete2.x] = '|'

        # Desenha a bola
        if 0 <= self.bola.y < self.altura and 0 <= self.bola.x < self.largura:
            tela[self.bola.y][self.bola.x] = 'O'

        # Desenha os blocos (apenas no modo Breakout)
        if self.modo == "breakout":
            for bloco in self.blocos:
                if 0 <= bloco.y < self.altura and 0 <= bloco.x < self.largura:
                    tela[bloco.y][bloco.x] = '#'

        # Exibe a tela
        for linha in tela:
            print(''.join(linha))

        # Exibe a pontuação
        print(f"Pontuação: {self.jogador1.pontuacao} - {self.jogador2.pontuacao}")

    def rodar(self):
        """Loop principal do jogo"""
        while True:
            self.atualizar()
            self.desenhar()
            time.sleep(0.1)  # Delay para visualização do movimento
