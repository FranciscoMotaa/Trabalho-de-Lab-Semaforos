#importa a função pygame (Que vai ser necessário para criar a interface, imprimir o tabuleiro na tela e intereagir e assim)
import pygame

from pygame.locals import *
from sys import exit
#inicia o pygame
pygame.init()
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

def coloca_peca(tela):
            x, y = pygame.mouse.get_pos()
            rect = pygame.Rect(x, y, 50, 50)
            pygame.draw.rect(tela, (255, 0, 0), rect)
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
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
              coloca_peca(tela)