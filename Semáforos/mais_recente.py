import pygame
from pygame.locals import *
from sys import exit

pygame.init()

def desenha_menu(tela):
    fundo = pygame.image.load("semaforo menu com peças.png")
    tela.blit(fundo, (0,0))
    pygame.display.update()

def menu_regras(tela):
    while True:
        area_sair_regras = pygame.Rect(13, 665, 100, 100)
        imagem_opcao3 = pygame.image.load("REGRAS1.png")
        tela.blit(imagem_opcao3, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            else:
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    mouse_pos=pygame.mouse.get_pos()
                    if area_sair_regras.collidepoint(mouse_pos):
                        main()

def menu_tipoDeJogo(tela):
    while True:
        area_sair_escolha_jogadores = pygame.Rect(13,665,100,100)
        fundo=pygame.image.load("escolher jogadores.png")
        tela.blit(fundo, (0,0))
        pygame.display.update()

def main():
    area_novo_jogo = pygame.Rect(177, 265, 300, 100)
    area_continuar_jogo = pygame.Rect(177, 361, 300, 100)
    area_regras = pygame.Rect(177, 496, 300, 100)
    area_sair = pygame.Rect(177, 600, 300, 100)

    largura=1366
    altura=768
    tela=pygame.display.set_mode((largura,altura))
    while True:
        desenha_menu(tela)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mouse_pos=pygame.mouse.get_pos()
                if area_novo_jogo.collidepoint(mouse_pos):
                    menu_tipoDeJogo(tela)
                elif area_continuar_jogo.collidepoint(mouse_pos):
                    print("Continuar jogo")
                elif area_regras.collidepoint(mouse_pos):
                    menu_regras(tela)
                elif area_sair.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()

main()