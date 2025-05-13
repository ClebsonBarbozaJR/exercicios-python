# Aluguel de carros

dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))
valor_carro = 60 * dias
km_rodado = 0.15 * km
valor_total = valor_carro + km_rodado
print("O total a pagar é R${:.2f}.".format(valor_total))