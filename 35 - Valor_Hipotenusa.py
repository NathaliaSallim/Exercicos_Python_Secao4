"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela quação:
h = raiz de a² + b². Faça um programa que receba os valores de a e b e calcule
o valor da hipotenusa através da equação e imprima o resultado.
"""

a = int(input(f'Insira o valor de a: '))
b = int(input(f'Insira o valor de b: '))

print(f'O valor da hipotenusa é {(a ** 2) + (b ** 2)}')

