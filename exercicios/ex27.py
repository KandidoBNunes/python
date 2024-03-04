import pygame
pygame.init()
pygame.mixer.music.load('caminho_para_o_seu_arquivo.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
