from random import randint
from time import sleep
jog = ('pedra','papel','tesoura')
computador = randint(0,2)
print('''suas opcoes
      [0] pedra
      [1]papel
      [2]tesoura''')
jogador=int(input('qual a sua jogada? '))
print('-='*15)
print('PEDRA!!')
sleep(1)
print('PAPEL!!')
sleep(1)
print('TESOURA!!')
sleep(1)
print('-='*15)
print('o computador jogou {}'.format(jog[computador]))
print('vc jogou {}'.format(jog[jogador]))
print('-='*15)
if computador == 0 :
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR GANHOU!')
    elif jogador ==2:
        print('COMPUTADFOR GANHOU!')
elif computador == 1:
    if jogador == 0:
         print('COMPUTADFOR GANHOU!')
    elif jogador == 1:
          print('EMPATE!')
    elif jogador ==2:
        print('JOGADOR GANHOU!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU!')
    elif jogador == 1:
         print('COMPUTADFOR GANHOU!')
    elif jogador ==2:
          print('EMPATE!')
print('-='*15)
print('FIM DA PARTIDA')
print('-='*15)