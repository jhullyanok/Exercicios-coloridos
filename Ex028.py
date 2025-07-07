#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e 
# peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('\n\033[1;35mBem Vindo ao jogo de adivinhação v.1.0\033[m\n')
print ('\033[31m-=-\033[m' *20)
print('\033[32mVou pensar em um número entre 0 e 5.\033[m \033[31mTente adivinhar...\033[m')
print('\033[31m-=-\033[m'*20)
n = randint(0, 5)
a = int(input('\033[32mEm que número eu pensei?\033[m '))
print('\033[1;31mPROCESSANDO...\033[m')
sleep(3)
if a < 0 or a > 5:
    print('Erro: Digite um número entre 0 e 5.')
if a == n:
    print('\033[1;32mParabéns! Você acertou!\033[m')
else:
    print('\033[1;31mVocê errou! Eu pensei no número\033[m \033[32m{}\033[m\033[m.'.format(n))
print('\n\033[1;35m---Obrigado por jogar---\033[m\n')
