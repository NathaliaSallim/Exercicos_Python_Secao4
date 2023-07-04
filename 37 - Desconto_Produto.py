"""
Faça um programa que leia o valor de um produto e imprima
o valor com o desconto, tendo em vista que o desconto foi de 12%
"""

print(f'Cálculo de desconto')

p = float(input(f'Qual o valor do produto? '))
vd = float(input(f'Insira o valor do desconto em %: '))
d = (p * vd) / 100

print(f'Valor do produto R$ {p}')
print(f'Desconto ganho R$ {vd}')
print(f'Valor com desconto R$ {p - d}')
