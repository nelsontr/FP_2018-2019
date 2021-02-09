'''
Instituto Superior Tecnico - Projeto "Hello Quantum Tecnico"
    Nome: Nelson Alexandre Geada Trindade
    Numero: 93743
    Curso/Cadeira: LEIC-T / Fundamentos de Programacao

    Observacoes sobre projeto:
        Todas as funcoes adicionais, foram criadas para simplificar o codigo das funcoes principais e para tornar o algoritmo mais eficiente.
        Durante as diversas funcoes, havera variaveis com nomes iguais em diferentes funcoes, de modo a ser mais facil a coompreensao de outro
        programador. Para substituir um elemento do tuplo por outro, vou recorrer algumas vezes ao comando:
            tuplo = tuplo[:i] + (a,) + tuplo[i+1:], onde (i) e o elemento do tuplo que pretendo substituir pelo elemento (a).
'''

#:::::::::::::::::::::::: Funcoes Auxiliar ::::::::::::::::::::::::

def mudanca_elemento(tuplo):
    '''
    #   Funcao - mudanca_elemento: tabuleiro -> tabuleiro/booleano
    #   Objetivo: Se os elementos do tuplo forem do conjunto (-1,0,1), entao se for '-1' o elemento vai ser substituido
            por 'x' e os outros elementos pela string do elemento. Senao da return False.
    '''
    ntuplo = ()
    for i in range(3):
        for e in tuplo[i]:          #Percorre os elementos (e) do subtuplo i (tuplo[i]) do tuplo principal
            if e == -1:
                ntuplo += ('x',)
            elif e in (0,1):
                ntuplo += (str(e),)
            else:
                return False        #Para a funcao eh_tabuleiro, se der False diz a funcao que o tuplo nao e valido
    return ntuplo                   #Da return de um tuplo sem subtuplos e com os elementos todos em string. Na funcao eh_tabuleiro, dara True

def repete(tuplo,lado,a,b):
    '''
    #   Funcao - repete: tabuleiro x {"E", "D"} x inteiro x inteiro -> tabuleiro
    #   Objetivo: Como as portas x e z tem o mesmo ciclo 'for' mas com diferentes valores, basta uma funcao que ao receber a e b,
            dao um tuplo em que tem os valores alterados. Se for 1 troca para 0 e vice-versa.
    '''
    ntuplo = tuplo[0]+tuplo[1]+tuplo[2]
    if lado == 'E':
        for i in range(3):
            if ntuplo[a+i] == 0:
                ntuplo = ntuplo[:a+i] + (1,) + ntuplo[a+i+1:]
            elif ntuplo[a+i] == 1:
                ntuplo = ntuplo[:a+i] + (0,) + ntuplo[a+i+1:]
    elif lado == 'D':
        for elemento in (b+1,b+4,b+6):
            if ntuplo[elemento] == 0:
                ntuplo = ntuplo[:elemento] + (1,) + ntuplo[elemento+1:]
            elif ntuplo[elemento] == 1:
                ntuplo = ntuplo[:elemento] + (0,) + ntuplo[elemento+1:]
    return (ntuplo[:3],ntuplo[3:6],ntuplo[6:])

#:::::::::::::::::::::::: Codigo Principal ::::::::::::::::::::::::

def eh_tabuleiro(tuplo):
    '''
    #   Funcao - eh_tabuleiro: universal -> booleano
    #   Objetivo: Verificar se o tuplo digitado e do formato pretendido - ((a,b,c),(d,e,f),(g,h)). Se for, vai dar True, caso contrario False
            (Em ambos os casos, da return de Booleano).
    '''
    if isinstance(tuplo,tuple) and len(tuplo)==3:
        if type(tuplo[0])==type(tuplo[1])==type(tuplo[2])==tuple and len(tuplo[0])==len(tuplo[1])==(len(tuplo[2])+1)==3:
            if not(mudanca_elemento(tuplo)):
                return False
            return True
    return False

def tabuleiro_str(tuplo_original):
    '''
    #   Funcao - tabuleiro_str: tabuleiro -> cad. caracteres
    #   Objetivo: Apos a validacao do argumento (eh_tabuleiro == True), entao vamos com a funcao auxiliar (mudanca_elemento) mudar todos os elementos
            do tuplo e converte-los para string de modo a obter um return com uma cadeia de caracteres.
    '''
    if not(eh_tabuleiro(tuplo_original)):
        raise ValueError('tabuleiro_str: argumento invalido')
    ntuplo=mudanca_elemento(tuplo_original)
    return '+-------+\n|...'+ntuplo[2]+'...|\n|..'+ntuplo[1]+'.'+ntuplo[5]+'..|\n|.'+ntuplo[0]+'.'+ntuplo[4]+'.'+ntuplo[7]+'.|\n|..'+ntuplo[3]+'.'+ntuplo[6]+'..|\n+-------+'

def tabuleiros_iguais(tuplo_1,tuplo_2):
    '''
    #   Funcao - tabuleiros_iguais: tabuleiro x tabuleiro -> booleano
    #   Objetivo: Apos a verificacao dos dois tabuleiros introduzidos (atraves da funcao eh_tabuleiro) da return a condicao tabuleiro1 == tabuleiro2.
    '''
    if not(eh_tabuleiro(tuplo_1)) or not(eh_tabuleiro(tuplo_2)):
        raise ValueError('tabuleiros_iguais: um dos argumentos nao e tabuleiro')
    return tuplo_1 == tuplo_2

def porta_x(tuplo_original,lado):
    '''
    #   Funcao -  porta_x: tabuleiro x {"E", "D"} -> tabuleiro
    #   Objetivo: Apos a verificacao do tabuleiro (atraves da funcao eh_tabuleiro) e verificar se a segunda variavel e string e que so pode ser E e D,
            chama a funcao repete(), com a=3,b=0.
    '''
    if eh_tabuleiro(tuplo_original) and isinstance(lado,str) and (lado in ('E','D')):
        return repete(tuplo_original,lado,3,0)
    raise ValueError('porta_x: um dos argumentos e invalido')

def porta_z(tuplo_original,lado):
    '''
    #   Funcao - porta_z: tabuleiro x {"E", "D"} -> tabuleiro
    #   Objetivo: Apos a verificacao do tabuleiro (atraves da funcao eh_tabuleiro) e verificar se a segunda variavel e string e que so pode ser E e D,
            chama a funcao repete(), com a=0,b=1.
    '''
    if eh_tabuleiro(tuplo_original) and isinstance(lado,str) and (lado in ('E','D')):
        return repete(tuplo_original,lado,0,1)
    raise ValueError('porta_z: um dos argumentos e invalido')

def porta_h(tuplo,lado):
    '''
    #   Funcao - porta_h: tabuleiro x {"E", "D"} -> tabuleiro
    #   Objetivo: Apos a verificacao do tabuleiro (atraves da funcao eh_tabuleiro) e verificar se a segunda variavel e string e que so pode ser E e D,
            dara um tuplo alterado.
    '''
    if eh_tabuleiro(tuplo) and isinstance(lado,str) and (lado in ('E','D')):
        ntuplo = tuplo[0]+tuplo[1]+tuplo[2]
        if lado == 'E':
            for e in range(3):
                auxiliar = ntuplo[e+3]                                #Vai guardar o valor de ntuplo[e+3]
                ntuplo = ntuplo[:e+3] + (ntuplo[e],) + ntuplo[e+4:]   #Altera o valor de ntuplo[e+3] par o valor de ntuplo[e]
                ntuplo = ntuplo[:e] + (auxiliar,) + ntuplo[e+1:]      #Altera o valor de ntuplo[e] por auxiliar
        elif lado == 'D':
            for e in (1,4,6):
                auxiliar = ntuplo[e+1]                                #Vai guardar o valor de ntuplo[e+1]
                ntuplo = ntuplo[:e+1] + (ntuplo[e],) + ntuplo[e+2:]   #Altera o valor de ntuplo[e+1] par o valor de ntuplo[e]
                ntuplo = ntuplo[:e] + (auxiliar,) + ntuplo[e+1:]      #Altera o valor de ntuplo[e] por auxiliar
        return (ntuplo[:3],ntuplo[3:6],ntuplo[6:])
    raise ValueError('porta_h: um dos argumentos e invalido')
