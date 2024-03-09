import random
num = random.randint(0,5)
valor = int(input('me diga um numero de 1 a 5 :'))
if num == valor:
    print('eu estava pensando no número', num, ', você ganhou!')
else: 
    print('Número errado, você perdeu! O número correto era', num)
print('pensei no numero',num)