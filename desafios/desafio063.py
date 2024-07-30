n =int( input(" Digite Quantos termos você deseja :"))
t1 = 0
t2 = 1
t3 = 0

while t3 <= n:
    print("{}.".format(t3))
    t3 = t1 + t2
    t1 = t2
    t2 = t3

print( " Fim ")