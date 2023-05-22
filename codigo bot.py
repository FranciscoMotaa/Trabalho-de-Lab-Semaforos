import random 

def bot_jogador(matriz):
    for i in range(3):
        for j in range(4):
            if matriz[i][j]==0:
                move = random.choice(list(legal_moves))
                matriz.push = move
