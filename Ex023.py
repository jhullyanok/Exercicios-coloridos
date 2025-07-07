#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
from time import sleep
num = int(input('\033[32mDigite um número de 0 a 9999: \033[m'))
if 0 <=num <= 9999:
    print('\033[32m-=-\033[m'*8)
    print('\033[1;31mAnalizando o número {}...\033[m'.format(num))
    print('\033[32m-=-\033[m'*8)
    sleep(1)
    print('Unidade: \033[1;31m{}\033[m'.format(num //1 %10))
    print('Dezena: \033[1;31m{}\033[m'.format(num //10 %10))
    print('Centena: \033[1;31m{}\033[m'.format(num //100 %10))
    print('Milhar: \033[1;31m{}\033[m'.format(num //1000 %10))
else:
    print('\033[1;31mErro:O número deve estar entre 0 e 9999\033[m.')
