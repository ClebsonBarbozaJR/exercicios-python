# É par ou ímpar?
n = int(input('Digite um número: '))
if n % 2 == 0: # Se o número for divisível por 2, isto é, tem resto 0...
    print('O número {} é par.'.format(n))
else:
    print('O número {} é ímpar.'.format(n))