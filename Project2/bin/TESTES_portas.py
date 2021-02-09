# ########################################################
# ################################################# TESTES

## Preparation
try:
    t0a = tabuleiro_inicial()
except:
    print('PORTAS Preparation A --> FAIL')

try:
    cad = '((-1, -1, -1), (0, 0, -1), (0, -1))'
    t0b = str_para_tabuleiro(cad)
except:
    print('PORTAS Preparation B --> FAIL')


points = 0

# Teste 1a - porta_x D
try:
    t0 = tabuleiro_inicial()
    t1 = porta_x(t0, "D")
    coord = cria_coordenada(2,1)
    if eh_tabuleiro(t1) and \
       tabuleiro_para_str(t1) == '+-------+\n|...x...|\n|..x.x..|\n|.x.1.x.|\n|..0.1..|\n+-------+' and \
       obter_valor(tabuleiro_celula(t1, coord)) == 1:
        print('PORTAS Teste 1a --> OK')
        points += 1
    else:
        print('PORTAS Teste 1a --> FAIL')
except:
    print('PORTAS Teste 1a --> FAIL')
    
# Teste 1b - porta_x D
try:
    t0 = str_para_tabuleiro('((-1, -1, -1), (0, 0, -1), (0, -1))')
    t1 = porta_x(t0, "D")
    coord = cria_coordenada(2,1)
    if eh_tabuleiro(t1) and \
       tabuleiro_para_str(t1) == '+-------+\n|...x...|\n|..x.x..|\n|.x.1.x.|\n|..0.1..|\n+-------+' and \
       obter_valor(tabuleiro_celula(t1, coord)) == 1:
        print('PORTAS Teste 1b --> OK')
        points += 1
    else:
        print('PORTAS Teste 1b --> FAIL')
except:
    print('PORTAS Teste 1b --> FAIL')

# Teste 2a - porta_x E
try:
    t0 = tabuleiro_inicial()
    t1 = porta_x(t0, "E")
    coord = cria_coordenada(1,0)
    if eh_tabuleiro(t1) and \
       tabuleiro_para_str(t1) == '+-------+\n|...x...|\n|..x.x..|\n|.x.1.x.|\n|..1.0..|\n+-------+' and \
       obter_valor(tabuleiro_celula(t1, coord)) == 1:
        print('PORTAS Teste 2a --> OK')
        points += 1
    else:
        print('PORTAS Teste 2a --> FAIL')
except:
    print('PORTAS Teste 2a --> FAIL')
    
# Teste 2b - porta_x E
try:
    t0 = str_para_tabuleiro('((-1, -1, -1), (0, 0, -1), (0, -1))')
    t1 = porta_x(t0, "E")
    coord = cria_coordenada(1,0)
    if eh_tabuleiro(t1) and \
       tabuleiro_para_str(t1) == '+-------+\n|...x...|\n|..x.x..|\n|.x.1.x.|\n|..1.0..|\n+-------+' and \
       obter_valor(tabuleiro_celula(t1, coord)) == 1:
        print('PORTAS Teste 2b --> OK')
        points += 1
    else:
        print('PORTAS Teste 2b --> FAIL')
except:
    print('PORTAS Teste 2b --> FAIL')
    


# Teste 3a - porta_z D
try:
    t0 = tabuleiro_inicial()
    t1 = porta_z(t0, "D")
    coord = cria_coordenada(2,1)
    if eh_tabuleiro(t1) and \
       tabuleiro_para_str(t1) == '+-------+\n|...x...|\n|..x.x..|\n|.x.0.x.|\n|..0.0..|\n+-------+' and \
       obter_valor(tabuleiro_celula(t1, coord)) == 0:
        print('PORTAS Teste 3a --> OK')
        points += 1
    else:
        print('PORTAS Teste 3a --> FAIL')
except:
    print('PORTAS Teste 3a --> FAIL')
    
# Teste 3b - porta_z D
try:
    t0 = str_para_tabuleiro('((-1, -1, -1), (0, -1, 0), (-1, 0))')
    t1 = porta_z(t0, "D")
    coord = cria_coordenada(2,2)
    if eh_tabuleiro(t1) and \
       tabuleiro_para_str(t1) == '+-------+\n|...x...|\n|..x.1..|\n|.x.x.1.|\n|..0.x..|\n+-------+' and \
       obter_valor(tabuleiro_celula(t1, coord)) == 1:
        print('PORTAS Teste 3b --> OK')
        points += 1
    else:
        print('PORTAS Teste 3b --> FAIL')
except:
    print('PORTAS Teste 3b --> FAIL')

# Teste 4a - porta_z E
try:
    t0 = tabuleiro_inicial()
    t1 = porta_z(t0, "E")
    coord = cria_coordenada(1,0)
    if eh_tabuleiro(t1) and \
       tabuleiro_para_str(t1) == '+-------+\n|...x...|\n|..x.x..|\n|.x.0.x.|\n|..0.0..|\n+-------+' and \
       obter_valor(tabuleiro_celula(t1, coord)) == 0:
        print('PORTAS Teste 4a --> OK')
        points += 1
    else:
        print('PORTAS Teste 4a --> FAIL')
except:
    print('PORTAS Teste 4a --> FAIL')
    
# Teste 4b - porta_z E
try:
    t0 = str_para_tabuleiro('((0, 0, -1), (-1, -1, -1), (0, -1))')
    t1 = porta_z(t0, "E")
    coord = cria_coordenada(0,0)
    if eh_tabuleiro(t1) and \
       tabuleiro_para_str(t1) == '+-------+\n|...x...|\n|..1.x..|\n|.1.x.x.|\n|..x.0..|\n+-------+' and \
       obter_valor(tabuleiro_celula(t1, coord)) == 1:
        print('PORTAS Teste 4b --> OK')
        points += 1
    else:
        print('PORTAS Teste 4b --> FAIL')
except:
    print('PORTAS Teste 4b --> FAIL')
    


# Teste 5a - porta_h D
try:
    t0 = tabuleiro_inicial()
    t1 = porta_h(t0, "D")
    coord = cria_coordenada(2,2)
    if eh_tabuleiro(t1) and \
       tabuleiro_para_str(t1) == '+-------+\n|...x...|\n|..x.0..|\n|.x.x.0.|\n|..0.x..|\n+-------+' and \
       obter_valor(tabuleiro_celula(t1, coord)) == 0:
        print('PORTAS Teste 5a --> OK')
        points += 1
    else:
        print('PORTAS Teste 5a --> FAIL')
except:
    print('PORTAS Teste 5a --> FAIL')
    
# Teste 5b - porta_h D
try:
    t0 = str_para_tabuleiro('((-1, -1, -1), (0, 0, -1), (0, -1))')
    t1 = porta_h(t0, "D")
    coord = cria_coordenada(2,2)
    if eh_tabuleiro(t1) and \
       tabuleiro_para_str(t1) == '+-------+\n|...x...|\n|..x.0..|\n|.x.x.0.|\n|..0.x..|\n+-------+' and \
       obter_valor(tabuleiro_celula(t1, coord)) == 0:
        print('PORTAS Teste 5b --> OK')
        points += 1
    else:
        print('PORTAS Teste 5b --> FAIL')
except:
    print('PORTAS Teste 5b --> FAIL')

# Teste 6a - porta_h E
try:
    t0 = tabuleiro_inicial()
    t1 = porta_h(t0, "E")
    coord = cria_coordenada(1,0)
    if eh_tabuleiro(t1) and \
       tabuleiro_para_str(t1) == '+-------+\n|...x...|\n|..0.x..|\n|.0.x.x.|\n|..x.0..|\n+-------+' and \
       obter_valor(tabuleiro_celula(t1, coord)) == -1:
        print('PORTAS Teste 6a --> OK')
        points += 1
    else:
        print('PORTAS Teste 6a --> FAIL')
except:
    print('PORTAS Teste 6a --> FAIL')
    
# Teste 6b - porta_h E
try:
    t0 = str_para_tabuleiro('((-1, -1, -1), (0, 0, -1), (0, -1))')
    t1 = porta_h(t0, "E")
    coord = cria_coordenada(0,0)
    if eh_tabuleiro(t1) and \
       tabuleiro_para_str(t1) == '+-------+\n|...x...|\n|..0.x..|\n|.0.x.x.|\n|..x.0..|\n+-------+' and \
       obter_valor(tabuleiro_celula(t1, coord)) == 0:
        print('PORTAS Teste 6b --> OK')
        points += 1
    else:
        print('PORTAS Teste 6b --> FAIL')
except:
    print('PORTAS Teste 6b --> FAIL')
    


val = 2/3
percent = points/12
print ('PORTAS GLOBAL --> {:2.1f} %'.format(100*percent), '({:.3f} val)'.format(val*percent))
