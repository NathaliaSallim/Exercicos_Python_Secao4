"""
Leia quatro notas, calcule a média aritmética e imprima o resultado
"""

n1 = 6.5
n2 = 7.5
n3 = 8.5
n4 = 9.0

"""
adicionei a função round() para diminiur o número de casas decimais, o número 1 corresponde a quantidade de casas 
decimais que desejo.
"""

media = round((n1 + n2 + n3 + n4) / 4, 1)
print(f'Média = {media}')