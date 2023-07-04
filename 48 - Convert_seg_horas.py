"""
Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""

total = int(input('Insira os segundos, para que seja convertido em horas, minutos e segundos: '))
hora = int(total / 3600)
minutos = int((total % 3600) / 60)
segundos = int((total % 60) % 60)

print(f'Os segundos inseridos foram convertidos para {hora}:{minutos}:{segundos}')
