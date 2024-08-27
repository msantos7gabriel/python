from random import randint
valores = (randint(1, 9), randint(1, 9), randint(
    1, 9), randint(1, 9), randint(1, 9))

menor = valores[0]
maior = valores[0]

print('Os valores sorteados foram', end=' ')
for i in range(0, len(valores)):
    print(valores[i], end=' ')
    if valores[i] > maior:
        maior = valores[i]
    if valores[i] < menor:
        menor = valores[i]
print(f'\nO Maior valor sorteado foi {maior}')
print(f'O Menor valor sorteado foi {menor}')
