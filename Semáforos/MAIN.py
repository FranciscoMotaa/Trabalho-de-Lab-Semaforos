import pygame
import pygame.mixer
from pygame.locals import *
from sys import exit
import random
pygame.init()

def verifica_vitoria(tela, matriz, nome):
    vitoria=False
    if matriz[0][0]==matriz[0][1] and matriz[0][1]==matriz[0][2] and matriz[0][2]!=0:
        vitoria=True
    elif matriz[0][1]==matriz[0][2] and matriz[0][2]==matriz[0][3] and matriz[0][3]!=0:
        vitoria=True
    elif matriz[1][0]==matriz[1][1] and matriz[1][1]==matriz[1][2] and matriz[1][2]!=0:
        vitoria=True
    elif matriz[1][1]==matriz[1][2] and matriz[1][2]==matriz[1][3] and matriz[1][3]!=0:
        vitoria=True
    elif matriz[2][0]==matriz[2][1] and matriz[2][1]==matriz[2][2] and matriz[2][2]!=0:
        vitoria=True
    elif matriz[2][1]==matriz[2][2] and matriz[2][2]==matriz[2][3] and matriz[2][3]!=0:
        vitoria=True
    elif matriz[0][0]==matriz[1][0] and matriz[1][0]==matriz[2][0] and matriz[2][0]!=0:
        vitoria=True
    elif matriz[0][1]==matriz[1][1] and matriz[1][1]==matriz[2][1] and matriz[2][1]!=0:
        vitoria=True
    elif matriz[0][2]==matriz[1][2] and matriz[1][2]==matriz[2][2] and matriz[2][2]!=0:
        vitoria=True
    elif matriz[0][3]==matriz[1][3] and matriz[1][3]==matriz[2][3] and matriz[2][3]!=0:
        vitoria=True
    elif matriz[0][0]==matriz[1][1] and matriz[1][1]==matriz[2][2] and matriz[2][2]!=0:
        vitoria=True
    elif matriz[0][1]==matriz[1][2] and matriz[1][2]==matriz[2][3] and matriz[2][3]!=0:
        vitoria=True
    elif matriz[0][3]==matriz[1][2] and matriz[1][2]==matriz[2][1] and matriz[2][1]!=0:
        vitoria=True
    elif matriz[0][2]==matriz[1][1] and matriz[1][1]==matriz[2][0] and matriz[2][0]!=0:
        vitoria=True

    if vitoria==True:
        while True:
            area_sair = pygame.Rect(13, 665, 100, 100)
            fundo = pygame.image.load("VENCEDOR.png")
            pygame.time.delay(400)
            tela.blit(fundo, (0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    guarda_nome(nome)
                    guarda_matriz(matriz)
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                    mouse_pos=pygame.mouse.get_pos()
                    if area_sair.collidepoint(mouse_pos):
                        som_click()
                        guarda_nome(nome)
                        guarda_matriz(matriz)
                        main()

def carrega_nome():
    with open("nome.txt", "r") as ficheiro_nome:
        conteudo = ficheiro_nome.read()
        nome = conteudo.split()
    return nome

def guarda_nome(nome):
    ficheiro_nome = open("nome.txt", "w")
    ficheiro_nome.write(str(nome))
    ficheiro_nome.close()

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

def desenha_tabuleiro_singleplayer(tela, matriz, nome):
    while True:
        area_sair_jogo = pygame.Rect(13,665,100,100)
        area_regras_ingame = pygame.Rect(113,665,100,100)
        fundo = pygame.image.load("vez do jogador.png")
        tela.blit(fundo, (0,0))
        pygame.display.update()
        #fazer random para ver quem comeca
        #fazar ciclo para jogar um jogador e depois o outro
        #a medida que troca de jogador troca o texto da vez
        #a cada jogada verificar se ganhou
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                guarda_nome(nome)
                guarda_matriz(matriz)
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mouse_pos=pygame.mouse.get_pos()
                if area_sair_jogo.collidepoint(mouse_pos):
                    som_click()

                    guarda_nome(nome)
                    guarda_matriz(matriz)
                    main(matriz, nome)
                if area_regras_ingame.collidepoint(mouse_pos):
                    som_click()
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
                verifica_vitoria(tela, matriz, nome)
                jogo_singleplayer(tela, matriz, nome)

def escolhaNome(tela, matriz):
    fonte = pygame.font.Font(None, 50)
    input_rect = pygame.Rect(470, 470, 435, 100)
    area_sair_escolhaNomes = pygame.Rect(13, 665, 100, 100)
    user_text = ''
    fundo=pygame.image.load("nome.png")
    tela.blit(fundo, (0,0))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    nome=user_text
                    desenha_tabuleiro_singleplayer(tela, matriz, nome)
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode     
        text_surface = fonte.render(user_text, True, (0, 0, 0)) 
        tela.blit(text_surface, (input_rect.x + 134, input_rect.y + 30))
        input_rect.w = max(435, text_surface.get_width() + 10)
        pygame.display.update()
        if area_sair_escolhaNomes.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                som_click()
                escolhaTipoDeJogo(tela, matriz)
        pygame.display.update()

def escolhaTipoDeJogo(tela, matriz):
    fonte = pygame.font.Font(None, 50)
    single_botao = pygame.Rect(334, 449, 339, 86)
    area_sair_escolhaNomes = pygame.Rect(13, 665, 100, 100)
    multiplayer_botao = pygame.Rect(735, 450, 339, 86)
    fundo=pygame.image.load("escolher tipo de jogo.png")
    tela.blit(fundo, (0,0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mouse_pos=pygame.mouse.get_pos()
                if area_sair_escolhaNomes.collidepoint(mouse_pos):
                    som_click()
                    main()
                elif single_botao.collidepoint(mouse_pos):
                    som_click()
                    escolhaNome(tela, matriz)
                elif multiplayer_botao.collidepoint(mouse_pos):
                    som_click()
                    nome_multiplayer(tela,matriz)

def nome_multiplayer(tela,matriz):
    fundo = pygame.image.load("nome jogador 1.png")
    area_sair_escolhaNomes = pygame.Rect(13, 665, 100, 100)
    nome1_botao = pygame.Rect(481, 477, 408, 86)
    tela.blit(fundo, (0,0))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mouse_pos=pygame.mouse.get_pos()
                if area_sair_escolhaNomes.collidepoint(mouse_pos):
                    som_click()
                    escolhaTipoDeJogo(tela, matriz)
                elif nome1_botao.collidepoint(mouse_pos):
                    nome1_multiplayer(tela, matriz)

def nome1_multiplayer(tela, matriz):
    fonte = pygame.font.Font(None, 50)
    input_rect = pygame.Rect(470, 470, 435, 100)
    area_sair_escolhaNomes = pygame.Rect(13, 665, 100, 100)
    user_text = ''
    fundo=pygame.image.load("nome jogador 1.png")
    tela.blit(fundo, (0,0))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    nome1=user_text   
                    nome2_multiplayer(tela, matriz, nome1)
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode     
        text_surface = fonte.render(user_text, True, (0, 0, 0)) 
        tela.blit(text_surface, (input_rect.x + 134, input_rect.y + 30))
        input_rect.w = max(435, text_surface.get_width() + 10)
        pygame.display.update()
        if area_sair_escolhaNomes.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                som_click()
                main()
        pygame.display.update()
    
def nome2_multiplayer(tela,matriz, nome1):
    fonte = pygame.font.Font(None, 50)
    input_rect = pygame.Rect(470, 470, 435, 100)
    area_sair_escolhaNomes = pygame.Rect(13, 665, 100, 100)
    user_text = ''
    fundo=pygame.image.load("nome jogador 2.png")
    tela.blit(fundo, (0,0))
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    nome2=user_text #alterar esta variavel depois 
                    while True:
                        multiplayer_jogo(tela, matriz, nome1, nome2)
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode     
        text_surface = fonte.render(user_text, True, (0, 0, 0)) 
        tela.blit(text_surface, (input_rect.x + 134, input_rect.y + 30))
        input_rect.w = max(435, text_surface.get_width() + 10)
        pygame.display.update()
        if area_sair_escolhaNomes.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                som_click()
                escolhaTipoDeJogo(tela, matriz)
        pygame.display.update()

def multiplayer_jogo(tela, matriz, nome1, nome2, running=True):
    fundo = pygame.image.load("vez do jogador.png")
    tela.blit(fundo, (0,0))
    jogadores=[nome1, nome2]
    jogada=random.choice(jogadores)
    
    fonte = pygame.font.SysFont("arlrdbd.ttf", 40, True, True)
    mensagem = f'É a vez de' #isto vai ter que se alterar para a variavel do nome do men depois 
    if jogada == nome1:
        cor = (255,0,0)
    else:
        cor = (0,255,0)
    texto_formatado = fonte.render(mensagem, True, cor)
    mensagem_nome = f'{jogada}'
    texto_formatado1 = fonte.render(mensagem_nome, True, cor)
    tela.blit(texto_formatado, (100, 372))
    tela.blit(texto_formatado1, (150, 430))

    while running:
        area_sair_jogo = pygame.Rect(13,665,100,100)
        area_regras_ingame = pygame.Rect(113,665,100,100)
        if True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    mouse_pos=pygame.mouse.get_pos()
                    if x>487 and x<594 and y>279 and y<391:
                        area1(tela, matriz)
                        verifica_vitoria(tela, matriz, nome1)

                    if x>601 and x<708 and y>279 and y<391:
                        area2(tela, matriz)
                        verifica_vitoria(tela, matriz, nome1)
                    if x>715 and x<822 and y>279 and y<391:
                        area3(tela, matriz)
                        verifica_vitoria(tela, matriz, nome1)
                    if x>829 and x<936 and y>279 and y<391:
                        area4(tela, matriz)
                        verifica_vitoria(tela, matriz, nome1)
                    if x>487 and x<594 and y>397 and y<510:
                        area5(tela, matriz)
                        verifica_vitoria(tela, matriz, nome1)
                    if x>601 and x<708 and y>397 and y<510:
                        area6(tela, matriz)
                        verifica_vitoria(tela, matriz, nome1)
                    if x>715 and x<822 and y>397 and y<510:
                        area7(tela, matriz)
                        verifica_vitoria(tela, matriz, nome1)
                    if x>829 and x<936 and y>397 and y<510:
                        area8(tela, matriz)
                        verifica_vitoria(tela, matriz, nome1)
                    if x>487 and x<594 and y>515 and y<628:
                        area9(tela, matriz)
                        verifica_vitoria(tela, matriz, nome1)
                    if x>601 and x<708 and y>515 and y<628:
                        area10(tela, matriz)
                        verifica_vitoria(tela, matriz, nome1)
                    if x>715 and x<822 and y>515 and y<628:
                        area11(tela, matriz)
                        verifica_vitoria(tela, matriz, nome1)
                    if x>829 and x<936 and y>515 and y<628:
                        area12(tela, matriz)
                        verifica_vitoria(tela, matriz, nome1)
                    if area_sair_jogo.collidepoint(mouse_pos):
                        som_click()
                        guarda_matriz(matriz)
                        main()
                    if area_regras_ingame.collidepoint(mouse_pos):
                        som_click()
                        menu_regras_ingame_singleplayer(tela, matriz, nome1)
                        guarda_matriz(matriz)

                if jogada == nome1:
                    jogada = nome2
                else: 
                    jogada = nome1

                pygame.display.flip()

def tela_jogador(tela, jogada, nome1, nome2):
    fonte = pygame.font.SysFont("arlrdbd.ttf", 40, True, True)
    if jogada == nome1:
        mensagem = f'É a vez de' #isto vai ter que se alterar para a variavel do nome do men depois 
        texto_formatado = fonte.render(mensagem, True, (255, 0, 0))
        mensagem_nome = f'{nome1}'
        texto_formatado1 = fonte.render(mensagem_nome, True, (255, 0, 0))
        tela.blit(texto_formatado, (100, 372))
        tela.blit(texto_formatado1, (150, 430))
    elif jogada == nome2:
        mensagem = f'É a vez de'
        texto_formatado = fonte.render(mensagem, True, (0, 255, 0))
        mensagem_nome = f'{nome2}'
        texto_formatado1 = fonte.render(mensagem_nome, True, (0, 255, 0))
        tela.blit(texto_formatado, (100, 372))
        tela.blit(texto_formatado1, (150, 430))
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
    jogadores=["jogador", "bot"]
    jogada=random.choice(jogadores)
    while True:
        area_sair_jogo = pygame.Rect(13,665,100,100)
        area_regras_ingame = pygame.Rect(113,665,100,100)
        if jogada=="jogador":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    mouse_pos=pygame.mouse.get_pos()
                    if x>487 and x<594 and y>279 and y<391:
                        area1(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>601 and x<708 and y>279 and y<391:
                        area2(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>715 and x<822 and y>279 and y<391:
                        area3(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>829 and x<936 and y>279 and y<391:
                        area4(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>487 and x<594 and y>397 and y<510:
                        area5(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>601 and x<708 and y>397 and y<510:
                        area6(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>715 and x<822 and y>397 and y<510:
                        area7(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>829 and x<936 and y>397 and y<510:
                        area8(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>487 and x<594 and y>515 and y<628:
                        area9(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>601 and x<708 and y>515 and y<628:
                        area10(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>715 and x<822 and y>515 and y<628:
                        area11(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>829 and x<936 and y>515 and y<628:
                        area12(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if area_sair_jogo.collidepoint(mouse_pos):
                        som_click()

                        guarda_matriz(matriz)
                        main()
                    if area_regras_ingame.collidepoint(mouse_pos):
                        som_click()

                        menu_regras_ingame_singleplayer(tela, matriz, nome)
                        guarda_matriz(matriz)
        elif jogada=="bot":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    mouse_pos=pygame.mouse.get_pos()
                    if x>487 and x<594 and y>279 and y<391:
                        area1(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>601 and x<708 and y>279 and y<391:
                        area2(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>715 and x<822 and y>279 and y<391:
                        area3(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>829 and x<936 and y>279 and y<391:
                        area4(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>487 and x<594 and y>397 and y<510:
                        area5(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>601 and x<708 and y>397 and y<510:
                        area6(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>715 and x<822 and y>397 and y<510:
                        area7(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>829 and x<936 and y>397 and y<510:
                        area8(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>487 and x<594 and y>515 and y<628:
                        area9(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>601 and x<708 and y>515 and y<628:
                        area10(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>715 and x<822 and y>515 and y<628:
                        area11(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if x>829 and x<936 and y>515 and y<628:
                        area12(tela, matriz)
                        verifica_vitoria(tela, matriz, nome)
                    if area_sair_jogo.collidepoint(mouse_pos):
                        som_click()

                        guarda_matriz(matriz)
                        main()
                    if area_regras_ingame.collidepoint(mouse_pos):
                        som_click()

                        menu_regras_ingame_singleplayer(tela, matriz, nome)
                        guarda_matriz(matriz) 

                """ posicoes_disponiveis = posicoes_disponiveis(matriz)
                if posicoes_disponiveis:
                    posicao = random.choice(posicoes_disponiveis)
                    i, j = posicao
                    # Realize a jogada do bot na posição (i, j) desejada
                    matriz[i][j] = 0  # Substitua "amarelo" pela cor desejada
                else:
                    return False
                    # Tratamento quando não há posições disponíveis
 """
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
                    som_click()
                    carrega_matriz()
                    desenha_tabuleiro_singleplayer(tela, matriz, nome)
                    som_click()


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
                    som_click()

                    main()

def desenha_menu(tela):
    fundo = pygame.image.load("semaforo menu com peças.png")
    tela.blit(fundo, (0,0))
    pygame.display.update()

def som_click():
    click_sound= pygame.mixer.Sound("Mouse_Click_3-fesliyanstudios.com.mp3")
    click_sound.set_volume(0.4)
    click_sound.play()
    pygame.time.delay(250)

def main():
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
        desenha_menu(tela)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mouse_pos=pygame.mouse.get_pos()
                if area_novo_jogo.collidepoint(mouse_pos):
                    som_click()
                    matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
                    escolhaTipoDeJogo(tela, matriz)
                elif area_continuar_jogo.collidepoint(mouse_pos):
                    som_click()
                    nome=carrega_nome()
                    print(nome)
                    matriz=carrega_matriz()
                    print(matriz)
                    desenha_tabuleiro_singleplayer(tela, matriz, nome)
                elif area_regras.collidepoint(mouse_pos):
                    som_click()
                    menu_regras(tela)
                elif area_sair.collidepoint(mouse_pos):
                    som_click()
                    pygame.time.delay(500)
                    guarda_nome(nome)
                    guarda_matriz(matriz)
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

pygame.display.set_caption("Semáforo!")
pygame.mixer.init()
pygame.mixer.music.load("Magical Sound Shower.mp3")
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)

main()