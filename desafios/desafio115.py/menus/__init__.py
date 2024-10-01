def titulo(texto):
    print('-'*45)
    print(f'{texto:^45}')
    print('-'*45)


def cad_pessoas():
    titulo('NOVO CADASTRO')
    while True:
        try:
            nome = str(input('Nome: ')).title().strip()
            break
        except:
            print('\033[0;31mERROR! Digite um número inteiro válido.\033[m')
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except:
            print('\033[0;31mERROR! Digite um número inteiro válido.\033[m')

    with open('nomes.txt', 'a', encoding='utf8') as names:
        names.write(f'\n{nome}')

    with open('idade.txt', 'a') as age:
        age.write(f'\n{idade} anos')

    print(f'Novo registro de {nome} adicionado.')


def lista_pessoas():
    titulo('PESSOAS CADASTRADAS')
    with open('nomes.txt', 'r', encoding='utf8') as nome:
        nomes_lista = nome.readlines()

    with open('idade.txt', 'r') as idade:
        idade_lista = idade.readlines()

    for i in range(len(nomes_lista)):
        print(f'{nomes_lista[i].replace('\n', ''):<30}{idade_lista[i]}', end='')
    print()


def sair_sys():
    titulo('Saindo do sistema... Até logo!')


def menu():
    while True:
        titulo('MENU PRINCIPAL')
        print('\033[0;33m1 - \033[m\033[0;34mVer Pessoas cadastradas\033[m')
        print('\033[0;33m2 - \033[m\033[0;34mCadastrar nova Pessoa\033[m')
        print('\033[0;33m3 - \033[m\033[0;34mSair do Sistema\033[m')
        print('-'*45)
        try:
            n = int(input('\033[0;32mSua Opção: \033[m'))
            if n == 1:
                lista_pessoas()
            elif n == 2:
                cad_pessoas()
            elif n == 3:
                sair_sys()
                break
            else:
                print('\033[0;31mERROR! Digite uma opção válida!\033[m')
        except:
            print('\033[0;31mERROR! Digite uma opção válida!\033[m')
