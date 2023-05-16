import pygame
from pygame.locals import *
from sys import exit

pygame.init()



largura=1366
altura=768
fonte = pygame.font.Font(None, 30)
tela=pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo do Semáforo')
while True:
    area_sair_escolha_jogadores = pygame.Rect(13,665,100,100)
    fundo=pygame.image.load("escolher jogadores.png")
    tela.blit(fundo, (0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = pygame.mouse.get_pos()
            print("x=",x,"y=",y)
            texto = fonte.render(f'x: {x}, y: {y}', True, (255, 0, 0))
            tela.blit(texto, (x + 10, y))
            pygame.display.update()