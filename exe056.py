soma = 0
maior_idade = 0
nome_mais_velho = ""
menor20 = 0
nome_menor20 = []
for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    soma += idade
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    while sexo not in ['M', 'F']:
        print('Opção inválida. Digite apenas M ou F.')
        sexo = str(input('Sexo [M/F]').strip().upper())
    if sexo == 'M':
        if idade > maior_idade:
            maior_idade = idade
            nome_mais_velho = nome
    if sexo == 'F':
        if idade < 20:
            menor20 += 1
            nome_menor20.append(nome)
print('A média de idade do grupo é {}.'.format(soma / 4))
if nome_mais_velho != "":
    print('O homem com a maior idade do grupo é {} com {} anos.'.format(nome_mais_velho, maior_idade))
else:
    print('Nenhum homem foi digitado.')
if nome_menor20:
    print('{} mulheres possuem menos de 20 anos. {}.'.format(menor20, ', '.join(nome_menor20)))
else:
    print('Nenhuma mulher foi digitada.')
