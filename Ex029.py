#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, 
# mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
print('\033[31m-=-\033[m'*13)
velocidade = float(input('Qual a velocidade atual do carro:\033[1;31mKm\033[m'))
print('\033[31m-=-\033[m'*13)
if velocidade > 80:
    multa = (velocidade - 80) *7
    print('\033[1;31mMULTADO!\033[m Voçê execedeu o limite de velocidade que é de \033[4;1;31m80km/h\033[m.')
    print('\033[4;1;33mO valor da multa é de {:.2f}R$\033[m.'.format(multa))
print('\033[1;32mTenha um bom dia!Dirija com segurança\033[m!')