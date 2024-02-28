n = input("Digite algo: ")
tipo = type(n).__name__
if tipo == 'str':
    if n.isdigit():
        info_adicional = "É um número inteiro."
    elif n.replace('.', '', 1).isdigit():
        info_adicional = "É um número decimal."
    else:
        info_adicional = "É uma string."
elif tipo == 'int':
    info_adicional = "É um número inteiro."
elif tipo == 'float':
    info_adicional = "É um número decimal."
else:
    info_adicional = "É de um tipo primitivo diferente."
print("O tipo primitivo do que você digitou é:", tipo)
print("Informações adicionais:", info_adicional)
