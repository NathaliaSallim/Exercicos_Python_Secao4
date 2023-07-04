"""
Receba o sálario-base de um funcionário. Calcule e imprima o sálario
a receber, sabendo-se que esse funcionário tem uma gratificaçaõ de 5%
sobre o salário-base. Além disso, ele paga 7% de imposto sobre o salário-base.
"""

s_base = float(input('Qual o valor do salário-base do funcionário? '))
g = int(input('Qual o valor em porcentagem de gratificação? '))

print(f'O salário a receber é de R$ {s_base - (s_base * 2)/100:.2f} ')