import pygame
from pygame.locals import *
from sys import exit
pygame.init()

# Carregar a imagem
def menu (janela):
    fundo = pygame.image.load("semaforo menu com peças.png")
    imagem_opcao3 = pygame.image.load("REGRAS1.png")
    janela.blit(fundo, (0,0))
    #criar botões
    area_novo_jogo = pygame.Rect(177, 265, 300, 100)
    area_continuar_jogo = pygame.Rect(177, 361, 300, 100)
    area_regras = pygame.Rect(177, 496, 300, 100)
    area_sair_regras = pygame.Rect(30, 663, 100, 100)
    area_sair = pygame.Rect(177, 600, 300, 100)


    if events.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            #if area_novo_jogo.collidepoint(mouse_pos):
                # Lógica para a opção "Novo Jogo"
                #janela.blit(imagem_opcao1, (0, 0))
            #elif area_continuar_jogo.collidepoint(mouse_pos):
                # Lógica para a opção "Continuar Jogo"
                #janela.blit(imagem_opcao2, (0, 0))
            if area_regras.collidepoint(mouse_pos):
                # Lógica para a opção "Regras"
                janela.blit(imagem_opcao3, (0, 0))
                area_sair_regras = pygame.Rect(40, 663, 100, 100)
                if events.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if area_sair_regras.collidepoint(mouse_pos):
                       janela.blit(fundo, (0,0))
            elif area_sair.collidepoint(mouse_pos):

# Criar a janela
janela = pygame.display.set_mode([1366,768])
pygame.display.set_caption("Semáforo")
                    
while True:
    menu()
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit()
        """ elif events.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            #if area_novo_jogo.collidepoint(mouse_pos):
                # Lógica para a opção "Novo Jogo"
                #janela.blit(imagem_opcao1, (0, 0))
            #elif area_continuar_jogo.collidepoint(mouse_pos):
                # Lógica para a opção "Continuar Jogo"
                #janela.blit(imagem_opcao2, (0, 0))
            if area_regras.collidepoint(mouse_pos):
                # Lógica para a opção "Regras"
                janela.blit(imagem_opcao3, (0, 0))
                area_sair_regras = pygame.Rect(40, 663, 100, 100)
                if events.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if area_sair_regras.collidepoint(mouse_pos):
                       janela.blit(fundo, (0,0))
                       continue
            elif area_sair.collidepoint(mouse_pos):
                loop = False """
            

    pygame.display.update()


