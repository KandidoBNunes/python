import random

ops1 = input(' me diga a uma das opcoes: ')
ops2 = input(' me diga a uma das opcoes: ')
ops3 = input(' me diga a uma das opcoes: ')
ops4 = input(' me diga a uma das opcoes: ')
ops5 = input(' me diga a uma das opcoes: ')

opsf = [ops1 , ops2 , ops3 , ops4 , ops5]

random.shuffle(opsf)
print('o escolhido é {} '.format(opsf))