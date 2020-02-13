# Esse tipo de formação do código, nao precisa ter uma variael que armazena
# todo o adrquivo CSV, descarregando assim um pouco o processamento do código,
# e fazendo com que a leitura seja em streaming, ou seja, é interpretado linha
# por linha ao inves de ler todo o arquivos, salvar numa variavel e só depois
# tomar decisões/ações


arquivo = open('pessoasIdades.csv')
for registro in arquivo:  # Pega cada linha do arquivo
    # a funcao .split() separa cada linha em uma lista, separando pela ','
    # a função .strip() tira os espaços vazios no inicio e final de cada string
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
arquivo.close()
