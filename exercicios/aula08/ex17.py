from math import sqrt, pow

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = sqrt((pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)))

print('A hipotenusa mede {:.2f}'.format(hipotenusa))