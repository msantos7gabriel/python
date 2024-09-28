from datetime import date

print('-'*30)
nascimento = int(input('Em quem ano você nasceu? '))
hj = date.today().year
idade = hj - nascimento


def voto(idade):
    if 18 <= idade <= 70:
        return 'OBRIGATÓRIO'
    elif 16 >= idade < 18 or idade > 70:
        return 'OPCIONAL'
    else:
        return 'NEGADO'


print(f'Com {idade} anos: VOTO {voto(idade)}.')
