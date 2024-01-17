valor_real = float(input('Digite um valor em R$: '))
dolar_hoje = 4.93 #16/01/2024

print('A conversão de R${} em US$ {:.2f}'.format(valor_real, (valor_real / dolar_hoje)))