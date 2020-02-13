import csv

with open('desafio-ibge.csv') as entrada:
    for linha in csv.reader(entrada):
        print(f'{linha[8]}: {linha[3]}')
