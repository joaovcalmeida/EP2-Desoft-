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

def preenche_frota(frota,navio,linha,coluna,orientacao,tamanho):
    if navio not in frota.keys():
        frota[navio] = []
    frota[navio].append(define_posicoes(linha,coluna,orientacao,tamanho))
    return frota

def posicao_valida(dicionario,linha,coluna,orientacao,tamanho):
    p_navio = define_posicoes(linha,coluna, orientacao,tamanho)
    for e in p_navio:
        if e[0] > 9 or e[1]>9:
            return False 
        for coordenadas in dicionario.values():
            for j in coordenadas:
                for h in j:
                    if e[0] == h[0] and e[1] == h[1]:
                        return False
    return True

navios=["porta-aviões","navio-tanque","navio-tanque","contratorpedeiro","contratorpedeiro","contratorpedeiro","submarino","submarino","submarino","submarino"]

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

tamanhos={
    "porta-aviões":4,
    "navio-tanque":3,
    "contratorpedeiro":2,
    "submarino": 1,
}

for navio in navios:
    print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio,tamanhos[navio]))
    linha = int(input('Linha: '))
    coluna = int(input('Coluna: '))
    if navio!='submarino':
        orientacao = int(input('[1] Vertical [2] Horizontal >'))
        if orientacao == 1:
            orientacao = 'vertical'
        elif orientacao == 2:
            orientacao = 'horizontal'
    if navio == 'submarino':
        orientacao='horizontal'   
    valida = posicao_valida (frota,linha,coluna,orientacao,tamanhos[navio])

    while valida==False:
        print('Esta posição não está válida!')
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio,tamanhos[navio]))
        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))
        if navio!='submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal >'))
            if orientacao == 1:
                orientacao = 'vertical'
            elif orientacao == 2:
                orientacao = 'horizontal'
        if navio == 'submarino':
            orientacao= 'horizontal'
    
        valida = posicao_valida(frota,linha,coluna,orientacao,tamanhos[navio])

    definidas=define_posicoes(linha,coluna,orientacao,tamanhos[navio])
    frota=preenche_frota(frota,navio,linha,coluna,orientacao,tamanhos[navio])
    

print(frota)


