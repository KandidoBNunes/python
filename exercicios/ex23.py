opost = float(input('digite o valor do cateto oposto: '))
adjc = float(input('digite o valor do cateto adjacente: '))
hipo = (opost ** 2 + adjc**2) ** 0.5
print('a hipotenusa e {:.5f}'.format(hipo))