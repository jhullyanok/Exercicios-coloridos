#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
print('\033[33m-=-\033[m'*9)
print('A hipotenusa mede \033[32m{:.2f}\033[m.'.format(hypot(co, ca)))
print('\033[33m-=-\033[m'*9)