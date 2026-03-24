import pygame
from config.settings import ALTURA

class Jogador:


    def __init__(self, x, y, largura, altura):

        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def mover(self):
  

        raise NotImplementedError("O método 'mover' deve ser implementado pela subclasse.")

    def verificar_colisao(self, bola):
  
        jogador_rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        bola_rect = pygame.Rect(bola.x, bola.y, bola.tamanho, bola.tamanho)
        return jogador_rect.colliderect(bola_rect)

class JogadorHumano(Jogador):


    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)

    def mover(self, direcao):
 
        if direcao == "up" and self.y > 0:
            self.y -= 5
        elif direcao == "down" and self.y < ALTURA - self.altura:
            self.y += 5