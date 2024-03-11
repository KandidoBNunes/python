num = input("Digite uma lista de números separados por espaços: ")
nume = [int(x) for x in num.split()]
menornum = min(num)
maiornum = max(num)
print("O menor número é:", menornum)
print("O maior número é:", maiornum)