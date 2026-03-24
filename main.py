import pygame
from game.Menu import Menu
from game.Player import JogadorHumano
from game.Ball import Bola
from config.settings import LARGURA, ALTURA

def inicializar_jogo():
    """
    Função para inicializar os objetos do jogo (jogadores, bola, etc.).
    """
    jogador1 = JogadorHumano(15, ALTURA // 2 - 30, 10, 60)
    jogador2 = JogadorHumano(LARGURA - 25, ALTURA // 2 - 30, 10, 60)
    bola = Bola(LARGURA // 2 - 7, ALTURA // 2 - 7, 7)
    return jogador1, jogador2, bola

def atualizar_placar(score_player1, score_player2):
    """
    Atualiza o placar na tela.
    """
    font_score = pygame.font.SysFont(None, 36)
    score_text = font_score.render(f"{score_player1} - {score_player2}", True, (255, 255, 255))
    return score_text

def main():
    """
    Função principal que inicializa o jogo. Exibe o menu e, quando o jogador pressiona ESPAÇO,
    inicia o jogo com os jogadores e a bola.
    """
    pygame.init()

    # Exibe o menu
    menu = Menu(LARGURA, ALTURA)
    if menu.exibir_menu():  # Quando apertar 'ESPAÇO', o jogo começa
        print("Iniciando o jogo...")  # Debug para garantir que o jogo começou

        jogador1, jogador2, bola = inicializar_jogo()

        # Inicia o loop do jogo
        clock = pygame.time.Clock()  # Controle de FPS
        score_player1 = 0
        score_player2 = 0

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            # Lógica do movimento da bola e dos jogadores
            bola.mover()

            # Movimento dos jogadores
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and jogador1.y > 0:
                jogador1.y -= 5
            if keys[pygame.K_DOWN] and jogador1.y < ALTURA - jogador1.altura:
                jogador1.y += 5

            if jogador2.y + jogador2.altura // 2 < bola.y:
                jogador2.y += 5
            elif jogador2.y + jogador2.altura // 2 > bola.y:
                jogador2.y -= 5

            # Colisões
            if bola.verificar_colisao(jogador1) or bola.verificar_colisao(jogador2):
                bola.velocidade_x = -bola.velocidade_x

            if bola.y <= 0 or bola.y >= ALTURA - bola.tamanho:
                bola.velocidade_y = -bola.velocidade_y

            if bola.x <= 0:
                score_player2 += 1
                bola.resetar()

            if bola.x >= LARGURA - bola.tamanho:
                score_player1 += 1
                bola.resetar()

            # Atualiza a tela
            tela = pygame.display.get_surface()
            tela.fill((0, 0, 0))  # Preencher a tela com a cor preta

            # Desenho dos jogadores e bola
            pygame.draw.rect(tela, (255, 255, 255), (jogador1.x, jogador1.y, jogador1.largura, jogador1.altura))
            pygame.draw.rect(tela, (255, 255, 255), (jogador2.x, jogador2.y, jogador2.largura, jogador2.altura))
            pygame.draw.circle(tela, (255, 255, 255), (bola.x, bola.y), bola.tamanho)

            # Exibe o placar
            score_text = atualizar_placar(score_player1, score_player2)
            tela.blit(score_text, score_text.get_rect(center=(LARGURA // 2, 30)))

            # Atualiza a tela
            pygame.display.flip()
            clock.tick(60)  # Controla o FPS

if __name__ == "__main__":
    main()