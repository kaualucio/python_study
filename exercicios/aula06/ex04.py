something = input('Digite algo: ')

print('O tipo primitivo de valor é: {}'.format(type(something)))
print('Só possui espaços? {}'.format(something.isspace()))
print('É um número? {}'.format(something.isnumeric()))
print('É alfabético? {}'.format(something.isalpha()))
print('É alfanumérico? {}'.format(something.isalnum()))
print('Está em maiúsculas? {}'.format(something.isupper()))
print('Está em minúsculas? {}'.format(something.islower()))
print('Está capitalizada? {}'.format(something.istitle()))