from ..Part1.Exo6 import Noeud

# tout a gauche

def minimum(a):
    if a is None or a.gauche is None:
        return a

    return minimum(a.gauche)

def supprime_min(a):
    if a.gauche is None:
        return a.droit
    else:
        return Noeud(supprime_min(a.gauche), a.valeur, a.droit)

def supprime(x, a):
    if a is None:
        return None

    elif x < a.valeur:
        return Noeud(supprime(x, a.gauche), a.valeur, a.droit)
    elif x > a.valeur:
        return Noeud(a.gauche, a.valeur, supprime(x, a.droit))

    elif a.droit is None:
        return a.gauche
    else:
        return Noeud(a.gauche, minimum(a.droit), supprime_min(a.droit))
        