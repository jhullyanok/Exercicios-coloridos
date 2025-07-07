# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from calendar import isleap
from datetime import date
ano = int(input('\033[34mQual ano deseja analizar?\033[m \033[1;36mDigite 0 para analizar o ano atual:\033[m '))
if ano == 0:
    ano = date.today().year
if isleap(ano):
    print('O ano \033[4m{}\033[m é \033[1;35mbissexto\033[m!'.format(ano))
else:
    print('O ano \033[4m{}\033[m não é \033[1;35mbissexto\033[m!'.format(ano))
