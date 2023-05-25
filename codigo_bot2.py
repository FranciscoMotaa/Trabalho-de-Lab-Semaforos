import random
import pygame
from pygame.locals import *

pygame.init()
tela = pygame.display.set_mode((1366, 768))
pygame.display.set_caption("IA no Pygame")
clock = pygame.time.Clock()

def verifica_vitoria(tela, matriz):
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

    print(vitoria)
    if vitoria==True:
        while True:
            area_sair = pygame.Rect(13, 665, 100, 100)
            fundo = pygame.image.load("VENCEDOR.png")
            tela.blit(fundo, (0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
            
def tela_jogador(tela,jogada):
    fonte = pygame.font.SysFont("arlrdbd.ttf", 40, True, True)
    if jogada == "jogador":
        mensagem = f'É a vez de jogador' #isto vai ter que se alterar para a variavel do nome do men depois 
        texto_formatado = fonte.render(mensagem, True, (255, 0, 0))
        tela.blit(texto_formatado, (100, 397))
        pygame.display.update()
    elif jogada == "bot":
        mensagem = f'É a vez do bot' 
        texto_formatado = fonte.render(mensagem, True, (0, 255, 0))
        tela.blit(texto_formatado, (149, 397))
        pygame.display.update()
    
def jogo_singleplayer(tela, matriz):
    #sorteio para ver quem começa a jogar
    jogadores=["jogador", "bot"]
    jogada=random.choice(jogadores)
    tela_jogador(tela, jogada)
    print(jogada)
    vez_jogador = False
    while True:
        area_sair_jogo = pygame.Rect(13,665,100,100)
        area_regras_ingame = pygame.Rect(113,665,100,100)
        #se o sorteodo for o jogador começa o jogador e depois passa para o bot 
        if jogada=="jogador":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    mouse_pos=pygame.mouse.get_pos()
                    if vez_jogador:
                        posicoe_tabuleir(tela, matriz, x, y)
                        vez_jogador = False
                ai.update()
            jogada = "bot"
        #se o sorteado for o bot faz isto 
        elif jogada=="bot":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                turno_ia(matriz)
                vez_jogador = True
                #ai.render()
            jogada = "jogador"
            ai.update()
            verifica_vitoria(tela,matriz)
        
def posicoe_tabuleir(tela, matriz, x, y):
    if x>487 and x<594 and y>279 and y<391:
                        area1(tela, matriz)
                        verifica_vitoria(tela, matriz)
    if x>601 and x<708 and y>279 and y<391:
                        area2(tela, matriz)
                        verifica_vitoria(tela, matriz)
    if x>715 and x<822 and y>279 and y<391:
                        area3(tela, matriz)
                        verifica_vitoria(tela, matriz)
    if x>829 and x<936 and y>279 and y<391:
                        area4(tela, matriz)
                        verifica_vitoria(tela, matriz)
    if x>487 and x<594 and y>397 and y<510:
                        area5(tela, matriz)
                        verifica_vitoria(tela, matriz)
    if x>601 and x<708 and y>397 and y<510:
                        area6(tela, matriz)
                        verifica_vitoria(tela, matriz)
    if x>715 and x<822 and y>397 and y<510:
                        area7(tela, matriz)
                        verifica_vitoria(tela, matriz)
    if x>829 and x<936 and y>397 and y<510:
                        area8(tela, matriz)
                        verifica_vitoria(tela, matriz)
    if x>487 and x<594 and y>515 and y<628:
                        area9(tela, matriz)
                        verifica_vitoria(tela, matriz)
    if x>601 and x<708 and y>515 and y<628:
                        area10(tela, matriz)
                        verifica_vitoria(tela, matriz)
    if x>715 and x<822 and y>515 and y<628:
                        area11(tela, matriz)
                        verifica_vitoria(tela, matriz)
    if x>829 and x<936 and y>515 and y<628:
                        area12(tela, matriz)
                        verifica_vitoria(tela, matriz)
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

def desenha_tabuleiro_singleplayer(tela, matriz):
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
                exit()
            elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
                mouse_pos=pygame.mouse.get_pos()

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
                #verifica_vitoria(tela, matriz)
                jogo_singleplayer(tela, matriz)

def turno_ia(matriz):
    #ve quais são as casas disponiveis 
    casas_disponiveis = []
    #percorre a matriz do jogo e se aquela posição tiver a zeros adiciona á lista de casas_disponiveis 
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 0:
                casas_disponiveis.append((i,j)) 
    #se condição para ler o tabuleiro e colocar lá as peças na matriz                         
    if casas_disponiveis:
        i, j = random.choice(casas_disponiveis)
        if matriz[i][j] == 0:
            matriz[i][j] = 1
            realizar_acao_interface(matriz, i, j, tela)
        elif matriz[i][j] == 1:
            matriz[i][j] = 2
            realizar_acao_interface(matriz, i, j, tela)
        elif matriz[i][j] == 2:
            matriz[i][j] = 3
            realizar_acao_interface(matriz, i, j, tela) 

        print(matriz)
    
def realizar_acao_interface(matriz, i, j, tela):
    valor = matriz[i][j]
    #fazer load das imagens 
    bola = pygame.image.load("bola.png")
    triangulo = pygame.image.load("triangulo.png")
    quadrado = pygame.image.load("quadrado.png")

    coordenadas = [
        (490, 282), (603, 282), (718, 282), (831, 282),
        (490, 400), (603, 400), (718, 400), (831, 400),
        (490, 518), (603, 518), (718, 518), (831, 518)
    ]
    x, y = coordenadas[i + j]

    if valor == 1:
        tela.blit(bola,(x,y))
        pygame.display.update()
    elif valor == 2:
        tela.blit(triangulo,(x,y))
        pygame.display.update()
    elif valor == 3:
       tela.blit(quadrado, (x,y))
       pygame.display.update() 
        



class AI:
    def __init__(self, tela):
        self.x = 490
        self.y = 282
        self.speed = 6
        self.bola = pygame.image.load("bola.png")
        self.triangulo = pygame.image.load("triangulo.png")
        self.quadrado = pygame.image.load("quadrado.png")
        self.tela = tela
        self.matriz = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.current_position = self.get_random_position_tabule(self)
        
    def get_random_position_matriz(self):
        matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        return random.choice(matriz)
    
    def get_random_position_tabule(self, matriz):
        positions = [
            (540, 336), (656, 336), (771, 336), (887, 336),
            (540, 451), (656, 451), (771, 451), (887, 451),
            (540, 570), (656, 570), (771, 570), (887, 570)
        ]

        matriz=[
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]]

        return random.choice(positions)

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            pygame.display.update()

    def render(self):
        x, y = self.current_position
        tela.blit(self.bola, (x - self.bola.get_width() // 2, y - self.bola.get_height() // 2))
        tela.blit(self.triangulo, (x - self.triangulo.get_width() // 2, y - self.triangulo.get_height() // 2))
        tela.blit(self.quadrado, (x - self.quadrado.get_width() // 2, y - self.quadrado.get_height() // 2))
        jogo_singleplayer(tela, matriz)
        pygame.display.update()
ai = AI(tela)


#o codigo começa aqui 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    matriz=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    #matriz=[[1,1,1,1],[1,1,1,1],[1,1,1,1]]
    desenha_tabuleiro_singleplayer(tela, matriz)
    ai.update()
    #ai.render()
    pygame.display.update()
    clock.tick(50)
