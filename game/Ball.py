import pygame
from config.settings import LARGURA, ALTURA

class Bola:


    def __init__(self, x, y, tamanho):
 
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.velocidade_x = 5
        self.velocidade_y = 5

    def mover(self):
       
        self.x += self.velocidade_x
        self.y += self.velocidade_y

    def verificar_colisao(self, jogador):
       
        bola_rect = pygame.Rect(self.x, self.y, self.tamanho, self.tamanho)
        jogador_rect = pygame.Rect(jogador.x, jogador.y, jogador.largura, jogador.altura)
        return bola_rect.colliderect(jogador_rect)

    def resetar(self):
       
        self.x = LARGURA // 2 - self.tamanho // 2
        self.y = ALTURA // 2 - self.tamanho // 2