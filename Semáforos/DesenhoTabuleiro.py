import pygame
from pygame.locals import *
from sys import exit

pygame.init()

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

largura=640
altura=480
fonte = pygame.font.Font(None, 30)
tela=pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo do Semáforo')
desenha_tabuleiro(tela)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()