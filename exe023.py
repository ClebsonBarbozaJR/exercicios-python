num = int(input('Digite um número: '))
print('Analisando o seu número {}...'.format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A unidade é {}\nA dezena é {}\nA centena é {}\nO milhar é {}'.format(u, d, c, m))

