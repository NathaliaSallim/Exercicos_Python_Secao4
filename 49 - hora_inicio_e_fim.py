"""
Faça um programa que leia o horário (hora,minuto e segundo) de inicio e duração,
em segundos, de uma experiência biológica. O programa deve resultar com o novo horário (hora, minuto e segundo)
do término da mesma.
"""

hora_inicio = int(input('Insira a hora inicial: '))
min_inicio = int(input('Insira os minutos: '))
seg_inicio = int(input('Insira os segundos: '))
duracao = int(input('Quantos segundos durou sua experiência: '))

hora_seg = int(hora_inicio * 60)
min_seg = int(hora_inicio * 60)
total_seg = hora_seg + min_seg + seg_inicio + duracao

hora_final = int((total_seg / 3600))
min_final = int((total_seg % 3600) / 60)
seg_final = int((total_seg % 3600) % 60)

print(f'Você começou a experiência às {hora_inicio}:{min_inicio}:{seg_inicio}\n'
      f'A duração da sua experiência foi {duracao} segundos\n'
      f'Você terminou a experiência às {hora_final}:{min_final}:{seg_final}.')


