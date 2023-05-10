#importa a função pygame (Que vai ser necessário para criar a interface, imprimir o tabuleiro na tela e intereagir e assim)
import pygame

from pygame.locals import *
from sys import exit
#inicia o pygame
pygame.init()
#define o tamanho na janela 
largura=640
altura=480
# Cria a janela do Pygame com as dimensões definidas acima
tela=pygame.display.set_mode((largura, altura))
# Define o título da janela
pygame.display.set_caption('Jogo do Semáforo')
# Inicia o loop principal do jogo
while True:
    for event in pygame.event.get():    # Verifica se o usuário fechou a janela
        if event.type == QUIT:
            pygame.quit() # Encerra o Pygame e sai do programa
            exit()
    # Desenha as linhas verticais do tabuleiro
    #pygame.draw.rect(tela, (255, 0, 0), (200, 300, 40, 50))	Vou precisar
    #pygame.draw.circle(tela,(0, 0, 120), (360, 260), 40)	Vou precisar
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
    

    