frase = str(input('Escreva uma palavra: ')).strip()

frase_nova = []

for i in range(0, len(frase)):
    if frase[i] == frase[-(i + 1)]:
        palíndromo = True
    else:
        palíndromo = False
        break

if palíndromo == True:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
