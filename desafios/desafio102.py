
def fatorial(n, show=False):
    """-> Gera um fatorial de um número.

    Args:
        n (int): O número a ser calculado.
        show (bool, optional): Mostra ou não a conta. Defaults to False.
    """
    fat = n
    for i in range(n, 1, -1):
        fat *= (i-1)

    if show == True:
        for i in range(n, 1, -1):
            print(i, end=' x ')
        print(f'1 = {fat}')
    else:
        print(fat)


print('-'*30)
fatorial(5, True)
fatorial(5)
