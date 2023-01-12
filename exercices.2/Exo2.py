def cree():
    return [0]

def contient(t, x):
    return t[0] & (1 << x) != 0

def ajoute(t, x):
    return t[0] | (1 << x)