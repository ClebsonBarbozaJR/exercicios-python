# Segmentos de um triângulos

print('-=-' * 20)
print('ANALISADOR DE TRIÂNGULOS'.center(55))
print('-=-' * 20)
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceito segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Esses segmentos FORMAM um triângulo.')
else:
    print('Esses segmentos NÃO FORMAM um triângulo.')