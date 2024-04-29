primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

print("Os 10 primeiros termos da PA são:")
for i in range(10):
    termo = primeiro_termo + i * razao
    print(termo, end=" ")