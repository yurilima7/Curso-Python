altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))

area = altura * largura
tinta = area / 2

print("Para pintar esta parede serão necessários {} litros de tintas".format(tinta))