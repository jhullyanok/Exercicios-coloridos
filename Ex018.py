#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin,cos,tan,radians
print('\033[36m-=-\033[m'*13)
angulo = float(input('\033[1;35mDigite o valor do ângulo desejado:\033[m '))
print('\033[36m-=-\033[m'*13)
conversao = radians(angulo)
print('\033[1;35mSENO:\033[m {:.2f}'.format(sin(conversao)))
print('\033[1;35mCOSSENO:\033[m {:.2f}'.format(cos(conversao)))
print('\033[1;35mTANGENTE:\033[m {:.2f}'.format(tan(conversao)))
