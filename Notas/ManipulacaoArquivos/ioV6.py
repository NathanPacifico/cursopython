# Esse tipo de formação do código, nao precisa ter uma variavel que armazena
# todo o adrquivo CSV, descarregando assim um pouco o processamento do código,
# e fazendo com que a leitura seja em streaming, ou seja, é interpretado linha
# por linha ao inves de ler todo o arquivos, salvar numa variavel e só depois
# tomar decisões/ações


# abre o arquivo csv, atribuindo a ele o nome arquivo. ao final desse bloco,
# o arquivo é automáticamente fechado
with open('pessoasIdades.csv') as arquivo:
    # cria um arquivo txt de nome "pessoas.txt", habilita ele para escrita
    with open('pessoas.txt', 'w') as saida:
        for registro in arquivo:
            # Pega cada linha do arquivo e chama ele internamente como saida
            # a funcao .split() separa cada linha em uma lista, separando pela ','
            # a função .strip() tira espaços vazios no inicio e final de cada
            # string
            print('Nome: {}, Idade: {}'.format(
                *registro.strip().split(',')), file=saida)
if arquivo.closed:
    print('Arquivo fechado!')
