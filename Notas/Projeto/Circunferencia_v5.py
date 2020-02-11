#! python
from math import pi
import sys

def areaCirculo(raio):
	area = pi*(float(raio)**2)
	print('A area da circunferencia é:' ,area)
	return area


if __name__ == '__main__':
	raio = sys.argv[1]
	areaCirculo(raio)
