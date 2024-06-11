import math
angulo = float(input('Escreva o Angulo: '))
seno = math.sin(angulo)
cosseno = math.cos(angulo)
tangente = math.tan(angulo)

print('O Angulo: {} tem seu Seno de: {}, Seu Cosseno de: {}, e Sua Tangente {}'.format(
    angulo, seno, cosseno, tangente))
