# Somando números ímpares se eles forem múltiplos de 3
soma = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0: # Se for múltiplo de 3
        cont += 1 # contador de múltiplos de 3
        soma += i # somando os múltiplos de 3
print('A soma dos {} números ímpares múltiplos de 3 é {}.'.format(cont, soma))
