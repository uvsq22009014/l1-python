def syracuse(n):
    """ Retourne la liste des valeurs de la suite en partant de n jusqu'à 1 """

    listeN = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            listeN.append (n)
        else:
            n = n * 3 + 1
            listeN.append(n)

    return listeN

#print(syracuse(3))


def testeConjecture(n_max):
    """ Teste la conjecture de Collatz pour toutes les valeurs de 2 à n_max """
    
    for i in range (2, n_max + 1) :
        syracuse (i)
    return "Comjecture verifiée jusqu'à n = " + str(n_max)

#print(testeConjecture(10000))


def tempsVol(n):
    """ Retourne le temps de vol de n """
    
    return len(syracuse(n)) - 1

#print("Le temps de vol de", 3, "est", tempsVol(3))

def tempsVolListe(n_max):
    """ Retourne la liste de tous les temps de vol de 1 à n_max """
    liste = [1]
    for i in range (1, n_max + 1) :
        liste.append(tempsVol(i))
    return liste

#print(tempsVolListe(100))

tvl = tempsVolListe(10000)
m = max(tvl)
print(tvl.index(m), "a un temps de vol de", m)


### fin sur le fichier du prof syracuseprof.py ###