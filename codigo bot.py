import random 
import pygame 
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("IA no Pygame")
clock = pygame.time.Clock()

class AI:
    def __init__(self):
        self.x = 490
        self.y = 282
        self.speed = 6
        self.image = pygame.image.load("bola.png") 
        self.image2 = pygame.image.load("quadrado.png")
        #matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]

    def update(self):
        botao_00 = pygame.Rect(490, 282, 110, 110)
        botao_01 = pygame.Rect(603, 282, 110, 110)
        botao_02 = pygame.Rect(718, 282, 110, 110)
        botao_03 = pygame.Rect(831, 282, 110, 110)
        botao_10 = pygame.Rect(490, 400, 110, 110)
        botao_11 = pygame.Rect(603, 400, 110, 110)
        botao_12 = pygame.Rect(718, 400, 110, 110)
        botao_13 = pygame.Rect(831, 400, 110, 110)
        botao_20 = pygame.Rect(490, 518, 110, 110)
        botao_21 = pygame.Rect(603, 518, 110, 110)
        botao_22 = pygame.Rect(718, 518, 110, 110)
        botao_23 = pygame.Rect(831, 518, 110, 110)
        
        posicoes = [botao_00, botao_01, botao_02, botao_03, botao_10, botao_11, botao_12, botao_13, botao_20, botao_21, botao_22, botao_23]
        x = random.choice(posicoes)
        screen.blit(self.image, (x[0] - self.image.get_width() // 2, x[1] - self.image.get_height() // 2))
        screen.blit(self.image2, (x[0] - self.image2.get_width() // 2, x[1] - self.image2.get_height() // 2))
        #pygame.draw.circle(screen, (0,255,0), x, 20)

    def render(self):
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 20)

ai = AI()

running = True

tabuleiro = pygame.image.load("vez do jogador.png")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(tabuleiro, (0,0))
    pygame.display.update()
    ai.update()
    ai.render()

    pygame.display.update()
    clock.tick(50)

pygame.quit()

#matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]



