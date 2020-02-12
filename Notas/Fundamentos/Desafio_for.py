from random import randint


def sorteiaNumero():
    numero = randint(0, 6)
    return numero


numeroSorteado = sorteiaNumero()
for x in range(0, 7):
    if x % 2 == 1:
        continue
    elif x == numeroSorteado:
        print('Acertou! Numero = ', numeroSorteado)
        break
else:  # Repare que esse é um else do for, ele só é executado se o for não for
       # interrompido por um comando break
    print('Errou!')
