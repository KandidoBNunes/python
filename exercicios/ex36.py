vel=int(input('qual a sua velocidade?'))
multa = (vel-80) * 7
if vel >= 80:
    print ('multado em {} reais!!' .format(multa))
else:
    print('continue a viagem bom senhor...')