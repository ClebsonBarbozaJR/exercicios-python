# Adivinhando o número escolhido entre 0 e 10, mas o programa só para quando acertar
# Contando quantas tentativas foram necessárias para acertar
from random import randint

palpite = 0
computador = randint(0,10)
jogador = -1

print('Pensei em um número de 0 a 10. Tente acertar!')
while computador != jogador:
        jogador = int(input('Escolha um número: '))
        palpite += 1
        if jogador > computador:
            print('Menos... tente novamente')
        elif jogador < computador:
            print('Mais... tente novamente')
print('Você acertou com {} tentativas.'.format(palpite))

