val1 = float(input('\033[95mMe diga o primeiro valor: \033[0m'))
val2 = float(input('\033[92mMe diga o segundo valor: \033[0m'))

if val1 > val2:
    print('\033[95m{} o primeiro valor é maior que {} o segundo valor!\033[0m'.format(val1, val2))
elif val2 > val1:
    print('\033[92m{} o segundo valor é maior que {} o primeiro valor!\033[0m'.format(val2, val1))
else:
    print('\033[93m {} e {} tem algo em comum os dois valores são iguais!\033[0m'.format(val1, val2))
