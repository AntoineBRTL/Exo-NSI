from Liste import Cellule

# Bon algo
def inserer(x, cellule):
    
    if cellule is None or cellule.valeur >= x:
        return Cellule(x, cellule)

    return Cellule(cellule.valeur, inserer(x, cellule.suivante))

c = Cellule(1, None)
c.suivante = Cellule(2, None)
c.suivante.suivante = Cellule(4, None)

#print(inserer(8, c))