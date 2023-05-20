import random

def bot_move(grid):
    # Percorre todas as células do grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Encontra a primeira luz apagada e faz a jogada
            if grid[i][j] == 0:
                return i, j

# Função principal do jogo
def main():
    # Criação do grid do jogo
    grid = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    # Variável para controlar a vez do jogador
    jogador = 1

    # Loop principal do jogo
    while True:
        if jogador == 1:
            # Lógica do jogador humano
            # Aqui você pode implementar a interação com o jogador humano
            pass
        elif jogador == 2:
            # Lógica do bot
            row, col = bot_move(grid)
            if grid[row][col] == 0:
                grid[row][col] = jogador
            # Alterna para a vez do jogador humano
            jogador = 1

        # Verifica se o jogo terminou (condição de vitória ou empate)
        # Aqui você precisa implementar a lógica para verificar a condição de vitória ou empate no "Semáforos"

        # Alterna a vez dos jogadores

# Executa o jogo
if __name__ == "__main__":
    main()