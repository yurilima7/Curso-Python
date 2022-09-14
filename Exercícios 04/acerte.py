from random import randint

sorteado = randint(1, 5)

chute = int(input("Digite um número entre 1 e 5: "))

if(sorteado == chute):
    print('Você acertou!')
else:
    print("Você errou! Sorteado foi: {}".format(sorteado))