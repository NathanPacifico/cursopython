arquivo = open('pessoasIdades.csv')
texto = arquivo.read()
arquivo.close()

for registro in texto.splitlines():  # separa o arquivo por linhas
    # separa cada linha em uma lista, separando pela ','
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))
