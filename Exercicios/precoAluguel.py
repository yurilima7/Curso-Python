km = float(input("Digite a quantidade de KM percorridos com o carro: "))
qtdDias = int(input("Digite a quantidade de dias em que o carro foi alugado: "))

precoPagamento = (60 * qtdDias) + (0.15 * km)

print("O pagamento deve ser de: R$ {:.2f}".format(precoPagamento))