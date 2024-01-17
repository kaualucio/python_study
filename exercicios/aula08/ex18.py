from math import cos, sin, tan, radians

angulo = float(input('Digite um ângulo: '))


print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, sin(radians(angulo))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cos(radians(angulo))))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tan(radians(angulo))))