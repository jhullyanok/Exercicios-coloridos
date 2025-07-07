#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada
from time import sleep
num = int(input('Digite um número: '))
print('\033[31m-=-\033[m'*7)
print('\033[32mANALIZANDO {}...\033[m'.format(num))
print('\033[31m-=-\033[m'*7)
sleep(3)
print('O dobro é {}{}{}.'.format('\033[32m',num*2,'\033[m'))
print('O triplo é {}{}{}.'.format('\033[32m',num*3, '\033[m'))
print('A raiz quadrada é {}{:.2f}{}.'.format('\033[32m',num ** (1/2),'\033[m'))
