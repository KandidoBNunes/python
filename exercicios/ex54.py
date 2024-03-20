def eh_par(numero):
    return numero % 2 == 0

digitos = input("Digite 6 dígitos separados por espaço: ")
digitos = digitos.split()

soma_pares = 0

for digito in digitos:
    numero = int(digito)
    if eh_par(numero):
        soma_pares += numero

print("A soma dos números pares é:", soma_pares)