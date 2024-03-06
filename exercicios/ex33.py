nome = input('digite seu nome: ')
nome = nome.upper()
nome = nome.split()
print("""seu primeiro nome e {}
     seu ultimo nome e {}""".format(nome[0],nome[-1],))