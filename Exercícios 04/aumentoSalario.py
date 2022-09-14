from pickle import TRUE


sal = float(input("Digite o seu salário: "))

if sal > 1250:
    print("Novo salário = R$ {:.2f}".format(sal * 1.10))
else :
    print("Novo salário = R$ {:.2f}".format(sal * 1.15))
    