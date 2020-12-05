def fonctionValeurs(n) :
    ''' fonction qui affiche quatre fois la valeur de son argument moins 2 si l'argument est supérieur à 1 et qui affiche -2 sinon.'''
    if n > 1 :
        print(4 * n - 2)
    else :
        print(-2)
    pass

#print (fonctionValeurs(3))
#help(fonctionValeurs)


var_glob = 9
n = 0
def division(var_loc) :
    '''fonction qui retourne la division entière de var_glob et var_loc.'''
    n = var_glob / var_loc
    return n 

#print(division(2))


def fonctionTemps(heure, jour, annee) :
    heure = 0
    annee = 2020
    minute = heure // 60
    print("année :", annee, "jour :", jour, "minute :", minute)
    pass

#print(fonctionTemps(jour = 1, heure = 3))
