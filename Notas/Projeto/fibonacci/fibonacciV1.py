def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f'{penultimo}, {ultimo}', end=(', '))
    proximo = penultimo+ultimo

    while proximo < limite:
        print(f'{proximo}', end=(', '))
        penultimo = ultimo
        ultimo = proximo
        proximo = penultimo+ultimo


if __name__ == '__main__':
    fibonacci(10000)
