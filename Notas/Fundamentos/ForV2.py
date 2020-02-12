for x in range(1, 11):
    if x % 2 == 0:
        continue  # comando continue cancela o laço de repetição somente nesse momento
    print(x)

for x in range(1, 11):
    if x == 5:
        break  # comando break sai do laço de repetição de vez
    print(x)

print('fim')
