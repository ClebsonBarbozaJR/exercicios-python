cidade = str(input('Qual o nome da sua cidade? '))
separado = cidade.upper().split()
print('O nome da sua cidade é {}.\nComeça com SANTO? {}.'.format(cidade, 'SANTO' in separado[0]))