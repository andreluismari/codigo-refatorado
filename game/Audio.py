import pygame


def inicializar_audio():
    pygame.mixer.init()


def tocar_musica_fundo():
    pygame.mixer.music.load("assets/sounds/background_music.mp3")  
    pygame.mixer.music.play(loops=-1, fade_ms=1000)  


def tocar_colisao_raquete():
    som_colisao_raquete = pygame.mixer.Sound("assets/sounds/collision_raquete.wav") 
    som_colisao_raquete.play()


def tocar_colisao_borda():
    som_colisao_borda = pygame.mixer.Sound("assets/sounds/collision_borda.wav")  #
    som_colisao_borda.play()


def tocar_gol():
    som_gol = pygame.mixer.Sound("assets/sounds/gol.wav")  
    som_gol.play()