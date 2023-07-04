"""
Receba a altura do degrau de uma escada e a altura que o
usuário deseja alcançar subindo a escada. Calcule e mostre
quantos degraus o ususário deverá subir para atingir seu objetivo.
"""

a_degrau = float(input('Qual a altura de um degrau da escada? '))
a_usuario = float(input('Qual a altura que você deseja alcancar, em metros? '))
d_total = (a_usuario * 100)/a_degrau

print(f'Você deverá subir {d_total:.0f} degraus, para alcançar a altura {a_usuario} metros.')

