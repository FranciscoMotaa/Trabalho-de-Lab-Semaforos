import pygame
from pygame.locals import *

pygame.init()

# Criar a janela
janela = pygame.display.set_mode([1366, 768])
pygame.display.set_caption("Semáforo")

# Carregar as imagens
fundo = pygame.image.load("semaforo menu com peças.png")
#imagem_opcao1 = pygame.image.load("imagem_opcao1.png")
#imagem_opcao2 = pygame.image.load("imagem_opcao2.png")
imagem_opcao3 = pygame.image.load("REGRAS1.png")

opcao_selecionada = None  # Guarda a opção selecionada pelo usuário

janela.blit(fundo, (1366, 768))

# Criar os botões
area_novo_jogo = pygame.Rect(177, 265, 300, 100)
area_continuar_jogo = pygame.Rect(177, 361, 300, 100)
area_regras = pygame.Rect(177, 496, 300, 100)
area_sair = pygame.Rect(177, 600, 300, 100)

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            #if area_novo_jogo.collidepoint(mouse_pos):
                # Lógica para a opção "Novo Jogo"
                #opcao_selecionada = "novo_jogo"
            #elif area_continuar_jogo.collidepoint(mouse_pos):
                # Lógica para a opção "Continuar Jogo"
                #opcao_selecionada = "continuar_jogo"
            if area_regras.collidepoint(mouse_pos):
                # Lógica para a opção "Regras"
                opcao_selecionada = "regras"
            elif area_sair.collidepoint(mouse_pos):
                # Lógica para a opção "Sair"
                loop = False

    # Atualiza a janela de acordo com a opção selecionada
    """if opcao_selecionada == "novo_jogo":
        janela.blit(imagem_opcao1, (0, 0))
        area_voltar_menu = pygame.Rect(40, 663, 100, 100)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if area_voltar_menu.collidepoint(mouse_pos):
                opcao_selecionada = None  # Volta para o menu principal
    elif opcao_selecionada == "continuar_jogo":
        janela.blit(imagem_opcao2, (0, 0))
        area_voltar_menu = pygame.Rect(40, 663, 100, 100)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if area_voltar_menu.collidepoint(mouse_pos):
                opcao_selecionada = None  # Volta para o menu principal"""
    if opcao_selecionada == "regras":
        janela.blit(imagem_opcao3, (0, 0))
        area_voltar_menu = pygame.Rect(40, 663, 100, 100)
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame
