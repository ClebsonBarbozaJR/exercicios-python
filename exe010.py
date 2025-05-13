#Conversor de moeadas

real = float(input('Quanto dinheiro você tem na carteira? R$'))
print('Com R${:.2f} você consegue comprar U${:.2f}.'.format(real, (real / 5.38)))
print('Com R${:.2f} você consegue comprar {:.2f} euros.'.format(real, (real / 5.76)))

