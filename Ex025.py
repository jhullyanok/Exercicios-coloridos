#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
nome = str(input('Digite seu nome completo: ')).strip()
print('\033[31m-=-\033[m'*9)
print('O seu nome tem \033[4mSilva\033[m: \033[1;31m{}\033[m'.format('SILVA' in nome.upper()))
print('\033[31m-=-\033[m'*9)