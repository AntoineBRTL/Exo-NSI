from .Exo6 import Noeud
from .Exo4 import str_arbre

def parfait(h):
    if(h == 0):
        return None
    return Noeud(parfait(h - 1), h, parfait(h - 1))