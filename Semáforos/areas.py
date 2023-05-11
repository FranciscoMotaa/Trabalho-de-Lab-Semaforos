import pygame

def draw_triangle(screen, color, point):
    point1 = (point[0], point[1]-40)
    point2 = (point[0]+40, point[1]+40)
    point3 = (point[0]-40, point[1]+40)
    pygame.draw.polygon(screen, color, [point1, point2, point3])

def area1(tela):
    x, y = pygame.mouse.get_pos()
    if x>16 and x<106 and y>16 and y<105:
        if event.type==pygame.MOUSEBUTTONDOWN and event.button == 1:
            if matriz[1][1]==0:
                pygame.draw.circle(tela,(0, 255, 0), (60, 63), 40)
                pygame.display.update()
                matriz[1][1]=1
            elif matriz[1][1]==1:
                pygame.draw.circle(tela,(0,0,0),(60,63),40)
                pygame.display.update()
                draw_triangle(tela,(255,255,0),(60,63))
                pygame.display.update()
            elif matriz[1][1]==2:
                draw_triangle(tela,(0,0,0),(60,63))
                rect = pygame.Rect(37.5, 37.5, 50, 50)
                pygame.draw.rect(tela, (255,0,0), rect)
