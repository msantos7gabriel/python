from random import randint
from time import sleep

jogadores = {}
jogadores_ordenados = {}
print('Valores sorteados:')
for i in range(1, 5):
    jogadores[f'jogador{i}'] = randint(1, 6)
    print(f'    O Jogador{i} tirou {jogadores[f'jogador{i}']}')
    sleep(1)
print('Ranking dos Jogadores: ')
print(sorted(jogadores.items(), reverse=True))

for i in sorted(jogadores, key=jogadores.get, reverse=True):
    jogadores_ordenados[i] = jogadores[i]
i = 0
for k, v in jogadores_ordenados.items():
    print(f'{i+1}° Lugar: {k} com {v}')
    i += 1
    sleep(1)
