#Faça um programa que leia uma frase pelo teclado 
# e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
print('\033[31m-=-\033[m'*7)
frase = str(input('\033[1;31mEscreva uma frase:\033[m ')).upper().strip()
print('\033[31m-=-\033[m'*7)
print('A letra \033[41mA\033[m aparece \033[1;4;31m{}\033[m vezes.'.format(frase.count('A')))
print('A letra \033[41mA\033[m aparece primeiro na posiçao \033[1;4;31m{}\033[m.'.format(frase.find('A')+1))
print('A última letra \033[41mA\033[m aparece na posição \033[1;4;31m{}\033[m.'.format(frase.rfind('A')+1))