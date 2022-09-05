from math import cos, sin, tan, radians

angulo = float(input("Digite o valor do ângulo: "))

cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))
print("\nO ângulo de {:.2f} apresenta:\nCosseno = {:.2f}\nSeno = {:.2f}\nTangente = {:.2f}".format(angulo, cosseno, seno, tangente))