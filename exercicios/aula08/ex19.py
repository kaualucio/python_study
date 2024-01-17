from random import randrange

primeiro = input('Primero Aluno: ')
segundo = input('Segundo Aluno: ')
terceiro = input('Terceiro Aluno: ')
quarto = input('Quarto Aluno: ')
lista = [primeiro, segundo, terceiro, quarto]

print('O aluno escolhido foi {}'.format(lista[randrange(0, 3)]))