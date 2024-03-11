ano=int(input('qual ano quer analizar?? '))
anob=ano%4
if anob==0:
    print('esse ano e bisexto')
else:
    print('esse ano nao e bisexto')