def fibonacci(quantidadeDeNumeros):
    lista = [0, 1]
    while len(lista) < quantidadeDeNumeros:
        lista.append(sum(lista[-2:]))
    return lista


if __name__ == '__main__':
    for fib in fibonacci(20):
        print(fib)
