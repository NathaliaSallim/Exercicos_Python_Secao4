"""
A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
- O primeiro ganhador receberá 46%
- O segundo ganhador receberá 32%
- O terceiro receberá o restante;(22%)
Calcule e imprima a quantia ganha por cada um dos ganhadores
"""

v_total = 780.000
g1 = (v_total * 46)/100
g2 = (v_total * 32)/100
g3 = (v_total * 22)/100

print(f'O primeiro ganhador receberá R$ {g1:.3f}')
print(f'O segundo ganhador receberá R$ {g2:.3f}')
print(f'O terceiro ganhador receberá R$ {g3:.3f}')
