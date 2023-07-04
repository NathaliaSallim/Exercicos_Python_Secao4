"""
Faça um programa que leia o valor da hora de trabalho (em reais) e
números de horas trabalhados no mês. Imprima o valor a ser pago ao funcionário,
adicionando 10% sobre o valor calculado.
"""

v_hora = float(input('Qual o valor da hora de trabalho em reais? '))
h_mes = int(input('Quantas horas o funcionário trabalhou esse mês? '))

salario: float = (v_hora * h_mes) * 1.1

print(f'O valor a ser pago ao funcionário, incuindo o adional de 10%, é de R$ {salario:.2f}')
