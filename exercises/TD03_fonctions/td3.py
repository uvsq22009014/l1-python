#temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(temps):
    """ Renvoie la valeur en secondes d'un temps donné en jour, heure, minute, seconde."""
    sec = 0
    sec += temps[0] * 24 * 60 * 60
    sec += temps[1] * 60 * 60
    sec += temps[2] * 60
    sec += temps[3] 
    return sec 

#temps = (3,23,1,34)
#print(type(temps))
#print(tempsEnSeconde(temps))   

def secondeEnTemps(seconde):
    """Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jours = seconde // (24 * 60 * 60)
    seconde = seconde % (24 * 60 * 60)
    heures = seconde // (60 * 60)
    seconde = seconde % (60 * 60)
    minutes = seconde // 60
    seconde = seconde % 60
    return jours, heures, minutes, seconde
    
#temps = secondeEnTemps(100000)
#print(temps[0],"jours",temps[1],"heures",temps[2],"minutes",temps[3],"secondes")
#print(tempsEnSeconde(temps))

def affichePluriel(valeur, unite) :
    """fonction qui affiche le nombre d'unités (heures, jours, ...) avec le pluriel ou 0 pris en compte"""
    if valeur > 1 :
        print(valeur, unite + "s", end = " ")
    elif valeur == 1 :
        print(valeur, unite, end = " ")

def afficheTemps(temps):
    affichePluriel(temps[0], "jour")
    affichePluriel(temps[1], "heure")
    affichePluriel(temps[2], "minute")
    affichePluriel(temps[3], "seconde")
    print()

#afficheTemps((1,0,14,23))  


def verifieTemps (temps) :
    # vérifie que le temps saisi par l'utilisateur est correct

    #jours, heures, minutes, secondes = temps
    _, heures, minutes, secondes = temps

    # si heures > un jour
    # si minutes > une heure
    # secondes > une minute
   
    if (heures >= 24) or (minutes >= 60) or (secondes >= 60):
       return (False)
    else :
        return (True)


def demandeTemps():

    jours, heures, minutes, secondes = 0, 0, 0, 9999

    while not verifieTemps((jours, heures, minutes, secondes)):
        jour = int(input("nombre de jours "))
        heure = int(input("nombre d'heures "))
        minute = int(input("nombre de minutes "))
        seconde = int(input("nombre de secondes "))
    return jour, heure, minute, seconde


#temps = demandeTemps()
#afficheTemps(temps)

#probleme : re-demande toujours un temps même quand il est valide

#pareil que :  afficheTemps(demandeTemps())


def sommeTemps(temps1,temps2):

    secondes = tempsEnSeconde(temps1) + tempsEnSeconde(temps2)
    return secondeEnTemps(secondes)

#print(sommeTemps((2,3,4,25),(5,22,57,1)))


def proportionTemps(temps,proportion):
    secondes = tempsEnSeconde(temps) * proportion
    return secondeEnTemps(secondes)
    
#afficheTemps(proportionTemps((2,0,600,0),1))
#afficheTemps(proportionTemps(proportion = 10, temps = ))
#appeler la fonction en échangeant l'ordre des arguments


def bissextile(annee) :

    if (annee % 400 == 0) :
        return True
    elif (annee % 4 == 0) and (annee % 100 == 0) :
        return False
    elif (annee % 4 == 0) :
        return True
    else :
        return False


def tempsEnDate(temps: int):

    jours, heures, minutes, secondes = temps

    annee = jours // 365
    jours %= 365

    moisAnnee = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if bissextile(annee + 1970):
        moisAnnee[1] = 29

    
    mois = 0
    while jours >= moisAnnee[mois] :
        jours -= moisAnnee[mois]
        mois += 1
    mois += 1

    return(annee, mois, jours, heures, minutes, secondes)

    #date origine : 1 Jan 1970


def afficheDate(date = -1):
    affichePluriel(date[0], "annee")
    print(date[1], "mois", end = " ")
    afficheTemps((date[2], date[3], date[4], date[5]))
    
temps = secondeEnTemps(1000000000)
afficheTemps(temps)
afficheDate(tempsEnDate(temps))
afficheDate()
