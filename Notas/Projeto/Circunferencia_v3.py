#! python
from math import pi


def areaCirculo(raio):
	area = pi*(float(raio)**2)
	print('A area da circunferencia é:' ,area)
	return area


if __name__ == '__main__':
	raio = input('Digite o raio desejado:')
	areaCirculo(raio)
