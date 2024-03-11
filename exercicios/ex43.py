a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < menor:
    menor = b
if c < menor:
    menor = c
maior = a
if b > maior:
    maior = b
if c > maior:
    maior = c
print('O menor valor digitado foi', menor)
print('O maior valor digitado foi', maior)
