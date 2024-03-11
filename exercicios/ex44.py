emp = float(input('\033[95mQual valor quer financiar? \033[0m'))
sal = float(input('\033[95mQual o seu salário? \033[0m'))
anos = int(input('\033[95mEm quantos anos? \033[0m')) * 12

if (sal/10*3) >= (emp/anos):
    print('\033[92mOK, nós fazemos o financiamento!\033[0m')
else:
    print('\033[91mInfelizmente não podemos financiar esse valor!\033[0m')
