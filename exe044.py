# Gerenciando um pagamento

compra = float(input('Digite o valor das total de sua compra: R$'))
print('''MÉTODOS DE PAGAMENTO:  
Digite [1] para pagamento a vista/cheque (10% off)
Digite [2] para pagamento a vista com cartão (5% off)
Digite [3] para pagamento no cartão em até 2x
Digite [4] para pagamento no cartão em até 3x ou mais (20% de juros)''')
metodo = int(input())
if metodo == 1:
    print('Com 10% de desconto, sua compra custará R${:.2f}.'.format(compra - (compra / 100 * 10)))
elif metodo == 2:
    print('Com 5% de desconto, sua compra custará R${:.2f}.'.format(compra - (compra / 100 * 5)))
elif metodo == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} sem juros. '.format(compra / 2), end='')
    print('O preço continuará sendo R${:.2f}.'.format(compra))
elif metodo == 4:
    parcela = int(input('Quantas parcelas? '))
    if parcela >= 3:
        print('Sua compra será parcelada em {}x de R${:.2f} com 20% de juros '.format(parcela, (compra * 0.20 * parcela) / parcela), end='')
        print('e ela custará R${:.2f} no final.'.format(compra * 0.20 * parcela))
    else:
        print('Valor inválido. Use a opção [3].')
else:
    print('Opção inválida.')

