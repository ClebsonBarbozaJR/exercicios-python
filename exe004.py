# Dissecando uma variável.

a = input('Digite algo: ')
print('\33[37;7mO tipo primitivo é\33[m ', type(a))
print('\33[31;1mÉ somente espaços?\33[m ', a.isspace())
print('\33[30;7mÉ um número?\33[m', a.isnumeric())
print('\33[35mÉ alfabético?\33[m', a.isalpha())
print('\33[33;40;4mÉ alfanúmerico?\33[m', a.isalnum())
print('\33[37;1mEstá em minúsculas?\33[m', a.islower())
print('\33[32mEstá em MAIÚSCULAS?\33[m', a.isupper())
print('\33[36;40;7mEstá capitalizada?\33[m', a.istitle())


