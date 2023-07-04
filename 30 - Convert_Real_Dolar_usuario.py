"""
Leia um valor em real e calcule a cotação do dólar.
Em seguida, imprima o valor correspondente em dólares.
R = real, C = Cotação do dólar hoje, D = fórmula para conversão, sendo Real/pela cotação do dólar.
Mesmo exercício, porém, com a interação do usuário.
"""

print(' ______________________________ ')
print('|     CONVERSOR DE MOEDAS      |')
print('|        REAL EM DÓLAR         |')
print(' ------------------------------ ')

R = float(input(f'Insira o valor em Real R$ '))
C = 4.92
D = R/C

print(f'O valor em dólar é US$ {round(D, 2)}')
