# ########################################################
# ################################################# TESTES

## Preparation
try:
    t0a = tabuleiro_inicial()
except:
    print('TABULEIRO Preparation A --> FAIL')

try:
    cad = '((-1, -1, -1), (0, 0, -1), (0, -1))'
    t0b = str_para_tabuleiro(cad)
except:
    print('TABULEIRO Preparation B --> FAIL')


points = 0

# Teste 1a - Reconhecedores
try:
    if eh_tabuleiro(t0a):  
        print('TABULEIRO Teste 1a --> OK')
        points += 1
    else:
        print('TABULEIRO Teste 1a --> FAIL')
except:
    print('TABULEIRO Teste 1a --> FAIL')
    
# Teste 1b - Reconhecedores
try:
    if eh_tabuleiro(t0b):  
        print('TABULEIRO Teste 1b --> OK')
        points += 1
    else:
        print('TABULEIRO Teste 1b --> FAIL')
except:
    print('TABULEIRO Teste 1b --> FAIL')
    

# Teste 2a - tabuleiro_celula
try:
    coord = cria_coordenada(0,0)
    cel = cria_celula(-1)

    if celulas_iguais(tabuleiro_celula(t0a, coord), cel):
        print('TABULEIRO Teste 2a --> OK')
        points += 1
    else:
        print('TABULEIRO Teste 2a --> FAIL')
except:
    print('TABULEIRO Teste 2a --> FAIL')


# Teste 2b - tabuleiro_celula
try:
    coord = cria_coordenada(0,0)
    cell = cria_celula(-1)

    if celulas_iguais(tabuleiro_celula(t0b, coord), cell):
        print('TABULEIRO Teste 2b --> OK')
        points += 1
    else:
        print('TABULEIRO Teste 2b --> FAIL')
except:
    print('TABULEIRO Teste 2b --> FAIL')

# Teste 3a - tabuleiro subsitui celula
try:
    coord = cria_coordenada(0,0)
    cell = cria_celula(1)
    
    t1 = tabuleiro_substitui_celula(t0a, cell, coord)

    if celulas_iguais(tabuleiro_celula(t1, coord), cell):
        print('TABULEIRO Teste 3a --> OK')
        points += 1
    else:
        print('TABULEIRO Teste 3a --> FAIL')
except:
    print('TABULEIRO Teste 3a --> FAIL')


# Teste 3b - tabuleiro subsitui celula
try:

    coord = cria_coordenada(0,0)
    cell = cria_celula(1)
    
    t1 = tabuleiro_substitui_celula(t0b, cell, coord)

    if celulas_iguais(tabuleiro_celula(t1, coord), cell):
        print('TABULEIRO Teste 3b --> OK')
        points += 1
    else:
        print('TABULEIRO Teste 3b --> FAIL')
except:
    print('TABULEIRO Teste 3b --> FAIL')

# Teste 4a - tabuleiro_inverte_estado
try:
    t0a = tabuleiro_inicial() 

    coord = cria_coordenada(1,0)
    cell = cria_celula(1)
    
    t1 = tabuleiro_inverte_estado(t0a, coord)

    if celulas_iguais(tabuleiro_celula(t1, coord), cell):
        print('TABULEIRO Teste 4a --> OK')
        points += 1
    else:
        print('TABULEIRO Teste 4a --> FAIL')
except:
    print('TABULEIRO Teste 4a --> FAIL')


# Teste 4b - tabuleiro_inverte_estado
try:
    cad = '((-1, -1, -1), (0, 0, -1), (0, -1))'
    t0b = str_para_tabuleiro(cad)

    coord = cria_coordenada(1,0)
    cell = cria_celula(1)
    
    t1 = tabuleiro_inverte_estado(t0b, coord)

    if celulas_iguais(tabuleiro_celula(t1, coord), cell):
        print('TABULEIRO Teste 4b --> OK')
        points += 1
    else:
        print('TABULEIRO Teste 4b --> FAIL')
except:
    print('TABULEIRO Teste 4b --> FAIL')


# Teste 5 - tabuleiros_iguais
try:
    t0a = tabuleiro_inicial() 

    cad = '((-1, -1, -1), (0, 0, -1), (0, -1))'
    t0b = str_para_tabuleiro(cad)

    if tabuleiros_iguais(t0a, t0b):
        print('TABULEIRO Teste 5 --> OK')
        points += 1
    else:
        print('TABULEIRO Teste 5 --> FAIL')
except:
    print('TABULEIRO Teste 5 --> FAIL')



# Teste 6a - tabuleiro para string
try:
    if tabuleiro_para_str(tabuleiro_inicial())=='+-------+\n|...x...|\n|..x.x..|\n|.x.0.x.|\n|..0.0..|\n+-------+':
        print('TABULEIRO Teste 6a --> OK')
        points += 1
    else:
        print('TABULEIRO Teste 6a --> FAIL')
except:
    print('TABULEIRO Teste 6a --> FAIL')


# Teste 6b - tabuleiro para string
try:
    cad = '((-1, -1, -1), (0, 0, -1), (0, -1))'
    t0b = str_para_tabuleiro(cad)

    if tabuleiro_para_str(t0b)=='+-------+\n|...x...|\n|..x.x..|\n|.x.0.x.|\n|..0.0..|\n+-------+':
        print('TABULEIRO Teste 6b --> OK')
        points += 1
    else:
        print('TABULEIRO Teste 6b --> FAIL')
except:
    print('TABULEIRO Teste 6b --> FAIL')




val = 0.5
percent = points/11
print ('TABULEIRO GLOBAL --> {:2.1f} %'.format(100*percent), '({:.3f} val)'.format(val*percent))
