# Categoria de um atleta

from datetime import date

nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - nasc
print('Ele tem {} anos de idade.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif idade <= 14:
    print('Sua categoria é INFANTIL.')
elif idade <= 19:
    print('Sua categoria é JUNIOR.')
elif idade <= 25:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categoria é MASTER.')