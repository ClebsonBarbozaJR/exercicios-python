from random import randint
from time import sleep

print('\033[33;1m-=-\033[m' * 10)
print('\033[1;34mJOKENPO\033[m'.center(40))
print('\033[33;1m-=-\033[m' * 10)
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua escolha? '))
if jogador < 0 or jogador > 2:
    print('\033[31;1mOpção inválida.\033[m')
else:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PÔ!!!')
    print('-=' * 12)
    print('Jogador escolheu {}'.format(itens[jogador]))
    print('Computador escolheu {}'.format(itens[computador]))
    print('-=' * 12)
    if computador == 0: # computador escolhe PEDRA
        if jogador == 0:
            print('\033[1mEMPATE!\033[m')
        elif jogador == 1:
            print('\033[32;1mJOGADOR VENCE!\033[m')
        else:
            print('\033[33;1mCOMPUTADOR VENCE!\033[m')
    elif computador == 1: # computador escolhe PAPEL
        if jogador == 0:
            print('\033[33;1mCOMPUTADOR VENCE!\033[m')
        elif jogador == 1:
            print('\033[1mEMPATE!\033[m')
        else:
            print('\033[32;1mJOGADOR VENCE!\033[m')
    elif computador == 2: # computador escolhe TESOURA
        if jogador == 0:
            print('\033[32;1mJOGADOR VENCE!\033[m')
        elif jogador == 1:
            print('\033[33;1mCOMPUTADOR VENCE!\033[m')
        else:
            print('\033[1mEMPATE!\033[m')