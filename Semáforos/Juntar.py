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

#Trocar os desenhos da area2/celula [0][1] da matriz
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

#Trocar os desenhos da area3/celula [0][2] da matriz
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

#Trocar os desenhos da area4/celula [0][3] da matriz
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

#Trocar os desenhos da area5/celula [1][0] da matriz
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

#Trocar os desenhos da area7/celula [1][1] da matriz
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

#Trocar os desenhos da area7/celula [1][2] da matriz
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

#Trocar os desenhos da area8/celula [1][3] da matriz
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

#Trocar os desenhos da area9/celula [2][0] da matriz
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

#Trocar os desenhos da area10/celula [2][1] da matriz
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

#Trocar os desenhos da area11/celula [2][2] da matriz
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

#Trocar os desenhos da area12/celula [2][3] da matriz
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

def menu_tipoDeJogo(tela):
    while True:
        tela.fill(BLACK)
        pygame.draw.rect(tela, BLACK, (button1_pos[0], button1_pos[1], button_width, button_height))
        pygame.draw.rect(tela, BLACK, (button2_pos[0], button2_pos[1], button_width, button_height))
        tela.blit(button4_text, (button4_pos[0]+10, button4_pos[1]+10))
        tela.blit(button5_text, (button5_pos[0]+10, button5_pos[1]+10))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            else:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = pygame.mouse.get_pos()
                    if button4_rect.collidepoint(mouse_pos):
                        tela.fill(BLACK)
                        pygame.display.update()
                        jogo(tela)
                    elif button5_rect.collidepoint(mouse_pos):
                        print("butao 5 pressionado")

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
                    erro=False
                    area1(tela)
                if x>116 and x<206 and y>16 and y<106:
                    erro=False
                    area2(tela)
                if x>216 and x<306 and y>16 and y<106:
                    erro=False
                    area3(tela)
                if x>316 and x<406 and y>16 and y<106:
                    erro=False
                    area4(tela)
                if x>16 and x<106 and y>116 and y<206:
                    erro=False
                    area5(tela)
                if x>116 and x<206 and y>116 and y<206:
                    erro=False
                    area6(tela)
                if x>216 and x<306 and y>116 and y<206:
                    erro=False
                    area7(tela)
                if x>316 and x<406 and y>116 and y<206:
                    erro=False
                    area8(tela)
                if x>16 and x<106 and y>216 and y<306:
                    erro=False
                    area9(tela)
                if x>116 and x<206 and y>216 and y<306:
                    erro=False
                    area10(tela)
                if x>216 and x<306 and y>216 and y<306:
                    erro=False
                    area11(tela)
                if x>316 and x<406 and y>216 and y<306:
                    erro=False
                    area12(tela)

def desenha_menu(tela):
    tela.fill(BLACK)
    pygame.draw.rect(tela, BLACK, (button1_pos[0], button1_pos[1], button_width, button_height))
    pygame.draw.rect(tela, BLACK, (button2_pos[0], button2_pos[1], button_width, button_height))
    pygame.draw.rect(tela, BLACK, (button3_pos[0], button3_pos[1], button_width, button_height))
    tela.blit(button1_text, (button1_pos[0]+10, button1_pos[1]+10))
    tela.blit(button2_text, (button2_pos[0]+10, button2_pos[1]+10))
    tela.blit(button3_text, (button3_pos[0]+10, button3_pos[1]+10))
    pygame.display.update()

matriz=[
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
largura=1366
altura=768
fonte = pygame.font.Font(None, 50)
tela=pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo do Semáforo')
# Define as posições e dimensões dos botões
button_width = 200
button_height = 50
button1_pos = (largura//2 - button_width//2, 100)
button2_pos = (largura//2 - button_width//2, 200)
button3_pos = (largura//2 - button_width//2, 300)
button4_pos = (largura//2 - button_width//2, 100)
button5_pos = (largura//2 - button_width//2, 200)

# Cria os textos dos botões
button1_text = fonte.render("Novo Jogo", True, WHITE)
button2_text = fonte.render("Continuar Jogo", True, WHITE)
button3_text = fonte.render("Regras", True, WHITE)
button1_rect = pygame.Rect(button1_pos, (button_width, button_height))
button2_rect = pygame.Rect(button2_pos, (button_width, button_height))
button3_rect = pygame.Rect(button3_pos, (button_width, button_height))
button4_text = fonte.render("Player vs Player", True, WHITE)
button5_text = fonte.render("Player vs BOT", True, WHITE)
button4_rect = pygame.Rect(button4_pos, (button_width, button_height))
button5_rect = pygame.Rect(button5_pos, (button_width, button_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        else:
            desenha_menu(tela)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if button1_rect.collidepoint(mouse_pos):
                    tela.fill(BLACK)
                    pygame.display.update()
                    menu_tipoDeJogo(tela)
                    jogo(tela)
                elif button2_rect.collidepoint(mouse_pos):
                    print("butao 2 pressionado")
                elif button3_rect.collidepoint(mouse_pos):
                    print("Mostra regras")
