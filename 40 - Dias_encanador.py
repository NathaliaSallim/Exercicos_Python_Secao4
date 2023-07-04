"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que
solicite o número de dias trabalhados pelo encanador e imprima a quantia liquida
que deverá ser poga, sabendo-se que são descontados 8% para imposto de renda.
"""

dia = int(input(f'Insira o total de dias trabalhados pelo encanador: '))
valor_dia = 30
d_imposto = 8
q_bruta = (valor_dia * dia)
q_liquida = (q_bruta * d_imposto)/100

print(f'O valor a ser pago ao encanador, considerando o desconto de 8%, é de R$ {q_bruta - q_liquida}')



