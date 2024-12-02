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

        self.raquete1 = Raquete(0, self.altura // 2 - 1)
        self.raquete2 = Raquete(self.largura - 1, self.altura // 2 - 1)
        self.bola = Bola(self.largura // 2, self.altura // 2, 2, 1)
        self.parede = Parede(0, 0, self.largura, self.altura)


        self.jogador1 = Jogador("Jogador 1")
        self.jogador2 = Jogador("Jogador 2")


    def atualizar(self):
        
        self.bola.mover()
        self.raquete1.mover(input('tecla: ').lower())

        self.bola.checar_colisao(self.raquete1)
        self.bola.checar_colisao(self.raquete2)

        self.bola.checar_colisao_com_parede(self.parede)

        if self.bola.x < 0:
            self.jogador2.aumentar_pontuacao()
            self.bola.resetar()
        elif self.bola.x >= self.largura:
            self.jogador1.aumentar_pontuacao()
            self.bola.resetar()
    def desenhar_inicio(self):

        os.system('cls')
        print("###########################################################")
        print("# Jogo de Pong (em modo console)                          #")
        print("###########################################################")
        print("Bola - Posição: (x, y)                                  ")
        print("Raquete 1 - Posição: (x, y)                              ")
        print("Raquete 2 - Posição: (x, y)                              ")
        print("Pontuação: 0 - 0                                         ")
        print("###########################################################")

    def desenhar(self):

        os.system('cls') 
        print("###########################################################")
        print("# Jogo de Pong (em modo console)                          #")
        print("###########################################################")
        
        # coordenadas da bola
        print(f"Bola - Posição: (x = {self.bola.x:.2f}, y = {self.bola.y})")

        # coordenadas das raquetes
        print(f"Raquete 1 - Posição: (x = {self.raquete1.x}, y = {self.raquete1.y})")
        print(f"Raquete 2 - Posição: (x = {self.raquete2.x}, y = {self.raquete2.y})")

        # pontuação
        print(f"Pontuação: {self.jogador1.pontuacao} - {self.jogador2.pontuacao}")

        print("###########################################################")

    def rodar(self):
        while True:
            self.atualizar()
            self.desenhar()
            time.sleep(1.5)

