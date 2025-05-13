# Calculando o comprimento de uma hipotenusa 

# Com bibliotecas
from math import sqrt, pow
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
h = (pow(co, 2)) + (pow(ca, 2))
raizh = sqrt(h)
print("O comprimento da hipotenusa é {:.2f}.".format(raizh))

# De forma padrão
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
h = (co**2) + (ca**2)
raizh = h**(1/2)
print("O comprimento da hipotenusa é {:.2f}".format(raizh))


# Usando a biblioteca hypot (que calcula a hipotenusa automaticamente)
from math import hypot
co = float(input("Comprimento do cateto oposto: "))
ca = float(input("Comprimento do cateto adjacente: "))
h = hypot(co, ca)
print("O comprimento da hiptenusa é {:.2f}.".format(h))
