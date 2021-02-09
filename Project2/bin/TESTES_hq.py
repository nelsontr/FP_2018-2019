# ########################################################
# ################################################# TESTES

points = 0

import sys

class TeeC2R4tP6YUgipw5ku(object):
    def __init__(self, input_handle):
        self.input = input_handle.split('\n')
        self.line = 0

    def readline(self):
        if len(self.input) == self.line:
            return ''
        result = self.input[self.line]
        self.line += 1
        return result


def teste_hq_C2R4tP6YUgipw5ku(string_entrada, input_jogo):
    # string_entrada = '((0,-1,0),(-1,-1,-1),(-1,0)):2'
    # input_jogo = 'H\nE\nH\nD'

    oldstdin = sys.stdin
    sys.stdin = TeeC2R4tP6YUgipw5ku(input_handle=input_jogo)
    try:
        hello_quantum(string_entrada)
    except ValueError as e:
        sys.stdin = oldstdin
        raise e
    sys.stdin = oldstdin

############################### Redirect stdout ### BEGIN
import sys
class ListStream:
    def __init__(self):
        self.data = []
    def write(self, s):
        self.data.append(s)
    def flush(self):
        pass

############################### Redirect stdout ### END
try:
    sys.stdout = x = ListStream()
    teste_hq_C2R4tP6YUgipw5ku('((0,-1,0),(-1,-1,-1),(-1,0)):2','H\nE\nH\nD')
    sys.stdout = sys.__stdout__
    res = ''.join(x.data)
    expected = 'Bem-vindo ao Hello Quantum!\n\
O seu objetivo e chegar ao tabuleiro:\n\
+-------+\n\
|...0...|\n\
|..x.x..|\n\
|.0.x.0.|\n\
|..x.x..|\n\
+-------+\n\
Comecando com o tabuleiro que se segue:\n\
+-------+\n\
|...x...|\n\
|..x.x..|\n\
|.x.0.x.|\n\
|..0.0..|\n\
+-------+\n\
Escolha uma porta para aplicar (X, Z ou H): Escolha um qubit para analisar (E ou D): +-------+\n\
|...x...|\n\
|..0.x..|\n\
|.0.x.x.|\n\
|..x.0..|\n\
+-------+\n\
Escolha uma porta para aplicar (X, Z ou H): Escolha um qubit para analisar (E ou D): +-------+\n\
|...0...|\n\
|..x.x..|\n\
|.0.x.0.|\n\
|..x.x..|\n\
+-------+\n\
Parabens, conseguiu converter o tabuleiro em 2 jogadas!\n'

    if(res==expected):
        print('HELLO_QUANTUM Teste 1 --> OK')
        points += 1
    else:
        print('HELLO_QUANTUM Teste 1 --> FAIL')
except:
    print('HELLO_QUANTUM Teste 1 --> FAIL')

try:
    sys.stdout = x = ListStream()
    teste_hq_C2R4tP6YUgipw5ku('((0,-1,0),(-1,-1,-1),(-1,0)):1','H\nE\nH\nD')
    sys.stdout = sys.__stdout__
    res = ''.join(x.data)
    expected = 'Bem-vindo ao Hello Quantum!\n\
O seu objetivo e chegar ao tabuleiro:\n\
+-------+\n\
|...0...|\n\
|..x.x..|\n\
|.0.x.0.|\n\
|..x.x..|\n\
+-------+\n\
Comecando com o tabuleiro que se segue:\n\
+-------+\n\
|...x...|\n\
|..x.x..|\n\
|.x.0.x.|\n\
|..0.0..|\n\
+-------+\n\
Escolha uma porta para aplicar (X, Z ou H): Escolha um qubit para analisar (E ou D): +-------+\n\
|...x...|\n\
|..0.x..|\n\
|.0.x.x.|\n\
|..x.0..|\n\
+-------+\n'

    if(res==expected):
        print('HELLO_QUANTUM Teste 2 --> OK')
        points += 1
    else:
        print('HELLO_QUANTUM Teste 2 --> FAIL')
except:
    print('HELLO_QUANTUM Teste 2 --> FAIL')


val = 0.25
percent = points/2
print ('HELLO_QUANTUM GLOBAL --> {:2.1f} %'.format(100*percent), '({:.3f} val)'.format(val*percent))


