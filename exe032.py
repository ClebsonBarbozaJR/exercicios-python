# Esse ano é bissexto?
from datetime import date

print('\033[1;33m-=-\033[m' * 20)
print('\033[1mANALISADOR DE ANOS BISSEXTOS\033[m'.center(56))
print('\033[1;33m-=-\033[m' * 20)

ano = int(input('Digite um ano qualquer ou pressione 0 para verificar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {}\033[32;1m É BISSEXTO\033[m.'.format(ano))
else:
    print('0 ano de {} \033[1;31mNÃO É BISSEXTO\033[m.'.format(ano))



