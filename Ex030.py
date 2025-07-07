#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número inteiro qualquer: '))
if num %2 ==0:
    print('\033[35m-=-\033[m'*7)
    print('o número \033[4m{}\033[m é \033[1;36mPAR\033[m'.format(num))
    print('\033[35m-=-\033[m'*7)
else:
    print('\033[35m-=-\033[m'*7)
    print('o número \033[4m{}\033[m é \033[1;34mÍMPAR\033[m'.format(num))
    print('\033[35m-=-\033[m'*7)