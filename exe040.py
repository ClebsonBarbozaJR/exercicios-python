n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('Média: \033[33;1m{:.1f}\033[m'.format((n1 + n2) / 2))
if (n1 + n2) / 2 < 5.0:
    print('O aluno está \033[31;1mREPROVADO\033[m.')
elif (n1 + n2) / 2 >= 5.0 and (n1 + n2) / 2 <= 6.9:
    print('O aluno está de \033[34;1mRECUPERAÇÃO\033[m.')
else:
    print('O aluno foi \033[32;1mAPROVADO\033[m.')