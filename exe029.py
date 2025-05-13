# Multa ao passar o limite de velocidade
print('---' * 20)
print('LIMITE DE VELOCIDADE = 80KM/H')
print('---' * 20)
vel = float(input('Qual a velocidade atual do seu carro? '))
if vel > 80: # Se a velocidade for maior que 80...
    print('Limite de velocidade excedido. Você foi multado em R${:.2f}.'.format((vel-80)*7.00)) # Exibe uma mensagem junto com o valor da multa.
print("Dirija com segurança!")