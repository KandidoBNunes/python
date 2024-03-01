km_percorridos = float(input("Digite a quantidade de Km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias pelo qual o carro foi alugado: "))
preco_total = (60 * dias_alugados) + (0.15 * km_percorridos)
print("O preço a pagar é R${:.2f}".format(preco_total))