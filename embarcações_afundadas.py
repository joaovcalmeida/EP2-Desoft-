def afundados(dicionario,tabuleiro):
    afundados = 0
    n_x = 0
    for posicoes in dicionario.values():
        for navio in posicoes:
            for posicao in navio:
                if tabuleiro[posicao[0]][posicao[1]] == 'X':
                    n_x += 1 
            if n_x == len(navio):
                afundados += 1
            n_x = 0
    return afundados