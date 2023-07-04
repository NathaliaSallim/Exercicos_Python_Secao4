"""
Leia  a altura e o raio de um cilindro circular e imprima o volume do
cilindro. o volume de um cilindro circular é calculado por meio da
seguinte fórmula: V = pi * raio² * altura, onde pi = 3,14.
"""

print(f'--------------------------------\n'
      f'|  CALCULADORA DO VOLUME DE UM |\n'
      f'|       CILINDRO CIRCULAR      |\n'
      f'--------------------------------\n')

pi = 3.14
raio = float(input(f'Insira o valor do raio: '))
altura = float(input(f'Insira o valor da altura: '))

v = pi * raio ** 2 * altura

print(f'O valor do volume do cilindro é: {v}')
"""
ou retirar a fórmula v = pi * raio ** 2 * altura 
e print(f'O valor do volume do cilindro é: {pi * (raio ** 2) * altura}')
"""
