a = str(input("Digite um nome: ")).strip()
print("Letra 'A' aparece {} vez(es)".format(a.upper().count('A')))
print("Letra 'A' aparece pela primeira vez na posição: {}".format(a.upper().find('A')+1))
print("Letra 'A' aparece pela última vez na posição: {}".format(a.upper().rfind('A')+1))