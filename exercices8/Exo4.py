def fusion(l1, l2):
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    if l2.valeur < l1.valeur:
        return Cellule(l2.valeur, fusion(l1, l2.suivante))
    else:
        return Cellule(l1.valeur, fusion(l1.suivante, l2))

def fusion(l1, l2):

    l = None

    while l1 is not None or l2 is not None:

        if l1 is not None and (l2 is None or l1.valeur < l2.valeur):
            l = Cellule(l1.valeur, l)

    return l