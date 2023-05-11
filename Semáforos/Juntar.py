import pygame
from pygame.locals import *
from sys import exit

pygame.init()
#Desenhar o tabuleiro
def desenha_tabuleiro(tela):
    pygame.draw.line(tela,(255, 255, 255), (10,10), (10,310), 10)	#1ª linha vertical
    pygame.draw.line(tela,(255, 255, 255), (110,10), (110,310), 10)	#2ª linha vertical
    pygame.draw.line(tela,(255, 255, 255), (210,10), (210,310), 10)	#3ª linha vertical
    pygame.draw.line(tela,(255, 255, 255), (310,10), (310,310), 10)	#4ª linha vertical
    pygame.draw.line(tela,(255, 255, 255), (410,10), (410,310), 10)	#5ª linha vertical
    pygame.draw.line(tela,(255, 255, 255), (10,10), (410,10), 10)	#1ª linha horizontal
    pygame.draw.line(tela,(255, 255, 255), (10,110), (410,110), 10)	#2ª linha horizontal
    pygame.draw.line(tela,(255, 255, 255), (10,210), (410,210), 10)	#3ª linha horizontal
    pygame.draw.line(tela,(255, 255, 255), (10,310), (410,310), 10)	#4ª linha horizontal
    pygame.display.update()

#Desenhar o triangulo
def draw_triangle(screen, color, point):
    point1 = (point[0], point[1]-40)
    point2 = (point[0]+40, point[1]+40)
    point3 = (point[0]-40, point[1]+40)
    pygame.draw.polygon(screen, color, [point1, point2, point3])

#Trocar os desenhos da area1/celula [0][0] da matriz
def area1(tela):
    x, y = pygame.mouse.get_pos()
    if x>16 and x<106 and y>16 and y<106:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
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
            # elif matriz[1][1]==3:
            #     texto=fonte.render(f'Aviso: Não pode alterar esta peça', True, (255,0,0))
            #     tela.blit(texto, (20, 400))
            #     pygame.display.update()
            #     texto=fonte.render(f'Aviso: Não pode alterar esta peça', True, (0,0,0))
            #     tela.blit(texto, (20, 400))

#Trocar os desenhos da area2/celula [0][1] da matriz
def area2(tela):
    x, y = pygame.mouse.get_pos()
    if x>116 and x<206 and y>16 and y<106:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
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

#Trocar os desenhos da area3/celula [0][2] da matriz
def area3(tela):
    x, y = pygame.mouse.get_pos()
    if x>216 and x<306 and y>16 and y<106:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
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

#Trocar os desenhos da area4/celula [0][3] da matriz
def area4(tela):
    x, y = pygame.mouse.get_pos()
    if x>316 and x<406 and y>16 and y<106:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
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

#Trocar os desenhos da area5/celula [1][0] da matriz
def area5(tela):
    x, y = pygame.mouse.get_pos()
    if x>16 and x<106 and y>116 and y<206:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
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

#Trocar os desenhos da area7/celula [1][1] da matriz
def area6(tela):
    x, y = pygame.mouse.get_pos()
    if x>116 and x<206 and y>116 and y<206:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
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

#Trocar os desenhos da area7/celula [1][2] da matriz
def area7(tela):
    x, y = pygame.mouse.get_pos()
    if x>216 and x<306 and y>116 and y<206:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
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

#Trocar os desenhos da area8/celula [1][3] da matriz
def area8(tela):
    x, y = pygame.mouse.get_pos()
    if x>316 and x<406 and y>116 and y<206:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
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

#Trocar os desenhos da area9/celula [2][0] da matriz
def area9(tela):
    x, y = pygame.mouse.get_pos()
    if x>16 and x<106 and y>216 and y<306:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
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

#Trocar os desenhos da area10/celula [2][1] da matriz
def area10(tela):
    x, y = pygame.mouse.get_pos()
    if x>116 and x<206 and y>216 and y<306:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
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

#Trocar os desenhos da area11/celula [2][2] da matriz
def area11(tela):
    x, y = pygame.mouse.get_pos()
    if x>216 and x<306 and y>216 and y<306:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
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

#Trocar os desenhos da area12/celula [2][3] da matriz
def area12(tela):
    x, y = pygame.mouse.get_pos()
    if x>316 and x<406 and y>216 and y<306:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
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

matriz=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

largura=640
altura=480
fonte = pygame.font.Font(None, 50)
tela=pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo do Semáforo')
desenha_tabuleiro(tela)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        else:
            area1(tela)
            area2(tela)
            area3(tela)
            area4(tela)
            area5(tela)
            area6(tela)
            area7(tela)
            area8(tela)
            area9(tela)
            area10(tela)
            area11(tela)
            area12(tela)