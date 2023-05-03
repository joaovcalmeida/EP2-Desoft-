def define_posicoes(linha,coluna, orientacao,tamanho):
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
            