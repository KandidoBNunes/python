a = input('digite uma frase: ')
ac = a.count('a')
ua = a.rfind('a')
pa = a.find('a')
print(""" sua fra se tem {} azes???
    e o primeiro dos `azes ` esta em {}
    enquanto o ultimo esta em {}""".format(ac,ua,pa))