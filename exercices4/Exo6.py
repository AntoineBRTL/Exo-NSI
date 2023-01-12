from Liste import Cellule

def identiques(c1, c2):
    if (c1 is None and c2 is not None) or (c2 is None and c1 is not None):
        return False

    if c1 is None and c2 is None:
        return True

    return c1.valeur == c2.valeur and identiques(c1.suivante, c2.suivante)

c = Cellule(1, None)
c.suivante = Cellule(2, None)
c.suivante.suivante = Cellule(3, None)

c2 = Cellule(1, None)
c2.suivante = Cellule(2, None)
c2.suivante.suivante = Cellule(3, None)
c2.suivante.suivante.suivante = Cellule(4, None)

print(identiques(c, c2))