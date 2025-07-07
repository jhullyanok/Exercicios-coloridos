#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
carteira = float(input('\033[33mValor na carteira:\033[m '))
print('Com \033[32m{} reais\033[m na sua carteira,voçê pode comprar \033[32m{:.2f} dolares\033[m'.format(carteira, carteira*5.71))
