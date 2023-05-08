import pygame
import sys
import time

# Inicializa o Pygame
pygame.init()

# Constantes e variáveis
WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
BACKGROUND_COLOR = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
GRAY = (128, 128, 128)
FPS = 60

# Configura a tela e as cores
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Jogo dos Semáforos")
clock = pygame.time.Clock()

def draw_traffic_light(x, y, red_on, yellow_on, green_on):
    # Desenha o semáforo
    pygame.draw.rect(screen, GRAY, (x, y, 80, 180))

    # Desenha as luzes
    pygame.draw.circle(screen, RED if red_on else GRAY, (x + 40, y + 40), 20)
    pygame.draw.circle(screen, YELLOW if yellow_on else GRAY, (x + 40, y + 90), 20)
    pygame.draw.circle(screen, GREEN if green_on else GRAY, (x + 40, y + 140), 20)

def update_traffic_light_state(state):
    if state == "red":
        return "green"
    elif state == "yellow":
        return "red"
    else:  # green
        return "yellow"

def main():
    state = "red"
    last_state_change_time = time.time()

    while True:
        # Processa eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Limpa a tela
        screen.fill(BACKGROUND_COLOR)

        # Atualiza o estado do semáforo
        if time.time() - last_state_change_time > 2:
            state = update_traffic_light_state(state)
            last_state_change_time = time.time()

        # Desenha o semáforo
        draw_traffic_light(280, 150, state == "red", state == "yellow", state == "green")

        # Atualiza a tela
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()