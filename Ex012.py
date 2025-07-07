#Faça um algoritmo que leia o preço de um produto
# e mostre seu novo preço, com 5% de desconto.
produto = float(input('\033[33mQual o preço do produto?\033[m \033[32mR%\033[m\033[m'))
avista = produto - (produto * 10 / 100)
parcelado = produto + (produto * 15 / 100)
print('\033[36m-=-\033[m'*10)
print('A vista sairá por \033[34mR%{}\033[m!'.format(avista))
print('E a prazo sairá por \033[34mR${}\033[m!'.format(parcelado))
print('\033[36m-=-\033[m'*10)