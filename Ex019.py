#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
aluno1 = input('Nome do aluno 1: ')
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 3: ')
aluno4 = input('Nome do aluno 4: ')
lista = [aluno1,aluno2,aluno3,aluno4]
sorteio = choice(lista)
print('\033[31m-=-\033[m'*19)
print('\033[1;4mO aluno escolhido para apagar o quadro foi \033[1;31m{}\033[m.'.format(sorteio))
print('\033[31m-=-\033[m'*19)