if __name__ == '__main__':
    nota = input('Digite a nota do aluno: ')
    # if nota.isnumeric():
    nota = float(nota)
    if nota > 10:
        print('Valor inválido!')
    elif nota > 9.0:
        print('A')
    elif nota > 8.0:
        print('A-')
    elif nota > 7.0:
        print('B')
    elif nota > 6.0:
        print('B-')
    elif nota > 5.0:
        print('C')
    elif nota > 4.0:
        print('C-')
    elif nota > 3.0:
        print('D')
    elif nota > 2.0:
        print('D-')
    elif nota > 1.0:
        print('E')
    elif nota > 0.0:
        print('E-')
    else:
        print('Valor inválido!')
  #  else:
   #     print('O valor deve ser numérico!')
