num = int(input('me diga um numero o qual vc quer a tabuada: '))
for c in range(1,11):
    print('{} X {:2} = {}'.format(num,c, num*c))