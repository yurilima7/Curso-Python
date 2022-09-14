nome = str(input("Digite o nome de uma pessoa: "))
n = nome.split()

print("Maiúscula: {}".format(nome.upper().strip()))
print("Minúscula: {}".format(nome.lower().strip()))
print("Nome tem {} letras".format(len(nome.strip()) - nome.count(' ')))
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))
print("Seu primeiro nome é: {}".format(n[0]))
print("Seu último nome é: {}".format(n[len(n) - 1]))