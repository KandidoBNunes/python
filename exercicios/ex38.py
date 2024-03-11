km = int(input('quanto vc quer viajar???'))
valor = 0
if km <= 200:
    valor = km * 0.5
else: 
    valor = km * 0.45
print('sua viajem vai custar {}'.format(valor))