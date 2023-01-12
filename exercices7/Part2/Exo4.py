from .Exo2 import ajoute, appartient

def ajoute_sans_doublon(x, a):
    if not appartient(x, a):
        a = ajoute(x, a)
    return a