"""
Peça que o usuário digite três valores e apresente como resultado a soma dos
quadrados do três valores lidos.
"""

nome = input("Olá, qual o seu nome?\n").title()
print(f'Olá, {nome}, digite três números e o resultado será a soma do quadrado dos três números. \n')

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))

soma = x ** 2 + y ** 2 + z ** 2


print(f'A soma dos quadrados dos três números é {soma}')