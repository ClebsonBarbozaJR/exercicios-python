# Mostrando 10 termos de uma progressão aritimética
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for i in range(1, 11):
    pa = a1 + (i - 1) * r
    print('a{} = {}'.format(i, pa))
print('FIM')