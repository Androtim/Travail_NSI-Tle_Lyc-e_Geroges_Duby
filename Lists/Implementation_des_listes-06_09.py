def CREER_LISTE_VIDE():

    #nombre = int(input("Combien de charactères dans la liste?"))
    liste = [None]*33
    liste[0] = 0

    return liste

def INSERER(L, element, i):

    if ((L[0] == len(L)) or (i-1>L[0])):
        print("La liste est déjà pleine ou alors le rang n'est pas correct.")

        return False

    else:
        for k in range (L[0]+1, i, -1):
            L[k] = L[k-1]
        L[i] = element
        L[0] = L[0]+1

        return True

def SUPPRIMER(L, i):

    if ((L[0] != 0) and i <= L[0]):
        for k in range (i, L[0], 1):
            L[k] = L[k+1]
        L[0] = L[0] -1

        return True

    else:
        print("La liste est déjà vide ou alors l'index n'est pas correct.")

        return False

def MODIFIER(L, i, element):

    if element == None:
        L[i] = element

    else:
        if i == 0 or i > L[0]:
            print("La liste ne possède pas d'élément d'indice" ,i + ".")

            return False

        else:
            L[i] = element

            return True

def RECHERCHER(L, element):

    if L[0] == 0:
        print("La liste est vide.")

        return False

    else:
        position = []
        for k in range (1, len(L)):
            if L[k] == element:
                position += [k]
            elif len(position) > 0:
                return position
            else:
                return False

def LIRE(L, i):

    if i == 0 or i > L[0]:
        print("La liste ne possède pas d'élément d'indice" ,i + ".")
        return False

    else:
        print("L'élément d'indice",i,"est :", L[i])
        return True

def AFFICHER(L):

    if L[0] == 0:
        print("La liste est vide.")

        return False

    else:
        affichage = ""
        for k in range (1, L[0] + 1):
            affichage += str(L[k])
            if k != L[0]:
                affichage += ", "

        print("Voici la liste d'éléments utilisés :" , affichage)
        return True

def INVERSER(L):

    if L[0] == 0:
        print("La liste est vide, impossible d'inverser")

    else:
        L2 = []
        if L[0] > 0:
            ListeNone = [None]*(len(L) - 1 - L[0])
            L2.append(L[0])
            longeur = L[0]
            while longeur > 0:
                L2.append(L[longeur])
                longeur -= 1

    return L2, True


#def Utiliser_les_fonctions():
#    Personne = True
#    while Personne == True:

def UTILISER():
    liste1 = CREER_LISTE_VIDE()
    INSERER(liste1, 2, 1)
    INSERER(liste1, 5, 1)
    INSERER(liste1, 3, 1)
    AFFICHER(liste1)
    liste1, resultat = INVERSER(liste1)
    AFFICHER(liste1)
    print(liste1)
