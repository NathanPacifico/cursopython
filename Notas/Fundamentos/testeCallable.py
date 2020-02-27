def funcao(*funcaoChamada, *valores):
    if callable(funcaoChamada):
        funcaoChamada(valores)


def soma(*arg):
    resultado = 0
    for i in range(len(arg)):
        resultado += arg
    print(resultado)


def subtração(*arg):
    resultado = 0
    for i in range(len(arg)):
        resultado -= arg
    print(resultado)


soma(1, 2, 3)
