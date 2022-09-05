n = int(input("Digite o número da tabuada desejada: "))

print("{:*^13}".format("TABUADA"))

for i in range(11):
    print("{} + {} = {}".format(n, i, n + i))