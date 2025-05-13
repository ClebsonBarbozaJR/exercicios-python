# Aumento salárial de 15% #

salario = float(input("Qual o salário do funcionário? R$"))
print("O funcionário que ganhava R${:.2f}, com 15% de aumento, passará a ganhar R${:.2f}.".format(salario, (salario + (15 / 100 * salario))))