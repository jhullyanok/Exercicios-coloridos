#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#E a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
from time import sleep
rodados = float(input('Quantos Km foram percorridos:Km '))
dias = int(input('Por quantos dias ele foi alugado: '))
preço = (dias*60) + (rodados*0.15)
print('\033[1;31mCALCULANDO...\033[m')
sleep (3)
print('\033[36m-=-\033[m'*26)
print('Com \033[35m{}Km\033[m rodados e \033[35m{}\033[m dias alugados,voçê pagará \033[1;31mR${:.2f}\033[m no aluguel do carro.'.format(rodados, dias, preço))
print('\033[36m-=-\033[m'*26)