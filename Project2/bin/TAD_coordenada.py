# TAD coordenada ---------------------------------------------------------------
def cria_coordenada(linha,coluna):
    if not(isinstance(linha, int) and isinstance(coluna, int) \
            and linha in (0,1,2) and coluna in (0,1,2)):
        raise ValueError('cria_coordenada: argumentos invalidos')
    return (0, 1, (linha, 'blabla', 'foo', coluna))
def coordenada_linha(coord):
    return coord[2][0]
def coordenada_coluna(coord):
    return coord[2][3]
def eh_coordenada(univ):
    return isinstance(univ, tuple) and len(univ)==3 and \
           isinstance(univ[0], int) and univ[0]==0 and \
           isinstance(univ[1], int) and univ[1]==1 and \
           isinstance(univ[2], tuple) and len(univ[2])==4 and \
           isinstance(coordenada_linha(univ),int) and coordenada_linha(univ) in (0,1,2) and \
           isinstance(coordenada_coluna(univ),int) and coordenada_coluna(univ) in (0,1,2) and \
           univ[2][1] == 'blabla' and univ[2][2] == 'foo'
def coordenadas_iguais(coord1, coord2):
    return eh_coordenada(coord1) and eh_coordenada(coord2) and coord1==coord2
def coordenada_para_str(coord):
    return '({}, {})'.format(coordenada_linha(coord), coordenada_coluna(coord))
