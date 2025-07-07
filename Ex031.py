# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
# e R$0,45 parta viagens mais longas.
distancia = float(input('Qual foi a distância da viagem?\033[31;1mKm\033[m'))
print('\033[32mVoçê está preste a começar uma viagem de \033[4m{}Km\033[m\033[m.'.format(distancia))
if distancia <= 200:
    print('\033[32m-=-\033[m'*13)
    print('\033[33mO valor da passagem é de \033[m\033[1;32mR%{:.2f}\033[m\033[m.'.format(distancia*0.50))
    print('\033[32m-=-\033[m'*13)
else:
    print('\033[32m-=-\033[m'*13)
    print('\033[33mO valor da passagem é de \033[m\033[1;31mR%{:.2f}\033[m\033[m.'.format(distancia*0.45))
    print('\033[32m-=-\033[m'*13)