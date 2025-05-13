# Fazendo o computador escolher um número aleatório

from random import choice
from time import sleep

lista = [0, 1, 2, 3, 4, 5] # O computador vai escolher um número de 0 a 5 dentro dessa lista.
escolhido = choice(lista)
print('Vou pensar em número entre 0 e 5, tente adivinhar!\n')
num = int(input('Qual número eu escolhi? '))
print('PROCESSANDO...')
sleep(2) # Delay de 2 segundos
print('O número que eu escolhi foi {}'.format(escolhido))
if num == escolhido: # Se for igual aos valores da lista...
    print('Você acertou!')
else:
    print('Você errou.')
