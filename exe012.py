valor_original = float(input('Qual é o preço do produto? R$'))
novo_valor = valor_original - (5 / 100 * valor_original)
print('O produto que custava R${}, com o desconto de 5%, o valor custará R${:.2f}.'.format(valor_original,novo_valor))
