# Aprovando ou não um empréstimo

print('-=-' * 15)
print('\033[1;33mFINANCIAMENTO DE CASA\033[m'.center(56))
print('-=-' * 15)
valorcasa = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
ano = int(input('Quantos anos de financiamento? '))

prestacao = valorcasa / (ano * 12)

if prestacao <= sal * 30 / 100: # Limite mensal do comprador
    print('Empréstimo CONCEDIDO. A parcela será de R${:.2f} por mês.'.format(prestacao))
else:
    print('Empréstimo NEGADO. A parcela é de R${:.2f} por mês, excedendo o limite de 30%.'.format(prestacao))
