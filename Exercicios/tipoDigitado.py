algo = input("Digite algo: ")
print("O tipo digitado é ", type(algo))
print("Só tem espaços? ", algo.isspace())
print("É um número? ", algo.isnumeric())
print("É alfabético? ", algo.isalpha())
print("É alfanumérico? ", algo.isalnum())
print("Está em maiusculas? ", algo.isupper())
print("Está em minúsculas? ", algo.islower())
print("Está capitalizada? ", algo.istitle())