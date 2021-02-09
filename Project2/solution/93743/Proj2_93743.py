'''
Instituto Superior Tecnico - Projeto 2 ("Hello Quantum Tecnico")
    Nome: Nelson Alexandre Geada Trindade
    Numero: 93743
    Curso/Cadeira: LEIC-T / Fundamentos de Programacao
'''
#:::::::::::::::::::::::::: Funcoes AUX :::::::::::::::::::::::::::::::#
def linha_coluna_para_str(linha,coluna):
    '''
    linha_coluna_para_str: inteiro x inteiro -> cad.caracteres
    funcao que devolve uma cad. caracteres da coordenada correspondente a linha introduzida e
        coluna introduzida
    '''
    return coordenada_para_str(cria_coordenada(linha,coluna))

def eh_tabuleiro_tuplo(tup):
    '''
    eh_tabuleiro_tuplo: tuplo -> logico
    funcao que devolve verdadeiro apenas se o argumento for um tuplo capaz de ser
        traduzido num tabuleiro
    '''
    return type(tup)==tuple and len(tup)==3 and all(type(e)==tuple for e in tup) and \
            all(len(tup[i])==2 if i==2 else len(tup[i])==3 for i in range(3)) and \
            all((n in (0, 1, -1) for sub in tup for n in sub))

def cria_tabuleiro(tup):
    '''
    cria_tabuleiro: tuplo -> tabuleiro
    funcao que devolve um tabuleiro a partir de um tuplo ja verificado pela
        funcao eh_tabuleiro_tuplo
    '''
    tab=dict(((linha_coluna_para_str(linha,coluna),cria_celula(tup[linha][coluna]))\
        for linha in range(3) for coluna in range(len(tup[linha]))))
    tab[linha_coluna_para_str(2, 2)]=tab[linha_coluna_para_str(2, 1)]
    tab[linha_coluna_para_str(2, 1)]=tab[linha_coluna_para_str(2, 0)]
    tab.pop(linha_coluna_para_str(2, 0))    #Elimina a coordenada (2, 0)
    return tab

def ciclo_escolhas(tabuleiro_jogo,JOGADAS_MAX,jogadas=0):
    '''
    ciclo_escolhas: tabuleiro x inteiro x inteiro -> tabuleiro x int
    funcao que devolve um tabuleiro e o numero de jogadas apos o ciclo de escolhas para a funcao
        hello_quantum()
    '''
    while jogadas!=JOGADAS_MAX:
        porta = input('Escolha uma porta para aplicar (X, Z ou H): ')
        lado = input('Escolha um qubit para analisar (E ou D): ')
        tabuleiro_jogo = porta_x(tabuleiro_jogo,lado) if porta=='X'\
            else porta_z(tabuleiro_jogo,lado) if porta=='Z' else porta_h(tabuleiro_jogo,lado)
        print(tabuleiro_para_str(tabuleiro_jogo))
        jogadas+=1
    return tabuleiro_jogo,jogadas


#:::::::::::::::::::::::::: CODIGO PRINCIPAL :::::::::::::::::::::::::::#
#::::::::::::::::::::::::::::::: CELULAS :::::::::::::::::::::::::::::::#
def cria_celula(valor_qubit):
    '''
    cria_celula: {1,0,-1} -> celula
    funcao que devolve uma celula, a partir de um valor de qubit (entre 1,0,-1)
    '''
    if valor_qubit not in (1,0,-1):
        raise ValueError('cria_celula: argumento invalido.')
    return ['ativo'] if valor_qubit==1 else ['inativo'] if valor_qubit==0 else ['incerto']

def obter_valor(celula):
    '''
    obter_valor: celula -> {1,0,-1}
    funcao que devolve um valor de qubit (entre 1,0,-1), a partir de uma celula
    '''
    return 1 if celula==cria_celula(1) else 0 if celula==cria_celula(0) else -1

def inverte_estado(celula):
    '''
    inverte_estado: celula -> celula
    funcao que devolve uma celula resultante de inverter o estado dessa celula
    '''
    celula[0] = cria_celula(0)[0] if celula==cria_celula(1) else cria_celula(1)[0]\
        if celula==cria_celula(0) else cria_celula(-1)[0]
    return celula

def eh_celula(arg):
    '''
    eh_celula: universal -> logico
    funcao que devolve verdadeiro apenas se o argumento for do tipo celula
    '''
    return arg in [cria_celula(qubit) for qubit in (-1,0,1)]

def celulas_iguais(c1,c2):
    '''
    celulas_iguais: celula x celula -> logico
    funcao que devolve verdadeiro apenas se o valor da celula-1 for igual ao valor da celula-2
    '''
    return eh_celula(c1) and eh_celula(c2) and obter_valor(c1)==obter_valor(c2)

def celula_para_str(celula):
    '''
    celula_para_str: celula -> cad.caracteres
    funcao que devolve uma cad.caracteres com o valor da celula introduzida como argumento
    '''
    return str(obter_valor(celula)) if celula in (cria_celula(1),cria_celula(0)) else 'x'


#::::::::::::::::::::::::::::: COORDENADAS :::::::::::::::::::::::::::::#
def cria_coordenada(linha,coluna):
    '''
    cria_coordenada: inteiro x inteiro -> coordenada
    funcao que devolve uma coordenada a partir de dois inteiros que irao funcionar como
        linha e coluna
    '''
    if not (type(linha)==type(coluna)==int and 0<=linha<=2 and 0<=coluna<=2):
        raise ValueError('cria_coordenada: argumentos invalidos.')
    return (linha,coluna)

def coordenada_linha(coordenada):
    '''
    coordenada_linha: coordenada -> inteiro
    funcao que devolve um inteiro correspondente a linha da coordenada introduzida como argumento
    '''
    return coordenada[0]

def coordenada_coluna(coordenada):
    '''
    coordenada_coluna: coordenada -> inteiro
    funcao que devolve um inteiro correspondente a coluna da coordenada introduzida como argumento
    '''
    return coordenada[1]

def eh_coordenada(arg):
    '''
    eh_coordenada: universal -> logico
    funcao que devolve verdadeiro apenas se o argumento for do tipo coordenada
    '''
    return arg in [cria_coordenada(linha,coluna) for linha in range(3) for coluna in range(3)]

def coordenadas_iguais(c1,c2):
    '''
    coordenadas_iguais: coordenada x coordenada -> logico
    funcao que devolve verdadeiro apenas se:
     - o valor da linha da coordenada-1 for igual ao valor da linha da coordenada-2
     - o valor da coluna da coordenada-1 for igual ao valor da coluna da coordenada-2
    '''
    return eh_coordenada(c1) and eh_coordenada(c2) and coordenada_linha(c1)==coordenada_linha(c2)\
        and coordenada_coluna(c1)==coordenada_coluna(c2)

def coordenada_para_str(coord):
    '''
    coordenada_para_str: coordenada -> cad.caracteres
    funcao que devolve uma cad.caracteres com a coordenada introduzida como argumento
    '''
    return str(cria_coordenada(coordenada_linha(coord), coordenada_coluna(coord)))


#::::::::::::::::::::::::::::: TABULEIRO :::::::::::::::::::::::::::::#
def tabuleiro_inicial():
    '''
    tabuleiro_inicial: {} -> tabuleiro
    funcao que devolve o tabuleiro inicial do jogo
    '''
    return str_para_tabuleiro('((-1,-1,-1),(0,0,-1),(0,-1))')

def str_para_tabuleiro(cc):
    '''
    str_para_tabuleiro: cad.caracteres -> tabuleiro
    funcao que devolve um tabuleiro com a cad.caracteres introduzida como argumento
    '''
    if not (type(cc)==str and eh_tabuleiro_tuplo(eval(cc))):
        raise ValueError('str_para_tabuleiro: argumento invalido.')
    return cria_tabuleiro(eval(cc))

def tabuleiro_dimensao(tab):
    '''
    tabuleiro_dimensao: tabuleiro -> inteiro
    funcao que devolve o numero de linhas/colunas do tabuleiro
    '''
    return (len(tab.keys())+1)//3
    #Numero de Linhas/Colunas (como excluimos o (2,0), somando assim 1 e dividindo por 3)

def tabuleiro_celula(tab,coor):
    '''
    tabuleiro_celula: tabuleiro x coordenada -> celula
    funcao que devolve a celula presente na coordenada introduzida do tabuleiro introduzido
    '''
    return tab[coordenada_para_str(coor)]

def tabuleiro_substitui_celula(tab,cel,coor):
    '''
    tabuleiro_substitui_celula: tabuleiro x celula x coordenada -> celula
    funcao que devolve o tabuleiro que resulta de substituir a celula existente na coordenada
        introduzida do tabuleiro introduzido pela nova celula.
    '''
    if not (eh_tabuleiro(tab) and eh_celula(cel) and eh_coordenada(coor)):
        raise ValueError('tabuleiro_substitui_celula: argumentos invalidos.')
    tab[coordenada_para_str(coor)]=cel
    return tab

def tabuleiro_inverte_estado(tab,coor):
    '''
    tabuleiro_inverte_estado: tabuleiro x coordenada -> tabuleiro
    funcao que devolve o tabuleiro que resulta de substituir a celula existente na coordenada
        introduzida do tabuleiro introduzido, pela nova celula
    '''
    if not (eh_tabuleiro(tab) and eh_coordenada(coor)):
        raise ValueError('tabuleiro_inverte_estado: argumentos invalidos.')
    tab[coordenada_para_str(coor)]=inverte_estado(tabuleiro_celula(tab,coor))
    return tab

def eh_tabuleiro(arg):
    '''
    eh_tabuleiro: universal -> logico
    funcao que devolve verdadeiro apenas se o argumento for do tipo tabuleiro
    '''
    return type(arg)==dict and all(eh_coordenada(eval(chave)) is True for chave in arg.keys())\
            and all(eh_celula(valores) is True for valores in arg.values())

def tabuleiros_iguais(t1,t2):
    '''
    tabuleiros_iguais: tabuleiro x tabuleiro -> logico
    funcao que devolve verdadeiro apenas se o todas as chaves do tabuleiro-1 forem iguais as
        chaves do tabuleiro-2
    '''
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and all((tabuleiro_celula(t1,(linha,coluna))==\
        tabuleiro_celula(t2,(linha,coluna)) for linha in range(0,3) for coluna in range(0,3)\
        if not (linha==2 and coluna==0)))

def tabuleiro_para_str(tab):
    '''
    tabuleiro_para_str: tabuleiro -> cad.caracteres
    funcao que devolve uma cad.caracteres a partir do tabuleiro introduzido
    '''
    return '+-------+\n|...{2}...|\n|..{1}.{5}..|\n|.{0}.{4}.{7}.|\n|..{3}.{6}..|\n+-------+'\
    .format(*[celula_para_str(tab[linha_coluna_para_str(linha, coluna)]) for linha in range(3)\
            for coluna in range(3) if not(linha==2 and coluna==0)])


#::::::::::::::::::::::::::::: PORTAS :::::::::::::::::::::::::::::#
def porta_x(tab,lado):
    '''
    porta_x: tabuleiro x {'E','D'} -> tabuleiro
    funcao que devolve o tabuleiro resultante de aplicar a porta X a celula inferior do qubit da
        esquerda, ou da direita, conforme seja 'E' ou 'D', respetivamente
    '''
    if not eh_tabuleiro(tab) or lado not in ('E','D'):
        raise ValueError('porta_x: argumentos invalidos.')
    for i in range(3):
        tabuleiro_inverte_estado(tab,cria_coordenada(1,i)) if lado=='E' else\
        tabuleiro_inverte_estado(tab, cria_coordenada(i,1))
    return tab

def porta_z(tab,lado):
    '''
    porta_z: tabuleiro x {'E','D'} -> tabuleiro
    funcao que devolve devolve o tabuleiro resultante de aplicar a porta Z a celula superior
        do qubit da esquerda, ou da direita, conforme seja 'E' ou 'D', respetivamente
    '''
    if not eh_tabuleiro(tab) or lado not in ('E','D'):
        raise ValueError('porta_z: argumentos invalidos.')
    for i in range(3):
        tabuleiro_inverte_estado(tab,cria_coordenada(0,i)) if lado=='E' else\
        tabuleiro_inverte_estado(tab, cria_coordenada(i,2))
    return tab

def porta_h(tab,lado):
    '''
    porta_h: tabuleiro x {'E','D'} -> tabuleiro
    funcao que devolve o tabuleiro resultante de aplicar a porta H ao qubit da esquerda,
        ou da direita, conforme seja 'E' ou 'D', respetivamente
    '''
    if not eh_tabuleiro(tab) or lado not in ('E','D'):
        raise ValueError('porta_h: argumentos invalidos.')
    for i in range(3):
        if lado=='E':
            lista_aux=tabuleiro_celula(tab,cria_coordenada(0,i))
            tabuleiro_substitui_celula(tab,tabuleiro_celula(tab,(1,i)),cria_coordenada(0,i))
            tabuleiro_substitui_celula(tab,lista_aux,cria_coordenada(1,i))
        else:
            lista_aux=tabuleiro_celula(tab,cria_coordenada(i,2))
            tabuleiro_substitui_celula(tab,tabuleiro_celula(tab,(i,1)),cria_coordenada(i,2))
            tabuleiro_substitui_celula(tab,lista_aux,cria_coordenada(i,1))
    return tab


#::::::::::::::::::::::::::: HELLO_QUANTUM :::::::::::::::::::::::::::#
def hello_quantum(cc):
    '''
    hello_quantum: cad.caracteres -> logico
    funcao que recebe uma cadeia de caracteres contendo a descricao do tabuleiro objetivo e do
        numero maximo de jogadas. A funcao devolve verdadeiro se o jogador conseguir transformar
        o tabuleiro inicial no tabuleiro objetivo, nao ultrapassando o numero de jogadas indicado
        e devolve falso em caso contrario
    '''
    tabuleiro_jogo , tabuleiro_final = tabuleiro_inicial() , str_para_tabuleiro(cc.split(':')[0])
    jogadas , JOGADAS_MAX = 0 , eval(cc.split(':')[1])
    print('Bem-vindo ao Hello Quantum!\nO seu objetivo e chegar ao tabuleiro:\n'+\
            tabuleiro_para_str(tabuleiro_final)+'\nComecando com o tabuleiro que se segue:\n'+\
            tabuleiro_para_str(tabuleiro_jogo))
    tabuleiro_jogo,jogadas=ciclo_escolhas(tabuleiro_jogo,JOGADAS_MAX)
    if tabuleiros_iguais(tabuleiro_jogo,tabuleiro_final):
        print('Parabens, conseguiu converter o tabuleiro em {} jogadas!'.format(jogadas))
    return tabuleiros_iguais(tabuleiro_jogo,tabuleiro_final)
