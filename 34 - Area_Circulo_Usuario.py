"""
Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
Area= pi * raio², considere pi = 3,14.
Achei importante calcular a:
Circunferência = 2 * pi * raio
Diâmetro = 2 * raio
"""

pi = 3.14

raio = float(input(f'Qual o valor do raio do cículo? '))
print(f'A área do cículo é {pi * raio ** 2}.\nA circunferencia é {round(2 * pi * raio,2)}.\nE o diametro é {2 * raio}')

