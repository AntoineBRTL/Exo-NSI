def _concatener(l1, l2):
    if l1 is None:
        return l2
    else:
        return Cellule(l1.valeur, _concatener(l1.suivante, l2)) 

def _niemeElement(n, l):
    if l is None:
        raise IndexError("Index invalide")
    elif n == 0:
        return l.valeur
    else:
        return _niemeElement(n - 1, l.suivante)

class Cellule:
    def __init__(self, v, s):
        self.valeur = v
        self.suivante = s
    
    def longueur(self):
        n = 0
        c = self
        while c is not None:
            n += 1
            c = c.suivante
        return n

    def concatener(self, l2):
        _concatener(self, l2)

    def __str__(self):
        return _strListe(self)

def _renverser(l):
    r = None
    c = l
    while c is not None:
        r = Cellule(c.valeur, r)
        c = c.suivante
    return r

class Liste:
    def __init__(self):
        self._tete = None

    def estVide(self):
        return self._tete is None

    def ajoute(self, x):
        self._tete = Cellule(x, self._tete)

    def __len__(self):
        n = 0
        c = self._tete
        while c is not None:
            n += 1
            c = c.suivante
        return n

    def __getitem__(self, n):
        return _niemeElement(n, self._tete)

    def renverser(self):
        self._tete = _renverser(self._tete)

    def __add__(self, l):
        r = Liste()
        r._tete = _concatener(self._tete, l._tete)
        return r

    def __str__(self):
        return _strListe(self._tete)

def _strListe(c):
    if c is None:
        return "\n"
    return str(c.valeur) + ", " + str(_strListe(c.suivante))