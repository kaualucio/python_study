preco = float(input('Qual o preço do produto? R$'))
desconto = 0.05 #5%
valor_com_desconto = preco - (preco * desconto)

print('O novo valor do produto com desconto de 5% é de R${:.2f}'.format(valor_com_desconto))