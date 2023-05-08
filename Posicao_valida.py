def define_posicoes(linha, coluna, orientacao, tamanho):
    resultado = []
    i =0 
    while i < tamanho:
        if orientacao == 'vertical':
            resultado.append([linha+i,coluna])
            i+=1
        if orientacao == 'horizontal':
            resultado.append([linha,coluna+i])
            i+=1
    return resultado
            
def posicao_valida(dicionario,linha,coluna,orientacao,tamanho):
    p_navio = define_posicoes(linha,coluna, orientacao,tamanho)
    for i in p_navio:
        if i[0] > 9 or i[1]>9:
            return False 
        for coordenadas in dicionario.values():
            for j in coordenadas:
                for h in j:
                    if i[0] == h[0] and i[1] == h[1]:
                        return False
    return True