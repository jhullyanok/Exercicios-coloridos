# Crie um programa que leia um número real qualquer pelo teclado 
# e mostre na tela a parte inteira desse número.
from math import trunc, floor, ceil
print('\033[32m-=-\033[m'*10)
num = float(input('\033[1;33mDigite um número:\033[m '))
print('\033[32m-=-\033[m'*10)
print('O número \033[33m{}\033[m tem a parte inteira \033[32m{}\033[m.'.format(num, trunc(num)))
print('O número \033[33m{}\033[m arredondado para cima é \033[32m{}\033[m.'.format(num, ceil(num)))
print('O número \033[33m{}\033[m arredondado para baixo é \033[32m{}\033[m.' .format(num, floor(num)))