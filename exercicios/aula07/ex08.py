distancia = float(input('Digite uma distância em metros: '))

print('A média de {} metros corresponde a:'.format(distancia))
print('{}km'.format((distancia/1000)))
print('{}hm'.format((distancia/100)))
print('{}dam'.format((distancia/10)))
print('{:.0f}dm'.format((distancia*10)))
print('{:.0f}cm'.format((distancia*100)))
print('{:.0f}mm'.format((distancia*1000)))