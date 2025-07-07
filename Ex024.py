#Crie um programa que leia o nome de uma cidade e 
# diga se ela começa ou não com o nome “SANTO”.
cidade = str(input('Digite o nome da cidade que voçê nasceu: ')).strip()
print('\033[34m-=-\033[m'*2)
print('\033[36m', cidade[0:5].capitalize() == 'Santo','\033[m')
print('\033[34m-=-\033[m'*2)
