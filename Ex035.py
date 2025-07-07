#Desenvolva um programa que leia o comprimento de três retas e 
# diga ao usuário se elas podem ou não formar um triângulo.
print('\033[34m-=-\033[m'*9)
print('\033[1;35m=ANALIZADOR DE TRIÂNGUlOS\033[m')
print('\033[34m-=-\033[m'*9)
reta1 = float(input('\033[35mDigite o segmento 1:\033[m '))
reta2 = float(input('\033[35mDigite o segmento 2:\033[m '))
reta3 = float(input('\033[35mDigite o segmento 3:\033[m '))
if reta1 + reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print('\033[1;32mAs retas PODEM FORMAR um triângulo\033[m.')
else:
    print('\033[1;31mAs retas NÃO PODEM FORMAR um triângulo.\033[m')
