# Dizendo quantas pessoas são maiores e menores de idade + Bônus: O nome e quais condições satisfazem
from datetime import date

contm = 0
contnaom = 0
maiores = []
menores = []
for i in range(1, 8):
    nome = str(input('Nome da {}º pessoa: '.format(i)))
    nasc = int(input('Ano de nascimento da {}º pessoa: '.format(i)))
    if date.today().year - nasc >= 18:
        contm += 1
        maiores.append(nome)
    else:
        contnaom += 1
        menores.append(nome)
print('{} pessoas são maiores de idade: {}.'.format(contm, ", ".join(maiores)))
print('{} pessoas são menores de idade: {}.'.format(contnaom, ", ".join(menores)))

