n = 30
nb_de_divisions = 0

while n != 0 :
    nb_de_divisions += 1
    n = n - (n / 2)
print(n)
print(nb_de_divisions)

#nombre minimum de fois ou il faut diviser n par 2 pour obtenir 0