# Descobrindo o seno, cosseno e tangente de um ângulo.

from math import sin, cos, tan, radians
an = float(input("Digite um ângulo: "))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print("O ângulo de {} tem o SENO de {:.2f}.".format(an, seno))
print("O ângulo de {} tem o COSSENO de {:.2f}.".format(an, cosseno))
print("O ângulo de {} tem a TANGENTE de {:.2f}.".format(an, tangente))
