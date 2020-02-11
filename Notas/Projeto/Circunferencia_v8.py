from math import pi
import sys


class cores:
    Vermelho = '\033[31m'
    Preto = '\033[30m'
    Verde = '\033[32m'
    Branco = '\033[0m'


def areaCirculo(raio):
    area = pi*(float(raio)**2)
    print('A area da circunferencia é:', area)
    return area


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if not sys.argv[1].isnumeric():
            print(cores.Vermelho + 'Digite um valor numerico!' + cores.Branco)
        else:
            areaCirculo(sys.argv[1])
            print(f'nome do arquivo: {sys.argv[0]}')

    else:
        areaCirculo(input('Digite a area da circunferencia:'))
