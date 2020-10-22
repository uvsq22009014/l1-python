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

def demandeTemps():
    jour = int(input("nombre de jours "))
    heure = int(input("nombre d'heures "))
    minute = int(input("nombre de minutes "))
    seconde = int(input("nombre de secondes `"))
    # à terminer pour tenir compte des bornes
    return jour, heure, minute, seconde

afficheTemps(demandeTemps())