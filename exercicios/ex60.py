primeiro = int(input('\033[35mPrimeiro termo: \033[m'))

razao = int(input('\033[32mRazão: \033[m'))

decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('\033[34m{}\033[m'.format(c), end='→')

print('\033[31mACABOU\033[m')