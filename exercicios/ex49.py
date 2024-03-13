alt = float(input('qual a sua altura? '))
peso = float(input('qual seu peso? '))
imc = peso / (alt**2)
print(imc)
if imc < 18.5:
    print('vc ta abaixo do peso')
elif 18.5 <= imc<25:
    print('vc ta no peso ideal')
elif 25 <=imc<30:
    print('vc ta com sobre peso')
elif 30<=imc< 40:
    print('vc ta obeso')
else:
    print('vc ta morbidamente obeso')