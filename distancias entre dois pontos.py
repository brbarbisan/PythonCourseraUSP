import math

x1 = int(input('Digite a primeira coordenada x: '))
y1 = int(input('Digite a primeira coordenada y: '))
x2 = int(input('Digite a segunda coordenada x: '))
y2 = int(input('Digite a segunda coordenada y '))

d = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) ** 2))

# print(d)

if d >= 10:
    print('longe')
else:
    print('perto')