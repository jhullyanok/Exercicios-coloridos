#Crie um programa que leia o nome completo de uma pessoa e mostre:
#– O nome com todas as letras maiúsculas e minúsculas.
#– Quantas letras ao todo (sem considerar espaços).
#– Quantas letras tem o primeiro nome.
from time import sleep
nome = str(input('\033[32mDigite o seu nome completo:\033[m ').strip())
print('\033[34m-=-\033[m'*8)
print('\033[1;36mAnalizando seu nome...\033[m')
print('\033[34m-=-\033[m'*8)
sleep(2)
print('Seu nome em maiúsculas é \033[1;36m{}\033[m'.format(nome.upper()))
print('Seu nome em minúsculas é \033[1;36m{}\033[m]'.format(nome.lower()))
print('O seu nome tem ao total \033[1;36m{}\033[m letras'.format(len(nome.replace(' ', ''))))
print('E o seu primeiro nome tem \033[1;36m{}\033[m letras ao total.'.format(len(nome.split()[0])))