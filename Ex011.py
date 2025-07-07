#Faça um programa que leia a largura e a altura de uma parede em metros
#calcule a sua área e a quantidade de tinta necessária para pintá-la
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados
largura = float(input('Qual a largura desejada? '))
altura = float(input('Qual a altura desejada? ')) 
area = largura * altura
print('\033[32m-=-\033[m'*24)
print('A quantidade de tinta necessária para pintar \033[33m{} metros\033[m é \033[31m{} litros\033[m! '.format(area, area /2))
print('\033[32m-=-\033[m'*24)
