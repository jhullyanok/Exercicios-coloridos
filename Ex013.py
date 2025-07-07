#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario + (salario * 15 / 100)
print('\033[34m-=-\033[m'*28)
print ('O funcionário que recebia \033[31mR%{:.2f}\033[m,com 15% de aumento, passará a receber \033[32mR%{:.2f}\033[m!'.format(salario, aumento))
print('\033[34m-=-\033[m'*28)