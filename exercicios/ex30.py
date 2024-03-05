city = input('digite o nome da sua cidade: ')
cida = city.lower()
tem =  'santo' in cida
tem2 = 'sao' in cida
if(tem or tem2 == True):
    print('sua cidade tem Santo no nome')
else:
    print('sua cidade nao tem santo no nome')