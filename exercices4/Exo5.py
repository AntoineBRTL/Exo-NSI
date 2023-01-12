from Liste import Cellule

def concatenerInverse(c1, c2):
    if c1 is None:
        return c2
    return concatenerInverse(c1.suivante, Cellule(c1.valeur,c2))

def inverser(c):
    return concatenerInverse(c, None)

c = Cellule(1, None)
c.suivante = Cellule(2, None)
c.suivante.suivante = Cellule(3, None)

c2 = Cellule(18, None)
c2.suivante = Cellule(29, None)
c2.suivante.suivante = Cellule(40, None)

print(concatenerInverse(c, c2))
print(inverser(c))