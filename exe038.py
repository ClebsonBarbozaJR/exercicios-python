# Quem é maior? O Primeiro ou o Segundo valor?

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
if num1 > num2:
    print('O \033[1mPRIMEIRO VALOR\033[m é o \033[1;32mMAIOR\033[m.')
elif num1 < num2:
    print('O \033[1mSEGUNDO VALOR\033[m é o \033[1;32mMAIOR\033[m.')
else:
    print('Os dois valores são \033[1;31mIGUAIS\033[m.')
