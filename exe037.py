# Convertendo bases númericas

print('\033[1m-=-\033[m' * 15)
print('\033[36;1mCONVERSOR DE BASES NÚMERICAS\033[m'.center(55))
print('\033[1m-=-\033[m' * 15)
num = int(input('Digite um número: '))
print('''Escolha sua base de conversão: 
\033[33;1m[ 1 ] Binário\033[m
\033[34;1m[ 2 ] Octal\033[m
\033[35;1m[ 3 ] Hexadecimal\033[m''')
base = int(input())
if base == 1:
    print('\033[1m{}\033[m Convertido para \033[1;33mBINÁRIO\033[m é igual a \033[1;32m{}\033[m.'.format(num, bin(num) [2:]))
elif base == 2:
    print('\033[1m{}\033[m Convertido para \033[34;1mOCTAL\033[m é igual a \033[1;32m{}\033[m'.format(num, oct(num) [2:]))
elif base == 3:
    print('\033[1m{}\033[m Convertido para \033[35;1mHEXADECIMAL\033[m é igual a \033[32;1m{}\033[m.'.format(num, hex(num) [2:]))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA\033[m.')