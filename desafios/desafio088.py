from ast import While
from random import randint
from time import sleep

numeros = []
aleatorio = j = 0

print('-'*40)
print(f'{'JOGA NA MEGA SENA':^40}')
print('-'*40)

count = int(input('Quantos jogos você quer eu sorteie? '))
print(f'{f' SORTEANDO {count} JOGOS ':=^40}')

for i in range(0, count):
    while len(numeros) < 6:
        aleatorio = randint(1, 60)
        j = 0
        if len(numeros) == 0:
            numeros.append(aleatorio)
        else:
            while j < len(numeros):
                if aleatorio != numeros[j]:
                    j += 1
                else:
                    aleatorio = randint(1, 60)
                    j = 0
            numeros.append(aleatorio)
    numeros.sort()
    sleep(1)
    print(f'Jogo {i+1}: {numeros}')
    numeros.clear()
print(f'{'< BOA SORTE! >':=^40}')
