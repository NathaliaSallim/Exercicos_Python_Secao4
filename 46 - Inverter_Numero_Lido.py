"""
Faça um programa que leia um número inteiro positivo de três digitos
(de 100 a 999). Gere outro número formado pelos dígitos invertidos
do número lido. Exemplo;
NumeroLido= 123
NumeroGerado = 321
"""

n_lido = (input('Digite um número inteiro de 100 a 999: '))

print(f'O número digitado foi {n_lido} e o número gerado pelos digitos invertidos foi {n_lido[::-1]}.')
