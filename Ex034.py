#Escreva um programa que pergunte o salário de um funcionário e 
# calcule o valor do seu aumento. Para salários superiores a R$1250,00, 
# calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250.00:
    print('O aumento no salário é de \033[32m15%\033[m e ele passará a receber R$\033[1;32m{:.2f}\033[m.'.format((salario * 15 / 100)+salario))
else:
    print('O aumento no salário é de \033[31m10%\033[m e ele passará a receber R$\033[1;31m{:.2f}\033[m.'.format((salario * 10 / 100)+salario))
