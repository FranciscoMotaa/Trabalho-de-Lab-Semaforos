import pygame
import pygame.mixer
from pygame.locals import *
from sys import exit

pygame.init()

def desenha_menu(janela):
    fundo = pygame.image.load("semaforo menu com peças.png")
    janela.blit(fundo, (0,0))
    pygame.display.update()

def menu_regras(janela):
    while True:
        area_sair_regras = pygame.Rect(30, 663, 100, 100)
        imagem_opcao3 = pygame.image.load("REGRAS.png")
        janela.blit(imagem_opcao3, (0,0))
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

def main():
    area_novo_jogo = pygame.Rect(177, 265, 300, 100)
    area_continuar_jogo = pygame.Rect(177, 361, 300, 100)
    area_regras = pygame.Rect(177, 496, 300, 100)
    area_sair = pygame.Rect(177, 600, 300, 100)

    botaonovojogo = pygame.image.load("novo jogo.png")
    botaocontinuarjogo = pygame.image.load("continuar jogo.png")
    botaoregras = pygame.image.load("regras botao.png")
    botaosair = pygame.image.load("sair botao.png")

    largura=1366
    altura=768
    janela=pygame.display.set_mode((largura,altura))
    janela.fill(0xA1CCCC)
    pygame.display.update()


    pygame.mixer.music.load("Magical Sound Shower.mp3")
    pygame.mixer.music.play(-1) #-1 para a música tar a dar sempre 

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            else:
                desenha_menu(janela)
                if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    mouse_pos=pygame.mouse.get_pos()
                    if area_novo_jogo.collidepoint(mouse_pos):
                        print("Entra no jogo")
                    elif area_continuar_jogo.collidepoint(mouse_pos):
                        print("Continuar jogo")
                    elif area_regras.collidepoint(mouse_pos):
                        menu_regras(janela)
                    elif area_sair.collidepoint(mouse_pos):
                        pygame.quit()
                        exit()

        if area_novo_jogo.collidepoint(pygame.mouse.get_pos()):
            janela.blit(botaonovojogo,(167,251))
            pygame.display.update()
        elif area_continuar_jogo.collidepoint(pygame.mouse.get_pos()):
            janela.blit(botaocontinuarjogo,(162,361))
            pygame.display.update()
        elif area_regras.collidepoint(pygame.mouse.get_pos()):
                    janela.blit(botaoregras,(162,490))
                    pygame.display.update()
        elif area_sair.collidepoint(pygame.mouse.get_pos()):
                    janela.blit(botaosair,(162,597))
                    pygame.display.update()            

main()