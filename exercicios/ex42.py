a = float(input('Digite o valor de um lado do triângulo: '))
b = float(input('Digite o valor de outro lado do triângulo: '))
c = float(input('Digite o valor do último lado do triângulo: '))
if a + b > c and b + c > a and c + a > b:
    print('É possível formar um triângulo.')
else:
    print('Não é possível formar um triângulo.')