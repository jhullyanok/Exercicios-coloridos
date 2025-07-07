#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média
nome = str(input('Qual é o nome do aluno? '))
nota1 = float(input('A primeira nota do aluno: '))
nota2 = float(input('A segunda nota: '))
nota3 = float(input('A terceira nota: '))
nota4 = float(input('A quarta nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print('\033[31m-=-\033[m'*20)
print ('\033[35mCalculando as notas do aluno {},a sua média escolar é {:.1f} !\033[m'.format(nome, media))
print('\033[31m-=-\033[m'*20)
