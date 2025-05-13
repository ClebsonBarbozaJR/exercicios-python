# Quantas vezes aparece a letra, em que posição na primeira e última vez

frase = str(input('Digite uma frase qualquer: ')).strip().upper()
print('Analisando sua frase...')
print('A letra \033[36;1mA\033[m aparece \033[32;1m{}\033[m vezes.'.format(frase.count('A')))
print('A letra \033[1;36mA\033[m aparece na primeira vez na posição \033[35;1m{}\033[m.'.format(frase.find('A')+1))
print('A letra \033[1;36mA\033[m aparece pela última vez na posição \033[1m{}\033[m.'.format(frase.rfind('A')+1))