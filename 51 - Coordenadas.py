"""
Escreva um programa que leia as coordenadas x e y de pontos no R²
e calcule
"""

import math

x1 = 0
y1 = 0
x2 = int(input('Digite o ponto (x2): '))
y2 = int(input('Digite o ponto (y2): '))

d1 = ((x1-x2) ** 2 + (y1-y2) ** 2)
d2 = math.sqrt(d1)

print(f'A distância entre os pontos é {d2:.2f}')

