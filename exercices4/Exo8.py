from Liste import Cellule
from Exo7 import inserer

def triParInsertion(cellule):
    if cellule is None:
        return None

    cellule = inserer(cellule.valeur, cellule.suivante)
    return Cellule(cellule.valeur, triParInsertion(cellule.suivante))

c = Cellule(3, None)
c.suivante = Cellule(2, None)
c.suivante.suivante = Cellule(18, None)
c.suivante.suivante.suivante = Cellule(8, None)
c.suivante.suivante.suivante.suivante = Cellule(4, None)

#print(triParInsertion(c))