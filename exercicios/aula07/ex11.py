largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura*altura

print('Sua parede tem dimensão de {:.2f}x{:.2f} e sua área é de {:.2f}.'.format(largura, altura, (area)))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format((area/2)))