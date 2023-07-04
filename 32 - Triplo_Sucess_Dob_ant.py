"""
Leia um numero inteiro e imprima a soma do sucessor de seu triplo com
o antecessor de seu dobro.

o triplo de 5 = 15, sucessor de 15 = 16
o dobro de 5 = 10, antecessor = 9
16 + 9 = 25
"""

n: int = 5
soma = ((n * 3) + 1) + ((n * 2) - 1)

print(soma)