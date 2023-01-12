from Liste import Cellule

def recursiveOccurence(x, c):
    if c is None:
        return 0

    if c.valeur == x:
        return 1 + recursiveOccurence(c.suivante)

    return recursiveOccurence(c.suivante)

def boucleOccurence(x, rc):
    c = rc
    o = 0
    while c is not None:
        if c.valeur == x:
            o += 1

        c = c.suivante
    return o