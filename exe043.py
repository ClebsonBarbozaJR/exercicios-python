# Cálculo de IMC

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))
imc = peso / altura ** 2
print('Seu IMC é de {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO.')
elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA.')