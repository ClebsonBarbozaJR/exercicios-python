# Qual é o maior e menor número

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Os números são \033[1;33m{}\033[m, \033[1;33m{}\033[m e \033[1;33m{}\033[m.'.format(n1, n2, n3))
print('O maior é \033[1;32m{}\033[m e o menor é \033[1;31m{}\033[m.'.format(maior, menor))