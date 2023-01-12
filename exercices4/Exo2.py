from msilib.schema import Error
from Liste import Cellule

def niemeElement(rc, n):
    c = rc
    x = 0
    while c is not None:
        if(n == x):
            return c.valeur
        x += 1
        c = c.suivante
    raise IndexError("Indice trop grand")