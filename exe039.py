# Alistamento Militar

from datetime import date

nasc = int(input('Qual seu ano de nascimento? '))
idade = date.today().year - nasc
print('Sua idade é de {} anos.'.format(idade))
if idade < 18:
    print('Você ainda não está no período de alistamento. Restam {} anos.'.format(18 - idade))
    print('Você irá se alistar em {}.'.format(date.today().year + (18 - idade)))
elif idade == 18:
    print('Você já está no período de alistamento. CORRE!')
else:
    print('Você passou {} anos do período de alistamento.'.format(idade - 18))
    print('Você era para ter se alistado em {}.'.format(date.today().year - (idade - 18)))