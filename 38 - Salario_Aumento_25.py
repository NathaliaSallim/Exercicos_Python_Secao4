"""
Leia o salário de um funcionário. Calcule e imprima o valor com o
desconto, tendo em vista que o desconto foi de 25%
"""

s_atual = float(input(f'Insira o salário atual do funcionário R$ '))
percentual = int(input(f'Qual o valor do aumento em % '))

percentual = percentual / 100
aumento = percentual * s_atual
s_novo = s_atual + aumento

print(f'Salário atual do funcionário é de R$ {s_atual}')
print(f'O aumento em porcentagem foi de {percentual:.1%}')
print(f'O aumento foi de R$ {aumento:.2f}')
print(f'Novo salário R$ {s_novo}')
