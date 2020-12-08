# programa para resolução de equação de segundo grau

import math

# entrada das variáveis da equação

a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

# print('Sua equação de baskhara ficou da seguinte forma: {}x^2 + {}x + {} = 0'.format(a, b, c))

delta = ((b ** 2) - 4 * a * c)

# print('O valor de delta é: {}'.format(delta))

if delta < 0:
    print('esta equação não possui raízes reais')

elif delta > 0:
    raiz1 = ((-1 * b) + (math.sqrt(delta))) / (2 * a)
    raiz2 = ((-1 * b) - (math.sqrt(delta))) / (2 * a)
    if raiz1 < raiz2:
        print('as raízes da equação são {} e {}'.format(raiz1, raiz2))
    else:
        print('as raízes da equação são {} e {}'.format(raiz2, raiz1))

elif delta == 0:
    raiz1 = (-1 * b) / (2 * a)
    print('a raíz desta equação é {}'.format(raiz1))

# print('Fim do programa!')
