def eh_palindromo(frase):
    frase = frase.replace(" ", "").lower()
    n = len(frase)   
    for i in range(n // 2):
        if frase[i] != frase[n - i - 1]:
            return False
    return True
frase = input("Digite uma frase: ")
if eh_palindromo(frase):
    print("A frase é um palíndromo.")
else:
    print("A frase não é um palíndromo.")