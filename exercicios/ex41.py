sal = float(input('digite seu salario: '))
if sal <= 1250:
    reaj = ((sal/20)* 3)+ sal
else:
    reaj =((sal/20)*2)+sal
print('seu salario atual e ', reaj)