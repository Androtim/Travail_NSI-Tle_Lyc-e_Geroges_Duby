def CREER_LISTE_VIDE():

    liste = [None]*33
    liste[0] = 0

    return liste

def INSERER(L, element, index):

    if ((L[0] == len(L)) or (i-1>L[0])):
        print("La liste est déjà pleine ou alors le rang n'est pas correct.")

        return False
    
    else:
        for k in range (L[0]+1, index, -1):
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
    
def MODIFIER(l, i, element):

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
        for k in range (1, len(L)):
            affichage += " " + str(k)

        print("Voici la liste d'éléments utilisés :" + affichage)
        return True
