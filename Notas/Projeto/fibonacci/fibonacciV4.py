def fibonacci(limite):
    lista = [0, 1]
    while lista[-1] < limite:
        lista.append(sum([lista[-2], lista[-1]]))
    return lista


if __name__ == '__main__':
    for fib in fibonacci(1000):
        print(fib)
