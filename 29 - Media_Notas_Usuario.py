"""
Peça ao usuário que insira suas quatro notas, calcule a média aritmética e imprima o resultado
"""

print('Olá aluno, insira suas notas para cálcular sua média.\nLembrando que a média é 6.0.\n')

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
n4 = float(input('Nota 4: '))

media = (n1 + n2 + n3 + n4) / 4

if media < 6:
    print(f'Sua média é {media}. Infelizmente você foi reprovado!')

else:
    print(f'Sua média é {media}. Parabéns você foi aprovado!')
