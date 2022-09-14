vel = int(input("Digite a velocidade do carro: "))

if(vel > 80):
    print("Ultrapassou limite de velocidade!")
    print("Multa de: R$ {:.2f}!".format(7.0 * (vel - 80)))
else:
    print("Parabéns, tudo em ordem!")