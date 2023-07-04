"""
Peça ao usuário que digite três valores  inteiros e imprima a soma deles
"""

nome = input('Olá, qual o seu nome? \n').title()
print(f'Seja bem-vindo(a){nome}, vamos somar?\n')

a = int(input('Digite um número '))
b = int(input('Digite outro número '))
c = int(input('Digite mais um número '))
soma = a + b + c

print(f'A soma de {a} + {b} + {c} é = {soma}')

