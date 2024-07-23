print('--Calculadora--')
n1 = int(input('\nDigite um numero: '))
n2 = int(input('\nDigite outro numero: '))
escolha = ''
while escolha != 5:
    escolha = int(input(
        '\n\n[1] Somar\n[2] multiplicar\n[3] maior\n[4] novos Números\n[5] Sair do Programa\n'))
    if escolha == 1:
        s = n1 + n2
        print("\nA soma de {} e {} se resulta em: {}".format(n1, n2, s))
    elif escolha == 2:
        s = n1 * n2
        print("\nA Multiplicação entre {} e {} se resulta em: {}".format(n1, n2, s))
    elif escolha == 3:
        if n1 > n2:
            print('o Numero: {} é maior'.format(n1))
        else:
            print('o Numero: {} é maior'.format(n2))
    elif escolha == 4:
        n1 = int(input('\nDigite um numero: '))
        n2 = int(input('\nDigite outro numero: '))
    elif escolha == 5:
        print('Saindo do Programa...')
    else:
        print('\nEscreva um valor correto')
