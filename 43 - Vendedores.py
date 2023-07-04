"""
Escreva um programa de ajuda para vendedores. A partir
de um valor total lido mostre:
* o total a pagar com desconto de 10%;
* o valor de cada parcela, no parcelamento de 3x sem juros;
* a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto);
* a comisão do vendedor, no caso da venda ser parcelada (5% sobre o valor total).
"""

total_venda = float(input(f'Qual o valor total da venda? R$ '))
d = total_venda - (total_venda * 10)/100
p = d / 3
c1 = d + (d * 5)/100
c2 = total_venda + (total_venda * 5)/100

print(f'O valor total a pagar, com o desconto de 10% é de R$ {d} ')
print(f'O parcelamento é de 3x sem juros, o valor de cada parcela será de R$ {p}')
print(f'A comissão do vendedor, no pagamento a vista, é de R$ {c1}')
print(f'A comissão do vendedor, no pagamento parcelado, é de R$ {c2}')







