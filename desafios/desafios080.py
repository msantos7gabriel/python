num = []

for i in range(0, 5):
    j = len(num)
    count = 0
    numeros = int(input('Digite um valor: '))
    while True:
        if len(num) == 0:
            count = len(num)
            j = len(num)
        else:
            if num[count] <= numeros:
                count += 1
            if num[j-1] > numeros:
                j -= 1
        if j == count:
            break
    num.insert(count, numeros)
    if count == len(num)-1:
        print('Adicionado ao final da lista...')
    else:
        print(f'Adicionado na posição {count} da lista...')
print('-='*30)
print(f'Os Valores Digitados em ordem foram {num}')   
