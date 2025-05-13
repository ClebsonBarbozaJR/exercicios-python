# Descobrindo se um número digitado pelo o usuário é primo ou não
n = int(input('Digite um número: '))
cont = 0
for i in range(1, n+1):
    if n % i == 0: # Se os números do intervalo forem divisíveis por zero...
        cont +=1 # ... Vai ser incrementado + 1 no contador
        print('\033[32m', end='') # Mostra na cor verde os números divísíveis
    else:
        print('\033[31m', end='') # Mostra na cor vermelha quem não é divisível
    print('{}'.format(i), end=' ') # Imprime o intervalo
print('\033[m\nNúmeros divisíveis: {}'.format(cont))
if cont == 2: # Se tiver apenas 2 divisores, é primo
    print('\033[mEste número é primo.')
else:
    print('\033[mEste número não é primo.')
