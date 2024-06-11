from math import pow, sqrt
co = int(input("Escreva o Valor do Cateto Oposto: "))
ca = int(input("Escreva o Valor do Cateto Adjacente: "))
h2 = pow(co, 2)+pow(ca, 2)
h2 = sqrt(h2)
print("O comprimento da hipotenusa é igual: {:.2f}".format(h2))
