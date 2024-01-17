import random

primeiro = input('Primero Aluno: ')
segundo = input('Segundo Aluno: ')
terceiro = input('Terceiro Aluno: ')
quarto = input('Quarto Aluno: ')
lista = [primeiro, segundo, terceiro, quarto]
random.shuffle(lista)

print('A ordem da apresentação é {}'.format(lista))