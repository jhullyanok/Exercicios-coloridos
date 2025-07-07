#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
c = float(input('Informe a temperatura: \033[34m°C\033[m'))
f = c * 9 / 5 + 32
print('\033[36m-=-\033[m'*15)
print('A temperatura de \033[34m{}°C\033[m corresponde a \033[36m{}°F\033[m!'.format(c, f))
print('\033[36m-=-\033[m'*15)