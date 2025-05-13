 #Crie um programa que mostre o nome do usuário e dê boas vindas.

nome = input("Qual é o seu nome? ").strip()
print('Olá \33[4;32m{}\33[m, \33[33mprazer em te conhecer!\33[m'.format(nome))

