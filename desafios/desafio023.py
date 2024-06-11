# Matematicamente
num = int(input("Digite Um Número (0 até 9999): "))

milhar = num // 1000
centena = num//100 - milhar * 10
dezena = num//10 - (milhar * 100 + centena * 10)
unidade = num//1 - (milhar * 1000 + centena * 100 + dezena*10)
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(
    unidade, dezena, centena, milhar))

# Manipulação em string

num = str(num)
print('\nUnidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(
    num[1:2], num[2:3], num[1:2], num[0:1]))
