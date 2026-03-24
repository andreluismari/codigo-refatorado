import pygame
from config.settings import ALTURA

class Jogador:
    """
    Classe base para um jogador no jogo Pong. Define a posição e os métodos básicos.

    Atributos:
        x (int): Posição inicial no eixo X.
        y (int): Posição inicial no eixo Y.
        largura (int): Largura da raquete.
        altura (int): Altura da raquete.
    """

    def __init__(self, x, y, largura, altura):
        """
        Inicializa o jogador com a posição e dimensões.

        Parâmetros:
            x (int): Posição inicial no eixo X.
            y (int): Posição inicial no eixo Y.
            largura (int): Largura da raquete.
            altura (int): Altura da raquete.
        """
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def mover(self):
        """
        Método de movimento que deve ser implementado nas subclasses.
        """
        raise NotImplementedError("O método 'mover' deve ser implementado pela subclasse.")

    def verificar_colisao(self, bola):
        """
        Verifica se a raquete colidiu com a bola.

        Parâmetro:
            bola (Bola): O objeto da bola a ser verificado.

        Retorna:
            bool: Verdadeiro se houver colisão.
        """
        jogador_rect = pygame.Rect(self.x, self.y, self.largura, self.altura)
        bola_rect = pygame.Rect(bola.x, bola.y, bola.tamanho, bola.tamanho)
        return jogador_rect.colliderect(bola_rect)

class JogadorHumano(Jogador):
    """
    Classe para o jogador humano. Permite mover a raquete para cima e para baixo.
    """

    def __init__(self, x, y, largura, altura):
        super().__init__(x, y, largura, altura)

    def mover(self, direcao):
        """
        Mover o jogador com base na direção dada.

        Parâmetro:
            direcao (str): A direção de movimento, pode ser 'up' ou 'down'.
        """
        if direcao == "up" and self.y > 0:
            self.y -= 5
        elif direcao == "down" and self.y < ALTURA - self.altura:
            self.y += 5