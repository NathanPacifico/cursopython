from math import pi
import sys

def areaCirculo(raio):
	area = pi*(float(raio)**2)
	print('A area da circunferencia é:' ,area)
	return area


if __name__ == '__main__':
	if len(sys.argv) > 1:
		areaCirculo(sys.argv[1])
		print(f'nome do arquivo: {sys.argv[0]}')
	else:
		areaCirculo(input('Digite a area da circunferencia:'))
