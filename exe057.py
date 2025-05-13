s = input('''Qual o seu sexo?
[ M ] Masculino
[ F ] Feminino\n''').strip().upper()
while s not in ['M', 'F']:
    s = input('Opção inválida. Digite apenas M ou F.\n').strip().upper()
print('Sexo {} resgitrado com sucesso.'.format(s))