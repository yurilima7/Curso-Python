print('{:=^30}'.format("Menu"))
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

s = n1 + n2
m = n1 * n2
d = n1 / n2
dI = n1 // n2
e = n1 ** n2

print("\nSOMA = {}\nMULTIPLICAÇÃO = {}\nDIVISÃO = {:.2f}".format(s,m,d))
print("DIVISÃO INTEIRA = {}\nPOTÊNCIA {}".format(dI, e))