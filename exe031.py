# Calculando o preço de uma viagem
d = float(input('Qual vai ser a distância da sua viagem? '))
if d <= 200:
    print('Sua viagem custará R${:.2f}.'.format(d * 0.50))
else:
   print('Sua viagem é longa. Ela custará R${:.2f}.'.format(d * 0.45))
print('Tenha uma boa viagem!')
