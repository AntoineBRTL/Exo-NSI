from ..Part1.Exo6 import Noeud
from ..Part1.Exo4 import str_arbre
from .Exo3 import supprime

def ajoute(x, a):
    if a is None:
        return Noeud(None, x, None)
    elif x < a.valeur:
        return Noeud(ajoute(x, a.gauche), a.valeur, a.droit)
    return Noeud(a.gauche, a.valeur, ajoute(x, a.droit))

def appartient(x, a):
    if a is None:
        return False
    elif x < a.valeur:
        return appartient(x, a.gauche)
    elif x > a.valeur:
        return appartient(x, a.droit)
    return True

def taille(a):
    if a is None:
        return 0
    return 1 + taille(a.gauche) + taille(a.droit)

def hauteur(a):
    if a is None:
        return 0
    return 1 + max(hauteur(a.gauche), hauteur(a.droit))

class ABR:
    def __init__(self):
        self.racine = None

    def __contains__(self, x):
        return appartient(x, self.racine)

    def ajouter(self, x):
        self.racine = ajoute(x, self.racine)

    def taille(self):
        return taille(self)

    def hauteur(self):
        return hauteur(self)

    def __str__(self):
        return str_arbre(self)

    def supp(self, x):
        return supprime(x, self)