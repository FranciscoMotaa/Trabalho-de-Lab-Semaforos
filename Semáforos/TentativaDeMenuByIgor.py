import pygame
from pygame.locals import *
from sys import exit

pygame.init()

button_color = (0,0,0,0) # transparente
hover_color = (255,255,255,100) # branco transparente
click_color = (255,255,255,150) # branco transparente

button_surface = pygame.Surface((100, 50))
button_surface.fill(button_color)
button_rect = button_surface.get_rect()
button_rect.center = (300, 200)
fundo_imagem = pygame.image.load('FundoSemaforos.png')
largura=640
altura=480
fonte = pygame.font.Font(None, 50)
tela=pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo do Semáforo')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if button_rect.collidepoint(event.pos):
                button_surface.fill(hover_color)
            else:
                button_surface.fill(button_color)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                button_surface.fill(click_color)
        if event.type == pygame.MOUSEBUTTONUP:
            if button_rect.collidepoint(event.pos):
                button_surface.fill(hover_color)

    tela.blit(fundo_imagem, (0, 0))
    tela.blit(button_surface, button_rect)
