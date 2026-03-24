import pygame
import sys

# Definição de cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Configuração da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Pong")

class Menu:
    def __init__(self, largura, altura):
        """
        Inicializa o menu com as dimensões da tela.
        """
        self.largura = largura
        self.altura = altura
        self.tela = pygame.display.set_mode((largura, altura))

    def exibir_menu(self):
        """
        Exibe o menu e aguarda a interação do jogador.
        Retorna True quando o jogador pressiona 'ESPAÇO' para iniciar o jogo.
        """
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_SPACE:
                        return True  # Inicia o jogo após pressionar 'ESPAÇO'

            # Preenche a tela com a cor preta
            self.tela.fill(PRETO)

            # Exibe o texto "Pong"
            font = pygame.font.SysFont(None, 50)
            text = font.render("Pong", True, BRANCO)
            text_rect = text.get_rect(center=(self.largura // 2, self.altura // 4 + 50))
            self.tela.blit(text, text_rect)

            # Exibe a instrução para pressionar 'ESPAÇO'
            font_blynk = pygame.font.SysFont(None, 26)
            tempo = pygame.time.get_ticks()
            if tempo % 2000 < 1000:
                text_blynk = font_blynk.render("Pressione ESPAÇO para jogar", True, BRANCO)
                text_blynk_rect = text_blynk.get_rect(center=(self.largura // 2, self.altura // 2 + 60))
                self.tela.blit(text_blynk, text_blynk_rect)

            # Atualiza a tela
            pygame.display.flip()