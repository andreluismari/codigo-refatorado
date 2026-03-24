import pygame
from config.settings import LARGURA, ALTURA

class Bola:
    """
    Classe responsável pela bola no jogo Pong. Controla a movimentação e colisões.

    Atributos:
        x (int): Posição inicial no eixo X.
        y (int): Posição inicial no eixo Y.
        tamanho (int): Tamanho da bola.
        velocidade_x (int): Velocidade da bola no eixo X.
        velocidade_y (int): Velocidade da bola no eixo Y.
    """

    def __init__(self, x, y, tamanho):
        """
        Inicializa a bola com a posição e o tamanho.

        Parâmetros:
            x (int): Posição inicial no eixo X.
            y (int): Posição inicial no eixo Y.
            tamanho (int): Tamanho da bola.
        """
        self.x = x
        self.y = y
        self.tamanho = tamanho
        self.velocidade_x = 5
        self.velocidade_y = 5

    def mover(self):
        """
        Atualiza a posição da bola.
        """
        self.x += self.velocidade_x
        self.y += self.velocidade_y

    def verificar_colisao(self, jogador):
        """
        Verifica se a bola colidiu com o jogador.

        Parâmetro:
            jogador (Jogador): O jogador com quem a bola pode colidir.

        Retorna:
            bool: Verdadeiro se houve colisão.
        """
        bola_rect = pygame.Rect(self.x, self.y, self.tamanho, self.tamanho)
        jogador_rect = pygame.Rect(jogador.x, jogador.y, jogador.largura, jogador.altura)
        return bola_rect.colliderect(jogador_rect)

    def resetar(self):
        """
        Reseta a posição da bola para o centro da tela.
        """
        self.x = LARGURA // 2 - self.tamanho // 2
        self.y = ALTURA // 2 - self.tamanho // 2