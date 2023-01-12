def str_arbre(a):
    if a is None:
        return ""

    return "(" + str_arbre(a.gauche) + str(a.valeur) + str_arbre(a.droite) + ")"