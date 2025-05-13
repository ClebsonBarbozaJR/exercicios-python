from time import sleep

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
escolha = 0
while escolha != 5:
    escolha = int(input('''-=-=-=-=-=-=-=-=-=-=-=-
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa\n-=-=-=-=-=-=-=-=-=-=-=-\nO que deseja fazer? '''))
    if escolha == 1:
        print(f'O resultado de {n1} + {n2} = {n1 + n2}')
    elif escolha == 2:
        print(f'O resultado de {n1} x {n2} = {n1 * n2}')
    elif escolha == 3:
        if n1 > n2:
            print(f'O maior número é {n1}')
        elif n1 < n2:
            print(f'O maior número é {n2}')
        else:
            print('Os dois números são iguais.')
    elif escolha == 4:
        print('Informe os números novamente.')
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
    elif escolha > 5 or escolha < 1:
        print('Opção inválida. Tente novamente.')
print('Finalizando...')
sleep(2)
print('Você saiu do programa.')