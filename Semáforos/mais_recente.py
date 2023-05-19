import pygame
import pygame.mixer
from pygame.locals import *
from sys import exit

pygame.init()


def carrega_nomes():
    with open("nomes.txt", "r") as ficheiro_nomes:
        conteudo = ficheiro_nomes.read()
        nomes = conteudo.split()
    return nomes

def guarda_nomes(nome1, nome2):
    ficheiro_nomes = open("nomes.txt", "w")
    ficheiro_nomes.write("")
    ficheiro_nomes.write(str(nome1) + " " + str(nome2))
    ficheiro_nomes.close()

def carrega_matriz():
    with open("matriz.txt", "r") as ficheiro_matriz:
        conteudo = ficheiro_matriz.read()
        matriz = eval(conteudo)
    return matriz

def guarda_matriz(matriz):
    ficheiro_matriz = open("matriz.txt", "w")
    ficheiro_matriz.write("")
    ficheiro_matriz.write(str(matriz))
    ficheiro_matriz.close()

def desenha_tabuleiro_singleplayer(tela, matriz, nome, tipo_de_jogo):
    while True:
        area_sair_jogo = pygame.Rect(13,665,100,100)
        area_regras_ingame = pygame.Rect(113,665,100,100)
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
                    guarda_nomes(nome)
                    guarda_matriz(matriz)
                    guarda_tipo_de_jogo(tipo_de_jogo)
                    main(matriz, nome)
                if area_regras_ingame.collidepoint(mouse_pos):
                    menu_regras_ingame_singleplayer(tela, matriz, nome)
            else:
                area1_carregar(tela,matriz)
                area2_carregar(tela,matriz)
                area3_carregar(tela,matriz)
                area4_carregar(tela,matriz)
                area5_carregar(tela,matriz)
                area6_carregar(tela,matriz)
                area7_carregar(tela,matriz)
                area8_carregar(tela,matriz)
                area9_carregar(tela,matriz)
                area10_carregar(tela,matriz)
                area11_carregar(tela,matriz)
                area12_carregar(tela,matriz)
                jogo_singleplayer(tela, matriz, nome)

def desenha_tabuleiro_multiplayer(tela, matriz, nome1, nome2, tipo_de_jogo):
    while True:
        area_sair_jogo = pygame.Rect(13,665,100,100)
        area_regras_ingame = pygame.Rect(113,665,100,100)
        fundo = pygame.image.load("vez do jogador.png")
        tela.blit(fundo, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mouse_pos=pygame.mouse.get_pos()
                if area_sair_jogo.collidepoint(mouse_pos):
                    guarda_nomes(nome1, nome2)
                    guarda_matriz(matriz)
                    guarda_tipo_de_jogo(tipo_de_jogo)
                    main(matriz, nome1, nome2)
                if area_regras_ingame.collidepoint(mouse_pos):
                    menu_regras_ingame_multiplayer(tela, matriz, nome1, nome2)
            else:
                area1_carregar(tela,matriz)
                area2_carregar(tela,matriz)
                area3_carregar(tela,matriz)
                area4_carregar(tela,matriz)
                area5_carregar(tela,matriz)
                area6_carregar(tela,matriz)
                area7_carregar(tela,matriz)
                area8_carregar(tela,matriz)
                area9_carregar(tela,matriz)
                area10_carregar(tela,matriz)
                area11_carregar(tela,matriz)
                area12_carregar(tela,matriz)
                jogo_multiplayer(tela, matriz, nome1, nome2)

def escolhaNome1(tela, matriz, tipo_de_jogo):
    fonte = pygame.font.Font(None, 50)
    input_rect = pygame.Rect(470, 470, 435, 100)
    area_sair_escolhaNomes = pygame.Rect(13, 665, 100, 100)
    user_text = ''
    fundo1=pygame.image.load("nome jogador 1.png")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    nome1=user_text
                    escolhaNome2(tela, matriz, nome1, tipo_de_jogo)
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode    
        tela.blit(fundo1, (0,0))
        text_surface = fonte.render(user_text, True, (0, 0, 0)) 
        tela.blit(text_surface, (input_rect.x + 130, input_rect.y + 30))
        input_rect.w = max(435, text_surface.get_width() + 10) 
        pygame.display.update()
        if area_sair_escolhaNomes.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                menu_tipoDeJogo(tela, matriz)
        pygame.display.update()
    
def escolhaNome2(tela, matriz, nome1, tipo_de_jogo):
    fonte = pygame.font.Font(None, 50)
    input_rect = pygame.Rect(470, 470, 435, 100)
    area_sair_escolhaNomes = pygame.Rect(13, 665, 100, 100)
    user_text = ''
    fundo2=pygame.image.load("nome jogador 2.png")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    nome2=user_text
                    desenha_tabuleiro_multiplayer(tela, matriz, nome1, nome2, tipo_de_jogo)
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode    
        tela.blit(fundo2, (0,0))
        text_surface = fonte.render(user_text, True, (0, 0, 0)) 
        tela.blit(text_surface, (input_rect.x + 130, input_rect.y + 30))
        input_rect.w = max(435, text_surface.get_width() + 10) 
        pygame.display.update()
        if area_sair_escolhaNomes.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                menu_tipoDeJogo(tela, matriz)
        pygame.display.update()

def escolhaNome(tela, matriz, tipo_de_jogo):
    fonte = pygame.font.Font(None, 50)
    input_rect = pygame.Rect(470, 470, 435, 100)
    area_sair_escolhaNomes = pygame.Rect(13, 665, 100, 100)
    user_text = ''
    fundo=pygame.image.load("nome.png")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    nome1=user_text
                    desenha_tabuleiro_singleplayer(tela, matriz, nome1, tipo_de_jogo)
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode     
        tela.blit(fundo, (0,0))
        text_surface = fonte.render(user_text, True, (0, 0, 0)) 
        tela.blit(text_surface, (input_rect.x + 130, input_rect.y + 30))
        input_rect.w = max(435, text_surface.get_width() + 10)
        pygame.display.update()
        if area_sair_escolhaNomes.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                menu_tipoDeJogo(tela, matriz)
        pygame.display.update()

def area1(tela, matriz):
    if matriz[0][0]==0:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (504.5,299))
        pygame.display.update()
        matriz[0][0]= 1
    elif matriz[0][0]==1:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(487,279))
        pygame.display.update()
        tela.blit(triangulo,(504.5,299))
        pygame.display.update()
        matriz[0][0]=2
    elif matriz[0][0]==2:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(487,279))
        pygame.display.update()
        tela.blit(quadrado,(504.5,299))
        pygame.display.update()
        matriz[0][0]=3
def area2(tela, matriz):
    if matriz[0][1]==0:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (618.5,299))
        pygame.display.update()
        matriz[0][1]=1
    elif matriz[0][1]==1:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(601,279))
        pygame.display.update()
        tela.blit(triangulo,(618.5,299))
        pygame.display.update()
        matriz[0][1]=2
    elif matriz[0][1]==2:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(601,279))
        pygame.display.update()
        tela.blit(quadrado,(618.5,299))
        pygame.display.update()
        matriz[0][1]=3
def area3(tela, matriz):
    if matriz[0][2]==0:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (732.5,299))
        pygame.display.update()
        matriz[0][2]=1
    elif matriz[0][2]==1:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(715,279))
        pygame.display.update()
        tela.blit(triangulo,(732.5,299))
        pygame.display.update()
        matriz[0][2]=2
    elif matriz[0][2]==2:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(715,279))
        pygame.display.update()
        tela.blit(quadrado,(732.5,299))
        pygame.display.update()
        matriz[0][2]=3
def area4(tela, matriz):
    if matriz[0][3]==0:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (846.5,299))
        pygame.display.update()
        matriz[0][3]=1
    elif matriz[0][3]==1:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(829,279))
        pygame.display.update()
        tela.blit(triangulo,(846.5,299))
        pygame.display.update()
        matriz[0][3]=2
    elif matriz[0][3]==2:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(829,279))
        pygame.display.update()
        tela.blit(quadrado,(846.5,299))
        pygame.display.update()
        matriz[0][3]=3
def area5(tela, matriz):
    if matriz[1][0]==0:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (504.5,417))
        pygame.display.update()
        matriz[1][0]=1
    elif matriz[1][0]==1:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(487,397))
        pygame.display.update()
        tela.blit(triangulo,(504.5,417))
        pygame.display.update()
        matriz[1][0]=2
    elif matriz[1][0]==2:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(487,397))
        pygame.display.update()
        tela.blit(quadrado,(504.5,417))
        pygame.display.update()
        matriz[1][0]=3
def area6(tela, matriz):
    if matriz[1][1]==0:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (618.5,417))
        pygame.display.update()
        matriz[1][1]=1
    elif matriz[1][1]==1:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(601,397))
        pygame.display.update()
        tela.blit(triangulo,(618.5,417))
        pygame.display.update()
        matriz[1][1]=2
    elif matriz[1][1]==2:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(601,397))
        pygame.display.update()
        tela.blit(quadrado,(618.5,417))
        pygame.display.update()
        matriz[1][1]=3
def area7(tela, matriz):
    if matriz[1][2]==0:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (732.5,417))
        pygame.display.update()
        matriz[1][2]=1
    elif matriz[1][2]==1:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(715,397))
        pygame.display.update()
        tela.blit(triangulo,(732.5,417))
        pygame.display.update()
        matriz[1][2]=2
    elif matriz[1][2]==2:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(715,397))
        pygame.display.update()
        tela.blit(quadrado,(732.5,417))
        pygame.display.update()
        matriz[1][2]=3
def area8(tela, matriz):
    if matriz[1][3]==0:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (846.5,417))
        pygame.display.update()
        matriz[1][3]=1
    elif matriz[1][3]==1:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(829,397))
        pygame.display.update()
        tela.blit(triangulo,(846.5,417))
        pygame.display.update()
        matriz[1][3]=2
    elif matriz[1][3]==2:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(829,397))
        pygame.display.update()
        tela.blit(quadrado,(846.5,417))
        pygame.display.update()
        matriz[1][3]=3
def area9(tela, matriz):
    if matriz[2][0]==0:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (504.5,535))
        pygame.display.update()
        matriz[2][0]=1
    elif matriz[2][0]==1:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(487,515))
        pygame.display.update()
        tela.blit(triangulo,(504.5,535))
        pygame.display.update()
        matriz[2][0]=2
    elif matriz[2][0]==2:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(487,515))
        pygame.display.update()
        tela.blit(quadrado,(504.5,535))
        pygame.display.update()
        matriz[2][0]=3
def area10(tela, matriz):
    if matriz[2][1]==0:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (618.5,535))
        pygame.display.update()
        matriz[2][1]=1
    elif matriz[2][1]==1:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(601,515))
        pygame.display.update()
        tela.blit(triangulo,(618.5,535))
        pygame.display.update()
        matriz[2][1]=2
    elif matriz[2][1]==2:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(601,515))
        pygame.display.update()
        tela.blit(quadrado,(618.5,535))
        pygame.display.update()
        matriz[2][1]=3
def area11(tela, matriz):
    if matriz[2][2]==0:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (732.5,535))
        pygame.display.update()
        matriz[2][2]=1
    elif matriz[2][2]==1:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(715,515))
        pygame.display.update()
        tela.blit(triangulo,(732.5,535))
        pygame.display.update()
        matriz[2][2]=2
    elif matriz[2][2]==2:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(715,515))
        pygame.display.update()
        tela.blit(quadrado,(732.5,535))
        pygame.display.update()
        matriz[2][2]=3
def area12(tela, matriz):
    if matriz[2][3]==0:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (846.5,535))
        pygame.display.update()
        matriz[2][3]=1
    elif matriz[2][3]==1:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(829,515))
        pygame.display.update()
        tela.blit(triangulo,(846.5,535))
        pygame.display.update()
        matriz[2][3]=2
    elif matriz[2][3]==2:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(829,515))
        pygame.display.update()
        tela.blit(quadrado,(846.5,535))
        pygame.display.update()
        matriz[2][3]=3

def area1_carregar(tela, matriz):
    if matriz[0][0]==1:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (504.5,299))
        pygame.display.update()
    elif matriz[0][0]==2:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(487,279))
        pygame.display.update()
        tela.blit(triangulo,(504.5,299))
        pygame.display.update()
    elif matriz[0][0]==3:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(487,279))
        pygame.display.update()
        tela.blit(quadrado,(504.5,299))
        pygame.display.update()
    print(matriz)
def area2_carregar(tela, matriz):
    if matriz[0][1]==1:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (618.5,299))
        pygame.display.update()
    elif matriz[0][1]==2:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(601,279))
        pygame.display.update()
        tela.blit(triangulo,(618.5,299))
        pygame.display.update()
    elif matriz[0][1]==3:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(601,279))
        pygame.display.update()
        tela.blit(quadrado,(618.5,299))
        pygame.display.update()
def area3_carregar(tela, matriz):
    if matriz[0][2]==1:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (732.5,299))
        pygame.display.update()
    elif matriz[0][2]==2:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(715,279))
        pygame.display.update()
        tela.blit(triangulo,(732.5,299))
        pygame.display.update()
    elif matriz[0][2]==3:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(715,279))
        pygame.display.update()
        tela.blit(quadrado,(732.5,299))
        pygame.display.update()
def area4_carregar(tela, matriz):
    if matriz[0][3]==1:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (846.5,299))
        pygame.display.update()
    elif matriz[0][3]==2:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(829,279))
        pygame.display.update()
        tela.blit(triangulo,(846.5,299))
        pygame.display.update()
    elif matriz[0][3]==3:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(829,279))
        pygame.display.update()
        tela.blit(quadrado,(846.5,299))
        pygame.display.update()
def area5_carregar(tela, matriz):
    if matriz[1][0]==1:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (504.5,417))
        pygame.display.update()
    elif matriz[1][0]==2:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(487,397))
        pygame.display.update()
        tela.blit(triangulo,(504.5,417))
        pygame.display.update()
    elif matriz[1][0]==3:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(487,397))
        pygame.display.update()
        tela.blit(quadrado,(504.5,417))
        pygame.display.update()
def area6_carregar(tela, matriz):
    if matriz[1][1]==1:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (618.5,417))
        pygame.display.update()
    elif matriz[1][1]==2:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(601,397))
        pygame.display.update()
        tela.blit(triangulo,(618.5,417))
        pygame.display.update()
    elif matriz[1][1]==3:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(601,397))
        pygame.display.update()
        tela.blit(quadrado,(618.5,417))
        pygame.display.update()
def area7_carregar(tela, matriz):
    if matriz[1][2]==1:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (732.5,417))
        pygame.display.update()
    elif matriz[1][2]==2:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(715,397))
        pygame.display.update()
        tela.blit(triangulo,(732.5,417))
        pygame.display.update()
    elif matriz[1][2]==3:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(715,397))
        pygame.display.update()
        tela.blit(quadrado,(732.5,417))
        pygame.display.update()
def area8_carregar(tela, matriz):
    if matriz[1][3]==1:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (846.5,417))
        pygame.display.update()
    elif matriz[1][3]==2:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(829,397))
        pygame.display.update()
        tela.blit(triangulo,(846.5,417))
        pygame.display.update()
    elif matriz[1][3]==3:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(829,397))
        pygame.display.update()
        tela.blit(quadrado,(846.5,417))
        pygame.display.update()
def area9_carregar(tela, matriz):
    if matriz[2][0]==1:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (504.5,535))
        pygame.display.update()
    elif matriz[2][0]==2:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(487,515))
        pygame.display.update()
        tela.blit(triangulo,(504.5,535))
        pygame.display.update()
    elif matriz[2][0]==3:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(487,515))
        pygame.display.update()
        tela.blit(quadrado,(504.5,535))
        pygame.display.update()
def area10_carregar(tela, matriz):
    if matriz[2][1]==1:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (618.5,535))
        pygame.display.update()
    elif matriz[2][1]==2:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(601,515))
        pygame.display.update()
        tela.blit(triangulo,(618.5,535))
        pygame.display.update()
    elif matriz[2][1]==3:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(601,515))
        pygame.display.update()
        tela.blit(quadrado,(618.5,535))
        pygame.display.update()
def area11_carregar(tela, matriz):
    if matriz[2][2]==1:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (732.5,535))
        pygame.display.update()
    elif matriz[2][2]==2:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(715,515))
        pygame.display.update()
        tela.blit(triangulo,(732.5,535))
        pygame.display.update()
    elif matriz[2][2]==3:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(715,515))
        pygame.display.update()
        tela.blit(quadrado,(732.5,535))
        pygame.display.update()
def area12_carregar(tela, matriz):
    if matriz[2][3]==1:
        circulo=pygame.image.load("bola.png")
        tela.blit(circulo, (846.5,535))
        pygame.display.update()
    elif matriz[2][3]==2:
        triangulo=pygame.image.load("triangulo.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(829,515))
        pygame.display.update()
        tela.blit(triangulo,(846.5,535))
        pygame.display.update()
    elif matriz[2][3]==3:
        quadrado=pygame.image.load("quadrado.png")
        apagar=pygame.image.load("quadrado tabuleiro.png")
        tela.blit(apagar,(829,515))
        pygame.display.update()
        tela.blit(quadrado,(846.5,535))
        pygame.display.update()

def jogo_singleplayer(tela, matriz, nome):
    while True:
        area_sair_jogo = pygame.Rect(13,665,100,100)
        area_regras_ingame = pygame.Rect(113,665,100,100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                mouse_pos=pygame.mouse.get_pos()
                if x>487 and x<594 and y>279 and y<391:
                    area1(tela, matriz)
                if x>601 and x<708 and y>279 and y<391:
                    area2(tela, matriz)
                if x>715 and x<822 and y>279 and y<391:
                    area3(tela, matriz)
                if x>829 and x<936 and y>279 and y<391:
                    area4(tela, matriz)
                if x>487 and x<594 and y>397 and y<510:
                    area5(tela, matriz)
                if x>601 and x<708 and y>397 and y<510:
                    area6(tela, matriz)
                if x>715 and x<822 and y>397 and y<510:
                    area7(tela, matriz)
                if x>829 and x<936 and y>397 and y<510:
                    area8(tela, matriz)
                if x>487 and x<594 and y>515 and y<628:
                    area9(tela, matriz)
                if x>601 and x<708 and y>515 and y<628:
                    area10(tela, matriz)
                if x>715 and x<822 and y>515 and y<628:
                    area11(tela, matriz)
                if x>829 and x<936 and y>515 and y<628:
                    area12(tela, matriz)
                if area_sair_jogo.collidepoint(mouse_pos):
                    main(matriz, nome1, nome2)
                    guarda_matriz(matriz)
                if area_regras_ingame.collidepoint(mouse_pos):
                    menu_regras_ingame_singleplayer(tela, matriz, nome)
                    guarda_matriz(matriz)

def jogo_multiplayer(tela, matriz, nome1, nome2):
    while True:
        area_sair_jogo = pygame.Rect(13,665,100,100)
        area_regras_ingame = pygame.Rect(113,665,100,100)
        fonte = pygame.font.Font("arlrdbd.ttf", 36)
        vez_do_jogador=0
        if vez_do_jogador==0:
            texto_surface = fonte.render("Vez de", True, (153,134,117))
            texto_surface2 = fonte.render(nome1, True, (153,134,117))
        else:
            texto_surface = fonte.render("Vez de", True, (153,134,117))
            texto_surface2 = fonte.render(nome2, True, (153,134,117))
        tela.blit(texto_surface, (170, 367))
        tela.blit(texto_surface2, (175, 420))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = pygame.mouse.get_pos()
                mouse_pos=pygame.mouse.get_pos()
                if x>487 and x<594 and y>279 and y<391:
                    area1(tela, matriz)
                if x>601 and x<708 and y>279 and y<391:
                    area2(tela, matriz)
                if x>715 and x<822 and y>279 and y<391:
                    area3(tela, matriz)
                if x>829 and x<936 and y>279 and y<391:
                    area4(tela, matriz)
                if x>487 and x<594 and y>397 and y<510:
                    area5(tela, matriz)
                if x>601 and x<708 and y>397 and y<510:
                    area6(tela, matriz)
                if x>715 and x<822 and y>397 and y<510:
                    area7(tela, matriz)
                if x>829 and x<936 and y>397 and y<510:
                    area8(tela, matriz)
                if x>487 and x<594 and y>515 and y<628:
                    area9(tela, matriz)
                if x>601 and x<708 and y>515 and y<628:
                    area10(tela, matriz)
                if x>715 and x<822 and y>515 and y<628:
                    area11(tela, matriz)
                if x>829 and x<936 and y>515 and y<628:
                    area12(tela, matriz)
                if area_sair_jogo.collidepoint(mouse_pos):
                    main(matriz, nome1, nome2)
                    guarda_matriz(matriz)
                if area_regras_ingame.collidepoint(mouse_pos):
                    menu_regras_ingame_multiplayer(tela, matriz, nome1, nome2)
                    guarda_matriz(matriz)

def menu_regras_ingame_multiplayer(tela, matriz, nome1, nome2):
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
                    carrega_matriz()
                    desenha_tabuleiro_multiplayer(tela, matriz, nome1, nome2)

def menu_regras_ingame_singleplayer(tela, matriz, nome):
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
                    carrega_matriz()
                    desenha_tabuleiro_singleplayer(tela, matriz, nome, tipo_de_jogo)

def menu_regras(tela, matriz):
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
                    main(matriz, nome1, nome2)

def menu_tipoDeJogo(tela, matriz):
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
                    main(matriz, nome1, nome2)
                elif area_singleplayer.collidepoint(mouse_pos):
                    tipo_de_jogo=1
                    escolhaNome(tela, matriz, tipo_de_jogo)
                elif area_multiplayer.collidepoint(mouse_pos):
                    tipo_de_jogo=2
                    escolhaNome1(tela, matriz, tipo_de_jogo)

def desenha_menu(tela, matriz):
    fundo = pygame.image.load("semaforo menu com peças.png")
    tela.blit(fundo, (0,0))
    pygame.display.update()

def main(matriz, nome1, nome2):
    largura=1366
    altura=768
    tela=pygame.display.set_mode((largura,altura))
    tela.fill(0xA1CCCC)

    area_novo_jogo = pygame.Rect(177, 265, 300, 100)
    area_continuar_jogo = pygame.Rect(177, 361, 300, 100)
    area_regras = pygame.Rect(177, 496, 300, 100)
    area_sair = pygame.Rect(177, 600, 300, 100)

    botaonovojogo = pygame.image.load("novo jogo.png")
    botaocontinuarjogo = pygame.image.load("continuar jogo.png")
    botaoregras = pygame.image.load("regras botao.png")
    botaosair = pygame.image.load("sair botao.png")

    while True:
        desenha_menu(tela, matriz)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mouse_pos=pygame.mouse.get_pos()
                if area_novo_jogo.collidepoint(mouse_pos):
                    matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                    menu_tipoDeJogo(tela, matriz)
                elif area_continuar_jogo.collidepoint(mouse_pos):
                    nomes_carregados=carrega_nomes()
                    nome1=nomes_carregados[0]
                    nome2=nomes_carregados[1]
                    print(nome1)
                    print(nome2)
                    carrega_matriz()
                    carrega_tipo_de_jogo()
                    if tipo_de_jogo==0:
                        desenha_tabuleiro_singleplayer(tela, matriz, nome1)
                    elif tipo_de_jogo==1:
                        desenha_tabuleiro_multiplayer(tela, matriz, nome1, nome2)
                elif area_regras.collidepoint(mouse_pos):
                    menu_regras(tela, matriz)
                elif area_sair.collidepoint(mouse_pos):
                    pygame.quit()
                    exit()
        if area_novo_jogo.collidepoint(pygame.mouse.get_pos()):
            tela.blit(botaonovojogo,(167,251))
            pygame.display.update()
        elif area_continuar_jogo.collidepoint(pygame.mouse.get_pos()):
            tela.blit(botaocontinuarjogo,(162,361))
            pygame.display.update()
        elif area_regras.collidepoint(pygame.mouse.get_pos()):
            tela.blit(botaoregras,(162,490))
            pygame.display.update()
        elif area_sair.collidepoint(pygame.mouse.get_pos()):
            tela.blit(botaosair,(162,597))
            pygame.display.update()      

matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
nome1='Player1'
nome2='Player2'

pygame.display.set_caption("Semáforo!")
pygame.mixer.init()
pygame.mixer.music.load("Magical Sound Shower.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

main(matriz, nome1, nome2)