"""
Implemente um programa que calcule o ano de nascimento
de uma pessoa a partir de sua idade.
"""

idade = int(input('Insira sua idade: '))
ano_atual = int(input('Ano atual: '))

ano_nasc = ano_atual - idade

print(f'O ano de seu nascimento é {ano_nasc}.')

