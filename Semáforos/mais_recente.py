import pygame
import pygame.mixer
from pygame.locals import *
from sys import exit

pygame.init()

def desenha_tabuleiro(tela):
    while True:
        area_sair_jogo = pygame.Rect(13,665,100,100)
        fundo = pygame.image.load("jogo simples.png")
        tela.blit(fundo, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mouse_pos=pygame.mouse.get_pos()
                if area_sair_jogo.collidepoint(mouse_pos):
                    main()

def escolhaNome(tela):
    fonte = pygame.font.Font(None, 50)
    input_rect = pygame.Rect(470, 470, 435, 100)
    area_sair_escolhaNomes = pygame.Rect(13, 665, 100, 100)
    user1_text = ''
    fundo=pygame.image.load("nome.png")
    while True:
        input_rect= pygame.Rect(470,470,435,100)
        area_sair_escolhaNomes = pygame.Rect(13,665,100,100)
        fundo = pygame.image.load("nome.png")
        tela.blit(fundo, (0,0))
        fonte = pygame.font.Font(None, 50)
        user1_text = ''
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mouse_pos=pygame.mouse.get_pos()
                if area_sair_escolhaNomes.collidepoint(mouse_pos):
                    menu_tipoDeJogo(tela)
                elif input_rect.collidepoint(event.pos):
                    active=True
                else:
                    active=False            
            elif event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(user1_text)
                            user1_text=''
                        elif event.key == pygame.K_BACKSPACE:
                            user1_text = user1_text[:-1]
                        else:
                            user1_text += event.unicode
        pygame.display.flip() """
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    print(user1_text)
                    user1_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    user1_text = user1_text[:-1]
                else:
                    user1_text += event.unicode
        tela.blit(fundo, (0,0))
        pygame.draw.rect(tela, (255, 255, 255), input_rect, 2)
        text_surface = fonte.render(user1_text, True, (0, 0, 0))
        tela.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(435, text_surface.get_width() + 10)

        pygame.draw.rect(tela, (255, 0, 0), area_sair_escolhaNomes)
        pygame.display.update()

        if area_sair_escolhaNomes.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                menu_tipoDeJogo(tela)

        pygame.display.flip()

def area1(tela):
    if matriz[0][0]==0:
        pygame.draw.circle(tela,(0, 255, 0), (60, 63), 40)
        pygame.display.update()
        matriz[0][0]=1
    elif matriz[0][0]==1:
        pygame.draw.circle(tela,(0,0,0),(60,63),40)
        pygame.display.update()
        draw_triangle(tela,(255,255,0),(60,63))
        pygame.display.update()
        matriz[0][0]=2
    elif matriz[0][0]==2:
        draw_triangle(tela,(0,0,0),(60,63))
        rect = pygame.Rect(37.5, 37.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()
        matriz[0][0]=3
def area2(tela):
    if matriz[0][1]==0:
        pygame.draw.circle(tela,(0, 255, 0), (160, 63), 40)
        pygame.display.update()
        matriz[0][1]=1
    elif matriz[0][1]==1:
        pygame.draw.circle(tela,(0,0,0),(160,63),40)
        pygame.display.update()
        draw_triangle(tela,(255,255,0),(160,63))
        pygame.display.update()
        matriz[0][1]=2
    elif matriz[0][1]==2:
        draw_triangle(tela,(0,0,0),(160,63))
        rect = pygame.Rect(137.5, 37.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()
        matriz[0][1]=3
def area3(tela):
    if matriz[0][2]==0:
        pygame.draw.circle(tela,(0, 255, 0), (260, 63), 40)
        pygame.display.update()
        matriz[0][2]=1
    elif matriz[0][2]==1:
        pygame.draw.circle(tela,(0,0,0),(260,63),40)
        pygame.display.update()
        draw_triangle(tela,(255,255,0),(260,63))
        pygame.display.update()
        matriz[0][2]=2
    elif matriz[0][2]==2:
        draw_triangle(tela,(0,0,0),(260,63))
        rect = pygame.Rect(237.5, 37.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()
        matriz[0][2]=3
def area4(tela):
    if matriz[0][3]==0:
        pygame.draw.circle(tela,(0, 255, 0), (360, 63), 40)
        pygame.display.update()
        matriz[0][3]=1
    elif matriz[0][3]==1:
        pygame.draw.circle(tela,(0,0,0),(360,63),40)
        pygame.display.update()
        draw_triangle(tela,(255,255,0),(360,63))
        pygame.display.update()
        matriz[0][3]=2
    elif matriz[0][3]==2:
        draw_triangle(tela,(0,0,0),(360,63))
        rect = pygame.Rect(337.5, 37.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()
        matriz[0][3]=3
def area5(tela):
    if matriz[1][0]==0:
        pygame.draw.circle(tela,(0, 255, 0), (60, 163), 40)
        pygame.display.update()
        matriz[1][0]=1
    elif matriz[1][0]==1:
        pygame.draw.circle(tela,(0,0,0),(60,163),40)
        pygame.display.update()
        draw_triangle(tela,(255,255,0),(60,163))
        pygame.display.update()
        matriz[1][0]=2
    elif matriz[1][0]==2:
        draw_triangle(tela,(0,0,0),(60,163))
        rect = pygame.Rect(37.5, 137.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()
        matriz[1][0]=3
def area6(tela):
    if matriz[1][1]==0:
        pygame.draw.circle(tela,(0, 255, 0), (160, 163), 40)
        pygame.display.update()
        matriz[1][1]=1
    elif matriz[1][1]==1:
        pygame.draw.circle(tela,(0,0,0),(160,163),40)
        pygame.display.update()
        draw_triangle(tela,(255,255,0),(160,163))
        pygame.display.update()
        matriz[1][1]=2
    elif matriz[1][1]==2:
        draw_triangle(tela,(0,0,0),(160,163))
        rect = pygame.Rect(137.5, 137.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()
        matriz[1][1]=3
def area7(tela):
    if matriz[1][2]==0:
        pygame.draw.circle(tela,(0, 255, 0), (260, 163), 40)
        pygame.display.update()
        matriz[1][2]=1
    elif matriz[1][2]==1:
        pygame.draw.circle(tela,(0,0,0),(260,163),40)
        pygame.display.update()
        draw_triangle(tela,(255,255,0),(260,163))
        pygame.display.update()
        matriz[1][2]=2
    elif matriz[1][2]==2:
        draw_triangle(tela,(0,0,0),(260,163))
        rect = pygame.Rect(237.5, 137.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()
        matriz[1][2]=3
def area8(tela):
    if matriz[1][3]==0:
        pygame.draw.circle(tela,(0, 255, 0), (360, 163), 40)
        pygame.display.update()
        matriz[1][3]=1
    elif matriz[1][3]==1:
        pygame.draw.circle(tela,(0,0,0),(360,163),40)
        pygame.display.update()
        draw_triangle(tela,(255,255,0),(360,163))
        pygame.display.update()
        matriz[1][3]=2
    elif matriz[1][3]==2:
        draw_triangle(tela,(0,0,0),(360,163))
        rect = pygame.Rect(337.5, 137.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()
        matriz[1][3]=3
def area9(tela):
    if matriz[2][0]==0:
        pygame.draw.circle(tela,(0, 255, 0), (60, 263), 40)
        pygame.display.update()
        matriz[2][0]=1
    elif matriz[2][0]==1:
        pygame.draw.circle(tela,(0,0,0),(60,263),40)
        pygame.display.update()
        draw_triangle(tela,(255,255,0),(60,263))
        pygame.display.update()
        matriz[2][0]=2
    elif matriz[2][0]==2:
        draw_triangle(tela,(0,0,0),(60,263))
        rect = pygame.Rect(37.5, 237.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()
        matriz[2][0]=3
def area10(tela):
    if matriz[2][1]==0:
        pygame.draw.circle(tela,(0, 255, 0), (160, 263), 40)
        pygame.display.update()
        matriz[2][1]=1
    elif matriz[2][1]==1:
        pygame.draw.circle(tela,(0,0,0),(160,263),40)
        pygame.display.update()
        draw_triangle(tela,(255,255,0),(160,263))
        pygame.display.update()
        matriz[2][1]=2
    elif matriz[2][1]==2:
        draw_triangle(tela,(0,0,0),(160,263))
        rect = pygame.Rect(137.5, 237.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()
        matriz[2][1]=3
def area11(tela):
    if matriz[2][2]==0:
        pygame.draw.circle(tela,(0, 255, 0), (260, 263), 40)
        pygame.display.update()
        matriz[2][2]=1
    elif matriz[2][2]==1:
        pygame.draw.circle(tela,(0,0,0),(260,263),40)
        pygame.display.update()
        draw_triangle(tela,(255,255,0),(260,263))
        pygame.display.update()
        matriz[2][2]=2
    elif matriz[2][2]==2:
        draw_triangle(tela,(0,0,0),(260,263))
        rect = pygame.Rect(237.5, 237.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()
        matriz[2][2]=3
def area12(tela):
    if matriz[2][3]==0:
        pygame.draw.circle(tela,(0, 255, 0), (360, 263), 40)
        pygame.display.update()
        matriz[2][3]=1
    elif matriz[2][3]==1:
        pygame.draw.circle(tela,(0,0,0),(360,263),40)
        pygame.display.update()
        draw_triangle(tela,(255,255,0),(360,263))
        pygame.display.update()
        matriz[2][3]=2
    elif matriz[2][3]==2:
        draw_triangle(tela,(0,0,0),(360,263))
        rect = pygame.Rect(337.5, 237.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()
        matriz[2][3]=3


def jogo(tela):
    while True:
        desenha_tabuleiro(tela)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                if x>16 and x<106 and y>16 and y<106:
                    area1(tela)
                if x>116 and x<206 and y>16 and y<106:
                    area2(tela)
                if x>216 and x<306 and y>16 and y<106:
                    area3(tela)
                if x>316 and x<406 and y>16 and y<106:
                    area4(tela)
                if x>16 and x<106 and y>116 and y<206:
                    area5(tela)
                if x>116 and x<206 and y>116 and y<206:
                    area6(tela)
                if x>216 and x<306 and y>116 and y<206:
                    area7(tela)
                if x>316 and x<406 and y>116 and y<206:
                    area8(tela)
                if x>16 and x<106 and y>216 and y<306:
                    area9(tela)
                if x>116 and x<206 and y>216 and y<306:
                    area10(tela)
                if x>216 and x<306 and y>216 and y<306:
                    area11(tela)
                if x>316 and x<406 and y>216 and y<306:
                    area12(tela)

def menu_regras(tela):
    while True:
        area_sair_regras = pygame.Rect(13, 665, 100, 100)
        fundo = pygame.image.load("REGRAS.png")
        tela.blit(fundo, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mouse_pos=pygame.mouse.get_pos()
                if area_sair_regras.collidepoint(mouse_pos):
                    main()

def menu_tipoDeJogo(tela):
    while True:
        area_sair_escolha_jogadores = pygame.Rect(13,665,100,100)
        area_singleplayer = pygame.Rect(320,434,355,100)
        area_multiplayer = pygame.Rect(720,434,355,100)
        fundo=pygame.image.load("escolher jogadores.png")
        tela.blit(fundo, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mouse_pos=pygame.mouse.get_pos()
                if area_sair_escolha_jogadores.collidepoint(mouse_pos):
                    main()
                elif area_singleplayer.collidepoint(mouse_pos):
                    escolhaNome(tela)
                elif area_multiplayer.collidepoint(mouse_pos):
                    escolhaNomes(tela)

def desenha_menu(tela):
    fundo = pygame.image.load("semaforo menu com peças.png")
    tela.blit(fundo, (0,0))
    pygame.display.update()

def main():
    largura=1366
    altura=768
    tela=pygame.display.set_mode((largura,altura))

    area_novo_jogo = pygame.Rect(177, 265, 300, 100)
    area_continuar_jogo = pygame.Rect(177, 361, 300, 100)
    area_regras = pygame.Rect(177, 496, 300, 100)
    area_sair = pygame.Rect(177, 600, 300, 100)

    matriz=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
    ]

    pygame.mixer.music.load("Magical Sound Shower.mp3")
    pygame.mixer.music.play(-1) 

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