from calendar import c
from Liste import Cellule

def recursiveTrouve(x, c):
    if c is None:
        return None

    if c.valeur == x:
        return 0

    n = recursiveTrouve(x, c.suivante)

    if(n is None):
        return None

    return 1 + n

def boucleTrouve(x, rc):
    rc = c
    r = 0
    while c is not None:
        if rc.valeur == x:
            return r
        r += 1
        rc = c.suivante
    return r