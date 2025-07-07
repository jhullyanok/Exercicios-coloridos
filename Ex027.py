#Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o último nome separadamente
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('\033[35m-=-\033[m'*7)
print('\033[1;35mPrazer em te conhecer!\033[m')
print('\033[35m-=-\033[m'*7)
print('O seu primeiro nome é \033[4;35m{}\033[m'.format(nome[0]))
print('O seu último nome é \033[4;35m{}\033[m'.format(nome[len(nome)-1]))
