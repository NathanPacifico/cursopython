def fibonacci(quantidadeDeNumeros, lista=(0, 1)):
    if len(lista) > quantidadeDeNumeros:
        return lista
    return fibonacci(quantidadeDeNumeros, lista + (sum(lista[-2:]),))


if __name__ == '__main__':
    for fib in fibonacci(10):
        print(fib)
