import pygame
from pygame.locals import *
from sys import exit

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

largura=640
altura=480
fonte = pygame.font.Font(None, 50)
tela=pygame.display.set_mode((largura, altura))

# Define as posições e dimensões dos botões
button_width = 200
button_height = 50
button1_pos = (largura//2 - button_width//2, 100)
button2_pos = (largura//2 - button_width//2, 200)
button3_pos = (largura//2 - button_width//2, 300)

# Cria os textos dos botões
button1_text = fonte.render("Novo Jogo", True, WHITE)
button2_text = fonte.render("Continuar Jogo", True, WHITE)
button3_text = fonte.render("Regras", True, WHITE)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        tela.fill(BLACK)
        pygame.draw.rect(tela, BLACK, (button1_pos[0], button1_pos[1], button_width, button_height))
        pygame.draw.rect(tela, BLACK, (button2_pos[0], button2_pos[1], button_width, button_height))
        pygame.draw.rect(tela, BLACK, (button3_pos[0], button3_pos[1], button_width, button_height))
        tela.blit(button1_text, (button1_pos[0]+10, button1_pos[1]+10))
        tela.blit(button2_text, (button2_pos[0]+10, button2_pos[1]+10))
        tela.blit(button3_text, (button3_pos[0]+10, button3_pos[1]+10))
        pygame.display.update()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.Rect(button1_pos, (button_width, button_height)).collidepoint(mouse_pos):
                #Ação do botao1
            elif pygame.Rect(button2_pos, (button_width, button_height)).collidepoint(mouse_pos):
                #Ação do botao2
            elif pygame.Rect(button3_pos, (button_width, button_height)).collidepoint(mouse_pos):
                #Ação do botao3