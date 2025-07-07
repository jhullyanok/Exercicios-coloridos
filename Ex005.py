#faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
num = int(input('\033[32mDigite um número: ''\033[m'))
print('\033[32mO antecessor de {} é {}{}{}.\033[m'.format(num,'\033[1;31m',num-1,'\033[m')) 
print('\033[32mO sucessor de {} é {}{}{}.\033[m'.format(num,'\033[1;31m', num+1,'\033[m'))
