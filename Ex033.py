#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('\033[31mDigite o primeiro número:\033[m '))
n2 = int(input('\033[32mDigite o segundo número:\033[m '))
n3 = int(input('\033[34mDigite o terceiro número:\033[m '))
lista = [n1,n2,n3]
print('O maior número é {}{}{}, e menor número é {}{}{}.'.format('\033[1;33m',max(lista),'\033[m','\033[1;36m',min(lista),'\033[m'))
