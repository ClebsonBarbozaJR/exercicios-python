# Qual é o primeiro e o último nome?
nome = str(input('Digite seu nome completo: ')).strip()
lista = nome.split()
print('Seu primeiro nome é \033[1;33m{}\033[m e seu último é \033[1;33m{}\033[m.'.format(lista[0], lista[-1]))