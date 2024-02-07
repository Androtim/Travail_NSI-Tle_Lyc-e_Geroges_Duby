# Créé par BEGHIN, le 18/12/2023 en Python 3.7

import bisect
import matplotlib.pyplot as plt

class ArbreHuffman:
    def __init__(self, lettre, nbocc, g=None, d=None):
        self.lettre = lettre
        self.nbocc = nbocc
        self.gauche = g
        self.droite = d

    def est_feuille(self) -> bool:
        return self.gauche == None and self.droite == None

    def __lt__(self, other):
        return self.nbocc > other.nbocc


def parcours(arbre, chemin_en_cours, dico):
    if arbre is None:
        return
    if arbre.est_feuille():
        dico[arbre.lettre] = chemin_en_cours
    else:
        parcours(arbre.gauche, chemin_en_cours + [0], dico)
        parcours(arbre.droite, chemin_en_cours + [1], dico)


def fusionne(gauche, droite) -> ArbreHuffman:
    nbocc_total = gauche.nbocc + droite.nbocc
    return ArbreHuffman(None, nbocc_total, gauche, droite)

def compte_occurence(texte: str) -> dict:
    occ = dict()
    for car in texte:
        if car.isalfa():
            if car not in occ:
                occ[car] = 0
            occ[car] += 1
    return occ


def construit_liste_arbres(texte: str) -> list:
    dic_occurences = compte_occurence(texte)
    liste_arbres = []
    for lettre, occ in dic_occurences.items():
        liste_arbres.append(ArbreHuffman(lettre, occ))
    return liste_arbres


def codage_huffman(texte: str) -> dict:
    liste_arbres = construit_liste_arbres(texte)
    liste_arbres.sort
    while len(liste_arbres) > 1:
        droite = liste_arbres.pop()
        gauche = liste_arbres.pop()
        new_arbre = fusionne(gauche, droite)
        bisect.insort(liste_arbres, new_arbre)

    arbre_huffman = liste_arbres.pop()
    dico = {}
    parcours(arbre_huffman, [], dico)
    return dico



def est_vide(t):
    return t == None

def hauteur(t):
    if est_vide(t):
        return 0
    else:
        _, t1, t2 = t
        return max([hauteur(t1), hauteur(t2)]) + 1



# PARTIE 2
def draw_tree_aux (t, rect, dy ,labels=False):
    if est_vide(t):
        return
    x1, x2, y1, y2 = rect
    xm=(x1+x2)//2
    x,t1,t2 = t
    draw_tree_aux(t1,(x1,xm,y1,y2-dy),dy,labels)
    draw_tree_aux(t2,(xm,x2,y1,y2-dy),dy,labels)
    if labels==True:
        plt.text(xm+10,y2,str(x), fontsize=10, \
        horizontalalignment='left', verticalalignment='top')
    if not est_vide(t1):
        a,b = ((xm,(x1+xm)//2),(y2,y2-dy))
        plt.plot(a,b,'k',marker='s')
    if not est_vide(t2):
        c,d=((xm,(x2+xm)//2),(y2,y2-dy))
        plt.plot(c,d,'k',marker='s')

def draw_tree(t, labels=False):
    d=512
    pad=20
    h = hauteur(t)
    if h == 0:
        dy = 1
    else:
        dy = (d-2*pad)/h
    draw_tree_aux(t,(pad,d-pad,pad,d-pad),dy,labels)
    plt.axis([0,d,0,d])
    plt.axis('off')
    plt.show()






with open ("petitchaperonrouge.txt") as f:
    text = f.read()

print(), print(), print()
test = codage_huffman(text)
print(), print(), print()
print(test)
print(), print(), print()
draw_tree(test)

