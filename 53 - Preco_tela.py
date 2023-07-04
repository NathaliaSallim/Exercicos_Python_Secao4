"""
Faça um programa para ler as dimensões de um terreno
(comprimento c e largura l), bem como o preço do metro
de tela p. Imprimao custo para cercas este mesmo terreno
com tela.
"""

c = float(input("Qual o comprimento do terreno? "))
l = float(input("Qual a largura_do terreno? "))
t = float(input("Qual o valor dometro da tela? "))

total_area = c * l
custo = total_area * t

print(f'O valor para cercar o terreno é de R$ {custo:.2f}')

