# Exemplo do for

palavra = 'Nathan'

for letra in (palavra):
    print(letra)

for letra in (palavra):
    # end altera o padrão do print, que geralmente é acrescentar uma nova linha no final(end='\n')
    print(letra, end='')
print('continua na mesma linha')
print('continua normalmente denovo')
