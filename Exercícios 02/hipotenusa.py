from math import hypot

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

#hipotenusa = (pow(ca, 2) + pow(co, 2)) ** (1/2)
hipotenusa = hypot(co, ca)

print("HIPOTENUSA = {:.2f}".format(hipotenusa))