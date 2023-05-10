import pygame

def draw_triangle(screen, color, point):
    point1 = (point[0], point[1]-50)
    point2 = (point[0]+50, point[1]+50)
    point3 = (point[0]-50, point[1]+50)
    pygame.draw.polygon(screen, color, [point1, point2, point3])