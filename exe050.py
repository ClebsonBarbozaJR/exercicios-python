# Somando 6 números PARES, se for ÍMPAR, ele é ignorado
soma = 0
cont = 0
for i in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(i)))
    if num % 2 == 0: # Se o número do usuário for par
        soma += num # A soma será feita
        cont += 1 # E ele será contado
print('Você informou {} números PARES. A soma deles é igual a {}.'.format(cont, soma))