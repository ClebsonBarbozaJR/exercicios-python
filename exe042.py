# Analisando triângulos 2.0

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('\033[32;1mEsses segmentos PODEM formar um triângulo\033[m ', end='')
    if a == b == c:
        print('\033[33;1mEQUILÁTERO\033[m.')
    elif a == b or a == c or b == c:
        print('\033[33;1mISÓSCELES\033[m.')
    else:
        print('\033[1;33mESCALENO\033[m.')
else:
    print('\033[31;1mEsses segmentos NÃO PODEM formar um triângulo\033[m.')