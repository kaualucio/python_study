salario = float(input('Qual é o salário do funcionário? R$'))
valor_com_aumento = salario + (salario * 0.15)

print('O salário de R${:.2f} com aumento de 15% será de R${:.2f}'.format(salario, valor_com_aumento))