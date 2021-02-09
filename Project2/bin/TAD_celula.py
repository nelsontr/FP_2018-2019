# TAD celula -------------------------------------------------------------------
def cria_celula(val):
    if not(isinstance(val, int) and val in (-1,0,1)):
        raise ValueError('cria_celula: argumento invalido')
    return [{'j': val},'bla']
def obter_valor(cell):
    return cell[0]['j']
def inverte_estado(cell):
    cell[0]['j']=cell[0]['j'] if cell[0]['j']<0 else 1 - cell[0]['j']
    return cell
def eh_celula(univ):
    return isinstance(univ, list) and len(univ)==2 and 'bla'==univ[1] \
            and 'j' in univ[0] and isinstance(obter_valor(univ), int) \
            and obter_valor(univ) in (-1,0,1)
def celulas_iguais(cell1, cell2):
    return eh_celula(cell1) and eh_celula(cell2) and cell1==cell2
def celula_para_str(cell):
    return 'x' if obter_valor(cell)==-1 else str(obter_valor(cell))
