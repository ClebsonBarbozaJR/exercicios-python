# Detectando um palíndromo
frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}.'.format(junto, inverso))
if junto == inverso:
    print('Temos um palíndromo.')
else:
    print('Isso não é um palíndromo.')
