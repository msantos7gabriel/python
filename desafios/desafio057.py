sexo = ''
while sexo != 'S' and sexo != 'M':
    sexo = str(input("Qual seu sexo [M/F]: ")).upper()
    if sexo != 'S' and sexo != 'M':
        print('\nPor Favor insira corretamente\n')
