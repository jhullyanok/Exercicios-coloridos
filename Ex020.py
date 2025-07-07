from random import shuffle, choice
from time import sleep
# Lista de códigos de cores ANSI
cores = [
    '\033[31m',  # vermelho
    '\033[32m',  # verde
    '\033[33m',  # amarelo
    '\033[34m',  # azul
    '\033[35m',  # magenta
    '\033[36m',  # ciano
    '\033[37m',  # branco
]

nome1 = str(input('Nome do primeiro aluno: '))
nome2 = str(input('Nome do segundo aluno: '))
nome3 = str(input('Nome do terceiro aluno: '))
nome4 = str(input('Nome do quarto aluno: '))
lista = [nome1, nome2, nome3,nome4]
shuffle(lista)
print('\033[33m-=-\033[m'*13)
print('\033[1;33mA ordem de apresentação dos alunos é:\033[m')
print('\033[33m-=-\033[m'*13)
for i, nome in enumerate(lista):
    cor = cores[i % len(cores)]
    print(f'{cor}{i + 1}º → {nome}\033[m')
    sleep(0.5)