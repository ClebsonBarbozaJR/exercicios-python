# Analisando o maior e o menor peso de 5 pessoas
maior = 0
menor = 0
for i in range(1, 5+1):
    peso = float(input('Peso da {}º pessoa: '.format(i)))
    if i == 1:
        maior = peso
        menor = peso
    elif peso > maior:  #
        maior = peso    # Essa parte faz a análise dos pesos das outras pessoas
    elif peso < menor:  #
        menor = peso    #
print('Maior peso lido: {}.'.format(maior))
print('Menor peso lido: {}.'.format(menor))
