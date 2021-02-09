# Portas -----------------------------------------------------------------------
def tabuleiro_inverte_linhaColuna(tab, pos, isLine):
    all_coord = (cria_coordenada(i,j) for i in range(tabuleiro_dimensao(tab)) for j in range(tabuleiro_dimensao(tab)) if not (i == 2 and j == 0))
    for coord in all_coord:
        if coordenada_linha(coord)==pos and isLine or \
           coordenada_coluna(coord)==pos and not isLine:
            newtab = tabuleiro_inverte_estado(tab, coord)
    return newtab
def checkGate(tab, side, gateType):
    if not (eh_tabuleiro(tab) and isinstance(side,str) and side in ('E', 'D')):
        raise ValueError('porta_' + gateType + ': argumentos invalidos')
def porta_x(tab, side):
    checkGate(tab, side, 'x')
    if side == 'E':
        return tabuleiro_inverte_linhaColuna(tab, 1, True)
    return tabuleiro_inverte_linhaColuna(tab, 1, False)
def porta_z(tab, side):
    checkGate(tab, side, 'z')
    if side == 'E':
        return tabuleiro_inverte_linhaColuna(tab, 0, True)
    return tabuleiro_inverte_linhaColuna(tab, 2, False)
def porta_h(tab, side):
    checkGate(tab, side, 'h')
    for i in range(tabuleiro_dimensao(tab)): # swap the whole line/column
        if side == 'E':
            coordA, coordB = cria_coordenada(0, i), cria_coordenada(1, i)
        else:
            coordA, coordB = cria_coordenada(i, 1), cria_coordenada(i, 2)
        cellA, cellB = tabuleiro_celula(tab, coordA), tabuleiro_celula(tab, coordB)
        tab = tabuleiro_substitui_celula(tab, cellB, coordA)
        tab = tabuleiro_substitui_celula(tab, cellA, coordB)
    return tab

