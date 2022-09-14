d = float(input("Digite a distância em Km da viagem: "))

if d <= 200:
    print("O Preço foi de R$ {:.2f}!".format(0.5 * d))
else:
    print("O Preço foi de R$ {:.2f}!".format(0.45 * d))