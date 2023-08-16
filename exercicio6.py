import math

pi = math.pi

raio = float(input('Digite o valor do raio'))

volume = (4/3)*(pi*(math.pow(raio, 3)))

area = 4*(pi*(math.pow(raio, 2)))

print(f'O valor do volume é igual a: {volume:.2f}')
print(f'O valor do area é igual a: {area:.2f}')