km = float(input('Quantos KM o carro percorreu? '))
dias_alugado = float(input('Por quantos dias ele foi alugado? '))

total_a_pagar = (dias_alugado * 60) + (km * 0.15)

print('O total a pagar é R${:.2f}'.format(total_a_pagar))