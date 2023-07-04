"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido
proporcionalmente ao valor que cada deu para a realização da aposta.
Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima
quanto cada um ganharia do prêmio com base no que investiu.
"""

p1 = input('Insira o nome do ganhador: ')
p2 = input('Insira o nome do outro jogador: ')
p3 = input('Insira o nome do outro ganhador: ')
v_premio = float(input('Insira o valor do prêmio ganho: R$ '))

apostador1 = float(input(f'Quanto investiu o ganhador {p1.title()}? R$ '))
apostador2 = float(input(f'Quanto investiu o ganhador {p2.title()}? R$ '))
apostador3 = float(input(f'Quanto investiu o ganhador {p3.title()}? R$ '))

v_total_apostado = apostador1 + apostador2 + apostador3

resultado1 = ((v_total_apostado / apostador1) * v_premio)
resultado2 = ((v_total_apostado / apostador2) * v_premio)
resultado3 = ((v_total_apostado / apostador3) * v_premio)

print(f'O ganhador {p1.title()}, irá receber R$ {resultado1:.2f}\n'
      f'O ganhador {p2.title()}, irá receber R$ {resultado2:.2f}\n'
      f'O ganhador {p3.title()}, irá receber R$ {resultado3:.2f}')


