def funcao(funcaoChamada, valores):
    for funcao in funcaoChamada:
        if callable(funcao):
            funcao(*valores)
 
 
def soma(*args):
    resultado = 0
    for arg in args:
        resultado += arg
    print(resultado)
 
 
def subtracao(*args):
    resultado = 0
    for arg in args:
        resultado -= arg
    print(resultado)
 
 
funcao(funcaoChamada=(soma, subtracao), valores=(1, 2, 3))
