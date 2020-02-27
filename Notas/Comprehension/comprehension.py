def verificaDia(dia):
    dicionario = {i: 'Dia de semana' if 2 <= i <=
                  6 else 'Fim de semana' for i in range(1, 8)}
    print(dicionario)


verificaDia(1)
