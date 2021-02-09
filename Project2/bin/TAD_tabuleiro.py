# TAD Tabuleiro ----------------------------------------------------------------
class TabuleiroXYZ:
    def __init__(self, *args):
        if len(args) == 0:
            self.XYZ = ('bla', { coordenada_para_str(cria_coordenada(0,0)) : cria_celula(-1),
                 coordenada_para_str(cria_coordenada(0,1)) : cria_celula(-1),
                 coordenada_para_str(cria_coordenada(0,2)) : cria_celula(-1),
                 coordenada_para_str(cria_coordenada(1,0)) : cria_celula( 0),
                 coordenada_para_str(cria_coordenada(1,1)) : cria_celula( 0),
                 coordenada_para_str(cria_coordenada(1,2)) : cria_celula(-1),
                 coordenada_para_str(cria_coordenada(2,1)) : cria_celula( 0),
                 coordenada_para_str(cria_coordenada(2,2)) : cria_celula(-1) }, 'blop')
        else:
            self.XYZ = args[0]

def tabuleiro_inicial():
	return TabuleiroXYZ()

def str_para_tabuleiro(cad):
    tab, tup = {}, eval(cad)
    for l in range(len(tup)):
        for c in range(len(tup[l])):
            pos = c if l<2 else c+1
            tab[coordenada_para_str(cria_coordenada(l, pos))] = cria_celula(tup[l][c])
    return TabuleiroXYZ(('bla', tab, 'blop'))

def tabuleiro_dimensao(tab):
    return 3
def eh_tabuleiro(univ_c):
    univ = univ_c.XYZ
    return isinstance(univ_c, TabuleiroXYZ) and isinstance(univ, tuple) and len(univ)==3 and \
           isinstance(univ[0], str) and univ[0]=='bla' and \
           isinstance(univ[2], str) and univ[2]=='blop' and \
           isinstance(univ[1], dict) and len(univ[1])==8 and \
            all(str(k) and eh_celula(univ[1][k]) for k in univ[1])
def tabuleiro_celula(tab, coord):
    if not (eh_tabuleiro(tab) and eh_coordenada(coord) and \
            coordenada_linha(coord)<tabuleiro_dimensao(tab) and \
            coordenada_coluna(coord)<tabuleiro_dimensao(tab)):
        raise ValueError('tabuleiro_celula: argumentos invalidos')
    return tab.XYZ[1][coordenada_para_str(coord)]
def tabuleiro_substitui_celula(tab, cell, coord):
    if not (eh_tabuleiro(tab) and eh_coordenada(coord) and eh_celula(cell) \
            and coordenada_linha(coord)<tabuleiro_dimensao(tab) \
            and coordenada_coluna(coord)<tabuleiro_dimensao(tab)):
        raise ValueError('tabuleiro_substitui_celula: argumentos invalidos')
    tab.XYZ[1][coordenada_para_str(coord)] = cell
    return tab
def tabuleiro_inverte_estado(tab, coord):
    if not (eh_tabuleiro(tab) and eh_coordenada(coord) and \
            coordenada_linha(coord)<tabuleiro_dimensao(tab) and \
            coordenada_coluna(coord)<tabuleiro_dimensao(tab)):
        raise ValueError('tabuleiro_inverte_estado: argumentos invalidos')
    tab.XYZ[1][coordenada_para_str(coord)] = inverte_estado(tab.XYZ[1][coordenada_para_str(coord)])
    return tab
def tabuleiros_iguais(tab1, tab2):
    return eh_tabuleiro(tab1) and eh_tabuleiro(tab2) and tab1.XYZ==tab2.XYZ
def tabuleiro_para_str(tab):
    return '+-------+\n|...{}...|\n|..{}.{}..|\n|.{}.{}.{}.|\n|..{}.{}..|\n+-------+'\
        .format(celula_para_str(tab.XYZ[1][coordenada_para_str(cria_coordenada(0,2))]),
                celula_para_str(tab.XYZ[1][coordenada_para_str(cria_coordenada(0,1))]),
                celula_para_str(tab.XYZ[1][coordenada_para_str(cria_coordenada(1,2))]),
                celula_para_str(tab.XYZ[1][coordenada_para_str(cria_coordenada(0,0))]),
                celula_para_str(tab.XYZ[1][coordenada_para_str(cria_coordenada(1,1))]),
                celula_para_str(tab.XYZ[1][coordenada_para_str(cria_coordenada(2,2))]),
                celula_para_str(tab.XYZ[1][coordenada_para_str(cria_coordenada(1,0))]),
                celula_para_str(tab.XYZ[1][coordenada_para_str(cria_coordenada(2,1))]))
