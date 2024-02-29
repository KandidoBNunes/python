nome = input('qual seu nome?')
print('prazer em te conhecer {:=^20}!'.format(nome))

#####################################

n1 = int(input('um valor: '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma e {}, o produto e {} e a divisao e {}'.format(s,m,d))
print('divisao inteira e {} e potencia {}'.format(di, e))