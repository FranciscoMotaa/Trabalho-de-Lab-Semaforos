import pygame

pygame.init()

# Definir as cores
BRANCO = (255, 255, 255)
CINZA_CLARO = (200, 200, 200)
CINZA_ESCURO = (100, 100, 100)

# Definindo a fonte do menu
pygame.font.init()
FONTE = pygame.font.SysFont("Arial", 40)

#opções do menu
opcoes = ["Novo Jogo", "Continuar Jogo", "Regras!"]

# Janela do jogo
largura = 640
altura = 480
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Menu")

# Loop principal do jogo
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Limpar a tela
    tela.fill(BRANCO)

    # Desenhar as opções do menu 
    for i in range(len(opcoes)):
        texto = FONTE.render(opcoes[i], True, CINZA_ESCURO)
        posicao = (largura/2 - texto.get_width()/2, altura/2 - len(opcoes)*30 + i*60)
        tela.blit(texto, posicao)

    # Atualizar a tela
    pygame.display.update()