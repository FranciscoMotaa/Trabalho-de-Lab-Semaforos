mensagem = f'É a vez de' #isto vai ter que se alterar para a variavel do nome do men depois 
    if jogada == nome1:
        cor = (255,0,0)
    else:
        cor = (0,255,0)
    texto_formatado = fonte.render(mensagem, True, cor)
    mensagem_nome = f'{jogada}'
    texto_formatado1 = fonte.render(mensagem_nome, True, cor)
    tela.blit(texto_formatado, (100, 372))
    tela.blit(texto_formatado1, (150, 430))
