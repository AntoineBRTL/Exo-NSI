def cree():
    return [0] * 6

def contient(s, x):
    iEntier = x // 64
    bit = x % 64
    return (s[iEntier] & (1 << bit) != 0)

def ajoute(s, x):
    iEntier = x // 64
    bit = x % 64
    s[iEntier] = s[iEntier] | (1 << bit)

def enumere(s):
    tab = []

    for entier in s:
        for bit in range(64):
            if entier & (1 << bit) != 0:
                tab.append(entier * 64 + bit)

    return tab