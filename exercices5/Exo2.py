class Cellule:
    def __init__(self, v, s):
        self.v = v
        self.s = s

class Pile:
    def __init__(self):
        self._contenu = None

    def est_vide(self):
        return self._contenu is None
        
    def empiler(self, e):
        self._contenu = Cellule(e, self._contenu)
        
    def depiler(self):
        if self.est_vide():
            raise IndexError("depile une pile vide")
        v = self._contenu.v
        self._contenu = self._contenu.s
        return v

    def consulter(self):
        if(self._contenu is not None):
            return self._contenu.v

        raise IndexError("Pas d'elements dans la pile !")

    def vider(self):
        self._contenu = None

    # O(x) complexité lineaire
    def __len__(self):
        return tailleCellule(self._contenu)


def tailleCellule(cellule):
    if cellule is None:
        return 0
    return 1 + tailleCellule(cellule.s)