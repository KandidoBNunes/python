ano = int(input('\033[96mEm que ano estamos? \033[0m'))
jov = int(input('\033[96mEm que ano você nasceu? \033[0m'))

if ano - jov > 18:
    print('\033[92mVocê não precisa se alistar... ainda!\033[0m')
elif ano - jov == 18:
    print('\033[93mVocê precisa se alistar o mais rápido possível!!!\033[0m')
elif ano - jov < 18:
    print('\033[92mVocê já se alistou, pode descansar.\033[0m')
else:
    print('\033[91m---ERRO---\033[0m')
