# Aumento de um salário de um funcionário

sal = float(input('Qual é o salário do funcionário? R$'))
print('Quem recebia R${:.2f},'.format(sal))
if sal > 1250:
    print('com 10% de aumento, passa a receber R${:.2f}.'.format(sal + (10 / 100 * sal)))
if sal <= 1250:
    print('com 15% de aumento, passa a receber R${:.2f}.'.format(sal + (15 / 100 * sal)))
