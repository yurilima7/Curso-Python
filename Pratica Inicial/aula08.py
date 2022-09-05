from math import sqrt
import random

num = int(input("Digite um número: "))
num2 = random.randint(1, 10)

raiz = sqrt(num)

print("Raiz Quadrada de {} é igual a {:.2f}".format(num, raiz))
print(num2)