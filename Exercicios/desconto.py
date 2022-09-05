preco = float(input("Digite o preço de um produto: "))

novoPreco = preco - (preco * 0.05)

print("O preço com desconto é R$ {:.2f}".format(novoPreco))