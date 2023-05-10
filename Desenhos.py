import pygame
from pygame.locals import *
from sys import exit

pygame.init()

def draw_triangle(screen, color, point):
    point1 = (point[0], point[1]-40)
    point2 = (point[0]+40, point[1]+40)
    point3 = (point[0]-40, point[1]+40)
    pygame.draw.polygon(screen, color, [point1, point2, point3])

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

def area1(tela):
    x, y = pygame.mouse.get_pos()
    if x>20 and y>20 and x<110 and y<110:
        rect = pygame.Rect(37.5, 37.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()

def teste(tela):
    if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
        pygame.draw.circle(tela,(0,0,0),(162.5,62.5),40)
        pygame.display.update()
        draw_triangle(tela,(255,255,0),(162.5,60))
        pygame.display.update()

def area2(tela):
    x, y = pygame.mouse.get_pos()
    if x>120 and y>20 and x<210 and y<110:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
            pygame.draw.circle(tela,(0, 255, 0), (162.5, 62.5), 40)
            pygame.display.update()
            teste(tela)
        # if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
        #     pygame.draw.circle(tela,(0,0,0),(162.5,62.5),40)
        #     pygame.display.update()
        #     draw_triangle(tela,(255,255,0),(162.5,60))
        #     pygame.display.update()
        # if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
        #     draw_triangle(tela,(0,0,0),(162.5,60))
        #     rect = pygame.Rect(137.5, 37.5, 50, 50)
        #     pygame.draw.rect(tela, (255,0,0), rect)

def area3(tela):
    x, y = pygame.mouse.get_pos()
    if x>220 and y>20 and x<310 and y<110:
        #rect = pygame.Rect(237.5, 37.5, 50, 50)
        #pygame.draw.rect(tela, (255,0,0), rect)
        draw_triangle(tela,(255,255,0),(262.5,60))
        pygame.display.update()

def area4(tela):
    x, y = pygame.mouse.get_pos()
    if x>320 and y>20 and x<410 and y<110:
        rect = pygame.Rect(337.5, 37.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()

def area5(tela):
    x, y = pygame.mouse.get_pos()
    if x>20 and y>120 and x<110 and y<210:
        rect = pygame.Rect(37.5, 137.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()

def area6(tela):
    x, y = pygame.mouse.get_pos()
    if x>120 and y>120 and x<210 and y<210:
        rect = pygame.Rect(137.5, 137.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()

def area7(tela):
    x, y = pygame.mouse.get_pos()
    if x>220 and y>120 and x<310 and y<210:
        rect = pygame.Rect(237.5, 137.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()

def area8(tela):
    x, y = pygame.mouse.get_pos()
    if x>320 and y>120 and x<410 and y<210:
        rect = pygame.Rect(337.5, 137.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()

def area9(tela):
    x, y = pygame.mouse.get_pos()
    if x>20 and y>220 and x<110 and y<300:
        rect = pygame.Rect(37.5, 237.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()

def area10(tela):
    x, y = pygame.mouse.get_pos()
    if x>120 and y>220 and x<210 and y<300:
        rect = pygame.Rect(137.5, 237.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()

def area11(tela):
    x, y = pygame.mouse.get_pos()
    if x>220 and y>220 and x<310 and y<300:
        rect = pygame.Rect(237.5, 237.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()

def area12(tela):
    x, y = pygame.mouse.get_pos()
    if x>320 and y>220 and x<410 and y<300:
        rect = pygame.Rect(337.5, 237.5, 50, 50)
        pygame.draw.rect(tela, (255,0,0), rect)
        pygame.display.update()

largura=640
altura=480
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