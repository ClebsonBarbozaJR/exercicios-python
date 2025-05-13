# Sorteando o aluno que vai apagar o quadro

from random import choice
n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceito aluno: ")
n4 = input("Quarto aluno: ")
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print("O aluno escolhido foi {}.".format(escolhido))